import numpy as np
import random
import os
import tensorflow as tf

from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras import Input, Model
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import LambdaCallback, ModelCheckpoint

class ModelConfig(object):
    poetry_file = './dataset/poetry.txt'
    weight_file = './model/poetry_models.h5'
    max_len = 6
    batch_size = 32
    learning_rate = 0.003

def preprocess_data(ModelConfig):
    files_content = ''
    with open(ModelConfig.poetry_file, 'r', encoding='UTF-8') as f:
        for line in f:
            x = line.strip() + "]"
            x = x.split(':')[1]
            if len(x) <= 5:
                continue
            if x[5] == '，':
                files_content += x

    words = sorted(list(files_content))
    counted_words = {}
    for word in words:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1

    delete_words = []
    for key in counted_words:
        if counted_words[key] <=2:
            delete_words.append(key)
    for key in delete_words:
        del counted_words[key]

    wordPairs = sorted(counted_words.items(), key=lambda x: -x[1])
    words, _ = zip(*wordPairs)
    words += (" ",)

    word2idx = dict((c, i) for i, c in enumerate(words))
    idx2word = dict((i, c) for i, c in enumerate(words))
    word2idx_dic = lambda x: word2idx.get(x, len(words) -1)
    return word2idx_dic, idx2word, words, files_content


class LSTMPoetryModel(object):
    def __init__(self, config: ModelConfig):
        self.model = None
        self.do_train = None
        self.loaded_model = True
        self.config = config

        self.word2idx_dic, self.idx2word, self.words, self.files_content = preprocess_data(self.config)

        self.poems = self.files_content.split(']')
        self.poems_num = len(self.poems)

        if os.path.exists(self.config.weight_file) and self.loaded_model:
            self.model = load_model(self.config.weight_file)
        else:
            self.train()

    def build_model(self):
        print('building model...')

        input_tensor = Input(shape=(self.config.max_len, len(self.words)))
        lstm = LSTM(512, return_sequences=True)(input_tensor)
        dropout = Dropout(0.6)(lstm)
        lstm = LSTM(256)(dropout)
        dropout = Dropout(0.6)(lstm)
        dense = Dense(len(self.words), activation = 'softmax')(dropout)
        self.model = Model(inputs=input_tensor, outputs=dense)
        optimizer = Adam(lr = self.config.learning_rate)
        self.model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    def data_generate(self):
        i = 0
        while True:
            x = self.files_content[i: i + self.config.max_len]
            y = self.files_content[i + self.config.max_len]
            if ']' in x or ']' in y:
                i += 1
                continue
            y_vec = np.zeros(
                shape=(1, len(self.words)),
                dtype=np.bool
                )
            y_vec[0, self.word2idx_dic(y)] = 1.0
            x_vec = np.zeros(
                shape=(1, self.config.max_len, len(self.words)),
                dtype=np.bool
                )
            for t, char in enumerate(x):
                x_vec[0, t, self.word2idx_dic(char)] = 1.0

            yield x_vec, y_vec
            i += 1
            
    def sample(self, preds, temperature=1.0):
        preds = np.asarray(preds).astype('float64')
        exp_preds = np.power(preds, 1./temperature)
        preds = exp_preds / np.sum(exp_preds)
        prob = np.random.choice(range(len(preds)), 1, p=preds)
        return int(prob.squeeze())


    def _pred(self, sentence, temperature=1):
        ''' 根据输入的最后五个字,返回单个预测的字'''
        
        if len(sentence) < self.config.max_len:
            print('_pred error sentence')
            return
        sentence = sentence[-self.config.max_len:]
        x_pred = np.zeros((1, self.config.max_len, len(self.words)))
        for t, char in enumerate(sentence):
            x_pred[0, t, self.word2idx_dic(char)] = 1.0
        preds = self.model.predict(x_pred, verbose=0)[0]
        next_index = self.sample(preds, temperature=temperature)
        next_char = self.idx2word[next_index]
        return next_char
        
    def _preds(self, sentence, length=23, temperature=1):
        ''' 根据输入的前五个字, 生成length个字'''
        
        sentence = sentence[:self.config.max_len]
        generate = ''
        for i in range(length):
            pred = self._pred(sentence, temperature)
            generate += pred
            sentence = sentence[1:]+pred
        return generate
    
    def predict_random(self, temperature = 1):
        ''' 1.从库中随机选取一句开头的诗句,生成五言绝句'''
        if not self.model:
            print('No available model')
            return

        index = random.randint(0, self.poems_num)
        sentence = self.poems[index][: self.config.max_len]
        generate = self.predict_sen(sentence, temperature=temperature)
        return generate

    def predict_first(self, char, temperature = 1):
        ''' 2.根据给出的首个字, 生成五言绝句'''
        if not self.model:
            print('No available model')
            return
        index = random.randint(0, self.poems_num)
        sentence = self.poems[index][1-self.config.max_len:] + char
        generate = str(sentence)
        generate += self._preds(sentence, length=23, temperature=temperature)
        return generate
    
    def predict_sen(self, text, temperature = 1):
        '''3. 根据给出的前max_len个字生成五言绝句'''
        if not self.model:
            return
        max_len = self.config.max_len
        if len(text) < max_len:
            print('给出的初始数字不能低于 %d\n' % max_len)
            return
        sentence = text[-max_len:]
        print('第一行为%s\n' % sentence)
        generate = str(sentence)
        generate += self._preds(sentence, length=24-max_len, temperature=temperature)
        return generate

    def predict_hide(self, text, temperature = 1):
        ''' 4. 给定4个字生成藏头诗'''
        if not self.model:
            print('predict_hide model not available')
            return
        if len(text) != 4:
            print('必须提供四个字')
            return

        index = random.randint(0, self.poems_num)
        # 初始化第一行
        sentence = self.poems[index][1-self.config.max_len:] + text[0]
        generate = str(text[0])

        for i in range(5):
            next_char = self._pred(sentence, temperature)
            sentence = sentence[1:] + next_char
            generate += next_char

        for i in range(3):
            generate += text[i+1]
            sentence = sentence[1:] + text[i+1]
            for j in range(5):
                next_char = self._pred(sentence, temperature)
                sentence = sentence[1:] + next_char
                generate += next_char
        return generate


    def generate_sample_result(self, epoch, logs):
        if epoch % 5 != 0:
            return
        with open('out/out.txt', 'a', encoding='utf-8') as f:
            f.write('=============第{}轮============\n'.format(epoch))

        print('=============第{}轮============\n'.format(epoch))
        for diversity in [0.7, 1.0, 1.3]:
            print('----------设置诗词创作自由度为{}--------------'.format(diversity))
            generate = self.predict_random(temperature=diversity)
            print(generate)

            with open('out/out.txt', 'a', encoding='utf-8') as f:
                f.write(generate + '\n')

    def train(self):
        print('Training...')
        number_of_epoch = len(self.files_content) - (self.config.max_len + 1) * self.poems_num
        number_of_epoch /= self.config.batch_size
        number_of_epoch = int(number_of_epoch / 1.5)
        print('EPOCHES is %d\n' % number_of_epoch)
        print('POEMS\' number is %d\n' % self.poems_num)
        print('文件长度为 %d' % len(self.files_content))
        if not self.model:
            self.build_model()

        self.model.fit(self.data_generate(),
                       verbose=True,
                       steps_per_epoch=self.config.batch_size,
                       epochs=number_of_epoch,
                       callbacks=[
                           ModelCheckpoint(self.config.weight_file, save_weights_only=False),
                           LambdaCallback(on_epoch_end=self.generate_sample_result)
                           ]
                       )

if __name__ == '__main__':
    model = LSTMPoetryModel(ModelConfig)
    print('Model loaded.')
    print('------------藏头诗----------')
    for i in range(3):
        # 藏头诗
        sen = model.predict_hide('云山雾花')
        print(sen)

    print('------------根据第一句生成----------')
    for i in range(3):
        # 给定第一句话进行预测
        sen = model.predict_sen('山阳空飞鸟')
        print(sen)

    print('------------给定第一个字生成----------')
    for i in range(3):
        # 给定第一个字进行预测
        sen = model.predict_first('鸟')
        print(sen)
    
    print('------------随机抽取第一句话生成----------')
    for temp in [0.5, 1.0, 1.5]:
        # 随机抽取第一句话进行预测
        sen = model.predict_random(temperature=temp)
        print(sen)

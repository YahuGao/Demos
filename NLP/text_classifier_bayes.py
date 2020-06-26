import jieba
import pandas as pd

DATA_DIR = "/home/ygao/Demos/NLP/data/"

NEWS_FILES = ["car_news.csv", "home_news.csv", "military_news.csv", "technology_news.csv", "entertainment_news.csv", "house_news.csv", "society_news.csv", "finance_news.csv", "international_news.csv", "sports_news.csv"]

STOPWORDS_FILE = "stopwords.txt"

def get_stopwords(stopwords_filename):
    with open(DATA_DIR + stopwords_filename, 'r') as f:
        stopwords = f.read().splitlines()
    return stopwords


def get_dataset(news_files, stopwords):
    dataset = []
    for filename in news_files:
        category = filename[:-9]
        contents = pd.read_csv(DATA_DIR + filename).dropna().content.values.tolist()
        for line in contents:
            try:
                segs = jieba.lcut(line)
                segs = list(filter(lambda x: len(x) > 1, segs))
                segs = list(filter(lambda x: x not in stopwords, segs))
                dataset.append((" ".join(segs), category))
            except:
                print(line)
                continue
    return dataset

def get_CountVectorizer(train_data, ngram):
    # 从数据中抽取词袋模型特征
    from sklearn.feature_extraction.text import CountVectorizer

    vec = CountVectorizer(
        analyzer='word',     # tokenize by character ngrams
        ngram_range=(1,ngram),
        max_features=4000,   # keep the most common 4000 ngrams
        )
    vec.fit(x_train)

    return vec
    
if __name__ == '__main__':
    stopwords = get_stopwords(STOPWORDS_FILE)
    dataset = get_dataset(NEWS_FILES[:3], stopwords)
    import random
    random.shuffle(dataset)
    x, y = zip(*dataset)
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1234)
    import time
    for ngram in range(1,5):
        start_time = time.time()
        vectorizer = get_CountVectorizer(x_train, ngram)
        from sklearn.naive_bayes import MultinomialNB
        classifier = MultinomialNB()
        classifier.fit(vectorizer.transform(x_train), y_train)
        end_time = time.time()
        print("ngram is: %d, Cost %.2fs" % (ngram, end_time - start_time), end=' ')
        print("score is %.2f." % classifier.score(vectorizer.transform(x_test), y_test))

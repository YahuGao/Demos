import pandas as pd
import jieba

files = ["data/car_news.csv", "data/home_news.csv", "data/military_news.csv", "data/technology_news.csv", "data/entertainment_news.csv", "data/house_news.csv", "data/society_news.csv", "data/finance_news.csv", "data/international_news.csv", "data/sports_news.csv"]

file_nums = len(files)

def get_words2ct(filename):
    df = pd.read_csv(filename)
    df = df.dropna()
    contents = df.content.values.tolist()
    words2ct = {}
    for content in contents:
        try:
            content = content.strip()
            segments = jieba.lcut(content)
            for segment in segments:
                if len(segment) > 1 and segment != '\r\n':
                    words2ct[segment] = words2ct.get(segment, 0) + 1
        except Exception as e:
            print(e)
            print(content, end="  ")
            continue

    return words2ct

def get_words2tf(words2ct):
    counts = sum(words2ct.values())
    words2tf = {word:count/counts for word, count in words2ct.items()}
    return words2tf

def get_words2idf(words2ct, other_words2cts):
    cts_other_documents = len(other_words2cts)
    words2idf = {}
    for word,_ in words2ct.items():
        count = 1
        for other_words2ct in other_words2cts:
            if word in other_words2ct:
                count += 1
        words2idf[word] = cts_other_documents / count

    return words2idf
        
def get_words2tfidf(words2tf, words2idf):
    words2tfidf = {}
    for word in words2tf.keys():
        words2tfidf[word] = words2tf[word] * words2idf[word]
    return words2tfidf
        
if __name__ == '__main__':
    words2cts = []
    words2tfs = []
    words2idfs = []
    words2tfidfs = []
    for filename in files:
        words2ct = get_words2ct(filename)
        words2tf = get_words2tf(words2ct)
        words2cts.append(([filename[5:-9]], words2ct))
        words2tfs.append(([filename[5:-9]], words2tf))

    for index in range(len(words2cts)):
        other_words2cts = []
        for item in words2cts[0:index]:
            other_words2cts.append(item[1])
        for item in words2cts[index+1:]:
            other_words2cts.append(item[1])
        words2idf = get_words2idf(words2cts[index][1], other_words2cts)
        words2tfidf = get_words2tfidf(words2tfs[index][1], words2idf)
        words2tfidf = sorted(words2tfidf.items(), key=lambda x:x[1], reverse=True)
        words2tfidfs.append((words2cts[index][0], words2tfidf))

    for index in range(len(words2tfidfs)):
        print(words2tfidfs[index][0])
        print(words2tfidfs[index][1][:10])    

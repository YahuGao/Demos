import numpy as np
import pandas as pd
import jieba
import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def get_segments(filename):
    segments = []
    df = pd.read_csv(filename, encoding='utf-8')
    contents = df["content"].values.tolist()
    # print(contents[:5])
    for content in contents:
        try:
            segs = jieba.lcut(content)
            for seg in segs:
                if len(seg) > 1 and seg != '\r\n':
                    segments.append(seg)
        except Exception as e:
            #            print(content)
            continue

    return segments


def get_stopwords(stopword_file):
    stopwords_df = pd.read_csv(stopword_file, index_col=False,
                               quoting=3, sep="\t", names=['stopword'], encoding='utf-8')
    return stopwords_df


def data_process(segments):
    segments = pd.DataFrame({'segment': segments})
    # Remove stopword
    stopwords = get_stopwords('data/stopwords.txt')
    segments = segments[~segments.segment.isin(stopwords.stopword)]
    segments['counter'] = np.ones((segments.shape[0],))
    segments = segments.groupby(by=segments['segment']).count()
    segments = list(zip(segments.index, segments.counter.values))
    segments = sorted(segments, key=lambda x: x[1], reverse=True)
    return segments


def draw_wordCloud(segments):
    word_fequence = {x[0]: x[1] for x in segments[:1000]}
    matplotlib.rcParams['figure.figsize'] = (12.0, 12.0)
    wordcloud = WordCloud(font_path="data/simhei.ttf",
                          background_color="white", max_font_size=80)
    wordcloud = wordcloud.fit_words(word_fequence)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    segments = get_segments('data/house_news.csv')
    segments = data_process(segments)
    draw_wordCloud(segments)

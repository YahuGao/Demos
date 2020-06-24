import jieba.analyse as analyse
import pandas as pd


def get_content(filename):
    df = pd.read_csv(filename)
    df = df.dropna()
    lines = df.content.values.tolist()
    content = " ".join(lines)
    return content


if __name__ == '__main__':
    filename = 'data/society_news.csv'
    content = get_content(filename)
    # allowPOS 仅包括指定词性的词，默认值为空，即不筛选
    keywords = analyse.extract_tags(
        content, topK=10, withWeight=False, allowPOS=())
    print("keywords with TF-IDF: ", keywords)
    keywords = analyse.textrank(
        content, topK=10, withWeight=False, allowPOS=('ns', 'n'))
    print("keywords with TextRank from 'ns' and 'n': ", keywords)
    keywords = analyse.textrank(
        content, topK=10, withWeight=False, allowPOS=('ns', 'v', 'vn', 'n'))
    print("keywords with TextRank from 'ns', 'n', 'v' and 'vn': ", keywords)

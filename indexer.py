import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer


def func(location):

    tk = TweetTokenizer()
    ps = PorterStemmer()

    n = len(location)

    wordsArray = []
    for i in range(n):
        file = open("uploads/{}".format(location[i]), encoding='utf8')
        read = file.read()
        file.seek(0)
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for ele in read:
            if ele in punc:
                read = read.replace(ele, " ")
        read = read.lower()
        words = tk.tokenize(read)
        for i in range(len(words)):
            words[i] = ps.stem(words[i])
        wordsArray.append(words)

    dict = {}

    for i in range(n):
        for item in wordsArray[i]:
            if item not in dict:
                dict[item] = {
                    "document_freq": 1,
                    "doc_numbers": [i+1],
                    "collection_freq": 0}
            if item in dict:
                if (i+1) not in dict[item]["doc_numbers"]:
                    dict[item]["doc_numbers"].append(i+1)
                dict[item]["collection_freq"] += 1
            dict[item]["document_freq"] = len(dict[item]["doc_numbers"])

    return dict

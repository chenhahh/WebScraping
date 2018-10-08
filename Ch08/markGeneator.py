# 根据马尔代夫模型,生成随机字符串
from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    """
    计算字典中出现次数总和
    :param wordList: 单词和频率
    :return: 总频率
    """
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    """

    :param wordList:字典
    :return: 出现的单词
    """
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    """
    根据给定的字符串构建单词字典
    :param text: 字符串
    :return: 字典
    """
    # 去除换行符和引号
    text = text.replace("\n", " ")
    text = text.replace("\"", "")

    # 保留标点符号
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")

    # 根据空格分割单词并过滤空单词
    words = text.split(" ")
    words = [word for word in words if word != ""]

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            # 为单词新建一个随后可能出现的单词字典
            wordDict[words[i-1]] = {}
        # 添加后一个单词到字典中
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]]+1

    return wordDict


text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# print(text)
wordDict = buildWordDict(text)
# print(wordDict)
# 生成链长100的马尔科夫链
length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)
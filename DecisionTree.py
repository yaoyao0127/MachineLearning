# -*- coding=utf-8 -*-
# python2.7
from math import log
import operator

# 创建简单的数据集
def creatDataset():
    dataSet = [[1, 1, 0, 'fight'], [1, 0, 1, 'fight'],
               [1, 0, 1,'fight'], [1, 0, 1, 'fight'],
               [0, 0, 1, 'run'], [0, 1, 0, 'fight'], [0, 1, 1, 'run']]
    labels = ['weapon', 'bullet', 'blood']
    return dataSet, labels

# 计算香农熵
def Shannon(dataSet):
    numEntries = len(dataSet)  # 数据集的条数
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]  # 现在所处的状态
        # 累计状态出现的次数
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            # print labelCounts
        labelCounts[currentLabel] += 1
    # print labelCounts
    shannon = 0
    for key in labelCounts:
        # key即为run和fight
        prob = float(labelCounts[key])/numEntries
        shannon -= prob * log(prob, 2)
    return shannon

def printData(myDat):
    for item in myDat:
        print '%s' % (item)
        
myDat, labels = creatDataset()
# printData(myDat)
print Shannon(myDat)
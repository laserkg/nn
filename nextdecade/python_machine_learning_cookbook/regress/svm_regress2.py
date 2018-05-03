#!/usr/bin/env python2.7
# encoding: utf-8
# Created by lizhishan on 2017/12/23

from sklearn import svm

X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
clf = svm.SVR()
clf.fit(X, y)
y_predict = clf.predict([[1, 1]])
clf.score(y_predict, [1.6])
if __name__ == '__main__':
    pass
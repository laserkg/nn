#!/usr/bin/env python2.7
# encoding: utf-8
# Created by lizhishan on 2017/12/21

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
input_classes = ['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw']

label_encoder.fit(input_classes)
print '\nClass Mapping: '
for i, item in enumerate(label_encoder.classes_):
    print item, '-->', i

# 单词被转换为从0开始的索引值。现在遇到一组标记，就可以轻松地替换他们了
labels = ['toyota', 'ford', 'audi']
encoded_labels = label_encoder.transform(labels)
print '\nLabels =', labels
print 'Encoded labels =', list(encoded_labels)

# 通过数字反转回单词的功能
encoded_labels = [2, 1, 0, 3, 1]
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print '\nEncoded labels =', encoded_labels
print 'Decoded labels =', list(decoded_labels)

if __name__ == '__main__':
    pass

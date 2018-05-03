#!/usr/bin/env python2.7
# encoding: utf-8
# Created by lizhishan on 2017/12/20

import numpy as np
from sklearn import preprocessing

data = np.array([
    [3, -1.5, 2, -5.4],
    [0, 4, -0.3, 2.1],
    [1, 3.3, -1.9, -4.3],
])

print '\nBefore scale, Mean = ', data.mean(axis=0)
print 'Before scale, Std deviation = ', data.std(axis=0)

# 均值移除
data_standardized = preprocessing.scale(data)
print data_standardized
print '\nMean = ', data_standardized.mean(axis=0)
print 'Std deviation = ', data_standardized.std(axis=0)

# 范围缩放(Scaling)

data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(data)
print '\nMin max Scaled data =', data_scaled

# 归一化（Normalization）
data_normalized = preprocessing.normalize(data, norm='l1')
print '\nL1 normalized data=', data_normalized

# 二值化
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)
print "\nBinarized data =", data_binarized

# one-hot encoding
encoder = preprocessing.OneHotEncoder()
encoder.fit([
    [0, 2, 1, 12],
    [1, 3, 5, 3],
    [2, 3, 2, 12],
    [1, 2, 4, 3]
])
encoder_vector = encoder.transform([
    [2, 3, 5, 3]
]).toarray()
print '\nEncoded vector =', encoder_vector


if __name__ == '__main__':
    pass

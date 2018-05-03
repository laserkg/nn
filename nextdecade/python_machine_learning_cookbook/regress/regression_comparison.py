# encoding: utf-8

import sys
import numpy as np

# filename = sys.argv[1]
filename = 'data_singlevar.txt'
X = []
y = []
with open(filename, 'r') as f:
    for line in f.readlines():
        xt, yt = [float(i) for i in line.split(',')]
        X.append(xt)
        y.append(yt)

# Train/test split
num_training = int(0.8 * len(X))
num_test = len(X) - num_training

# Training data
X_train = np.array(X[:num_training]).reshape((num_training,1))
y_train = np.array(y[:num_training])

# Test data
X_test = np.array(X[num_training:]).reshape((num_test,1))
y_test = np.array(y[num_training:])

from sklearn import linear_model

# Create linear regression object
linear_regressor = linear_model.LinearRegression()

# Train the model using the training sets
linear_regressor.fit(X_train, y_train)

# # Plot outputs
import matplotlib.pyplot as plt
#
# 拟合训练集数据
y_train_pred = linear_regressor.predict(X_train)
plt.figure()
plt.scatter(X_train, y_train, color='green')
plt.plot(X_train, y_train_pred, color='black', linewidth=4)
plt.title('Linear Training data')
plt.show()
#
# 看训练的模型预测了训练数据的输出结果，但这并不能说明模型对未知的数据也适用，因为我们是在训练数据上运行模型。
# 在测试集上预测
# Predict the output
y_test_pred = linear_regressor.predict(X_test)

plt.scatter(X_test, y_test, color='green')
plt.plot(X_test, y_test_pred, color='black', linewidth=4)
plt.xticks(())
plt.yticks(())
plt.title('Linear Test data')
plt.show()

from sklearn.svm import SVR
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_train_rbf = svr_rbf.fit(X_train, y_train).predict(X_train)
y_train_lin = svr_lin.fit(X_train, y_train).predict(X_train)
y_train_poly = svr_poly.fit(X_train, y_train).predict(X_train)


# 使用岭回归器,alpha越小越接近linear regressor，应该试着调大,0.01,0.1,1,3,5
ridge_regressor = linear_model.Ridge(alpha=0.5, fit_intercept=True, max_iter=10000)
ridge_regressor.fit(X_train, y_train)
# 拟合训练集数据
y_train_pred_ridge = ridge_regressor.predict(X_train)
plt.figure()
plt.scatter(X_train, y_train, color='green')
plt.plot(X_train, y_train_pred_ridge, color='black', linewidth=4)
plt.title('Ridge Training data')
plt.show()

##### 拟合训练数据，对比各种回归模型 ###
lw = 2
plt.scatter(X_train, y_train, color='darkorange',label='data')
plt.plot(X_train,y_train_pred, color='navy',lw=lw, label='Linear model')
plt.plot(X_train,y_train_pred_ridge,color='c',lw=lw, label='Ridge model')
plt.plot(X_train, y_train_rbf, color='tan', lw=lw, label='RBF model')
plt.plot(X_train, y_train_lin, color='gray', lw=lw, label='Linear model')
plt.plot(X_train, y_train_poly, color='maroon', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Regression Model omparation')
plt.legend()
plt.show()

# 拟合测试集数据
y_test_pred_ridge = ridge_regressor.predict(X_test)
plt.figure()
plt.scatter(X_test, y_test, color='green')
plt.plot(X_test, y_test_pred_ridge, color='black', linewidth=4)
plt.xticks(())
plt.yticks(())
plt.title('Ridge Test data')
plt.show()



# Measure performance
# 用误差来表示实际值与模型预测值之间的差值
import sklearn.metrics as sm
#
print "Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred), 2)
print "Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred), 2)
print "Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred), 2)
print "Explain variance score =", round(sm.explained_variance_score(y_test, y_test_pred), 2)
print "R2 score =", round(sm.r2_score(y_test, y_test_pred), 2)

print "\nRidge Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred_ridge), 2)
print "Ridge Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred_ridge), 2)
print "Ridge Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred_ridge), 2)
print "Ridge Explain variance score =", round(sm.explained_variance_score(y_test, y_test_pred_ridge), 2)
print "Ridge R2 score =", round(sm.r2_score(y_test, y_test_pred_ridge), 2)

# # # Model persistence
# # 模型训练后，将模型保存为文件，那么下次再使用的时候，只要简单地加载就可以了
# import cPickle as pickle
# #
# output_model_file = '3_model_linear_regr.pkl'
# #
# with open(output_model_file, 'w') as f:
#     pickle.dump(linear_regressor, f)
# #
# with open(output_model_file, 'r') as f:
#     model_linregr = pickle.load(f)
# #
# y_test_pred_new = model_linregr.predict(X_test)
# print "\nNew mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred_new), 2)


import pandas as pd
import numpy as np
import random
from sklearn import model_selection


def RepeatSample(df, w):
    '''
    :param df:
    :param w:
    :return:
    '''
    w_min = min(w)
    sampleFreq = [int(np.ceil(i/w_min)) for i in w]
    df2 = pd.Series()
    for i in range(df.shape[0]):
        freq = sampleFreq[i]
        for j in range(1,freq+1):
            df2 = pd.concat([df2,df.iloc[i]],axis = 1)
    df2 = df2.T
    df2.index = range(df2.shape[0])
    df2 = df2.drop(0)
    df2.index = range(df2.shape[0])
    return df2

def UpdateWeights(real,pred, w0, alpha):
    '''
    :param real:
    :param pred:
    :param w0:
    :return:
    '''
    if abs(real-pred)<0.0001:
        w1 = w0*np.exp(-alpha)
    else:
        w1 = w0*np.exp(alpha)
    return w1

def SimpleClassiferPred(df,ID,pred):
    '''
    :param df:带有预测值的数据集，其中每个样本可能 会有重复记录
    :param ID: 样本的唯一标识
    :param pred:样本的预测。同一样本可能会有不同的预测
    :return: 对重复样本，返回出现频率最高的预测值
    '''
    idPred = df.groupby([ID])[pred].mean()
    idPredDict = idPred.to_dict()
    idPredDict = {k:int(round(v)) for k,v in idPredDict.items()}
    return idPredDict

def  TrainAda(df, feature_list, iteration, y,featureSampling=False, treeDepth=3):
    '''
    :param df:训练集，包含特征和标签
    :param feature_list:特征集
    :param iteration: 迭代次数
    :param featureSampling: 从特征集中的抽样率。默认不进行特征抽样
    :param treeDepth每棵树的深度
    :return:每次迭代的权重和CART模型
    '''
    N = df.shape[0]
    w0 = np.array([1.0]*N)/N
    alpha_list = []
    cart_list = []
    df2 = df.copy()
    df2['ID'] = range(df.shape[0])
    df2['w0'] = w0
    for k in range(iteration):
        if not featureSampling:
            subFeatures = feature_list
        else:
            samplingSize = int(len(feature_list)*featureSampling)
            subFeatures = random.sample(feature_list, samplingSize)
        trainData = RepeatSample(df2, w0)
        trainData[y] = trainData[y].astype(float)
        cart = TrainCART(trainData,subFeatures,y,treeDepth)
        trainData['pred'] = trainData[subFeatures].apply(lambda x: predCART(x, cart), axis=1)
        predicion = SimpleClassiferPred(trainData,'ID','pred')
        df2['pred'] = df2['ID'].map(predicion)
        err_pred = trainData.apply(lambda x: abs(x[y] - x.pred), axis=1)
        err = sum(err_pred)/N
        if err >= 0.5:   #预测错误率超过0.5的分类器进行舍弃
            continue
        alpha = 0.5*np.log((1-err)/err)
        cart_list.append(cart)
        alpha_list.append(alpha)
        w2 = df2.apply(lambda x: UpdateWeights(x[y], x.pred, x.w0, alpha),axis = 1)
        w0 = [i/sum(w2) for i in w2]
        df2['w0'] = w0
        if err<=0.00001:
            break
    return {'alpha':alpha_list, 'cart model':cart_list}


AllData = pd.read_csv('C:/Users/OkO/Desktop/Financial Data Analsys/3nd Series/Public/bank.csv', header=0)
Attributes = list(AllData.columns)
Attributes.remove('y')
AllData['y2'] = AllData['y'].apply(lambda x: int(x == 'yes'))
#fewerAttributes = [u'age', u'job', u'marital', u'education', u'default', u'cash_loan', u'contact_number_type', u'maturity']

smallData = AllData[Attributes+['y2']]

df1 = smallData.loc[smallData['y2'] == 1]
df0 = smallData.loc[smallData['y2'] == 0]
df0_2 = df0.iloc[0:1000]
myData= pd.concat([df0_2,df1])

X_train,X_test = model_selection.train_test_split(myData,test_size=0.4, random_state=0)

x1 = X_train.copy()
x2 = X_test.copy()
cart = TrainCART(x1,Attributes,'y2',9)
x2['y3'] = x2[Attributes].apply(lambda x: predCART(x, cart), axis=1)
err_pred = x2.apply(lambda x: abs(x.y2 - x.y3), axis=1)
err = sum(err_pred)*1.0/len(err_pred)
print err   #0.597701149425


T = 10
AdaModel = TrainAda(X_train, Attributes, T, y)
alpha = AdaModel['alpha']
cart_list = AdaModel['cart model']
pred = X_test[Attributes].apply(lambda x: predCART(x, cart_list[0])*alpha[0], axis=1)
for k in range(1,T):
    pred2 = X_test[Attributes].apply(lambda x: predCART(x, cart_list[k])*alpha[k], axis=1)
    pred = pd.concat([pred,pred2],axis=1)
X_test['ada'] = pred.apply(sum,axis=1)
X_test['ada'] = X_test['ada'].map(lambda x: int(x>0.5))
err_pred = X_test.apply(lambda x: abs(x.y2 - x.ada), axis=1)
err = sum(err_pred)*1.0/len(err_pred)
print err #  0.40229885057471265
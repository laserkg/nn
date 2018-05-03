# encoding: utf-8

import types
import numbers

def Gini(df, var, y):
    '''
    :param df:数据集，包含了需要计算Gini指数的特征和标签
    :param y: 标签，0或1
    :return: Gini指数
    '''
    n = df.shape[0]
    n1 = sum(df[y])
    n2 = n - n1
    return 1- (n1*1.0/n)**2-(n2*1.0/n)**2

def Terminate(df, feature_list, y):
    '''
    :param df: 当前构建CART的数据集
    :param feature_list: 当前构建CART的特征集
    :param y: 标签
    :return: 终止与否
    '''
    majorityClass = int(sum(df[y])*1.0/df.shape[0]>=0.5)
    if feature_list == []:
        return majorityClass
    if df[feature_list].drop_duplicates().shape[0] == 1:
        return majorityClass
    if len(set(df[y])) == 1:
        return majorityClass
    return 'subTree'


def FeatureType(df, var):
    if isinstance(df.iloc[0][var],numbers.Real):
        return 'numerical'
    else:
        return 'categorical'


def NumFeatureSplit(df,var,y):
    '''
    :param df:
    :param var:
    :param y:
    :return:
    '''
    x = sorted(list(set(df[var])))
    split_gini = {}
    N = df.shape[0]
    for i in range(1,len(x)):
        threshold = 0.5*(x[i-1]+x[i])
        df_sub1 = df[df[var]<=threshold]
        df_sub2 = df[df[var] > threshold]
        n1, n2 = df_sub1.shape[0], df_sub2.shape[0]
        varGini = n1*1.0/N*Gini(df_sub1, var, y) + n2*1.0/N*Gini(df_sub2, var, y)
        split_gini[threshold] = varGini
    return {'splittedPoint' : min(split_gini,key=split_gini.get), 'minGini' : min(split_gini.values())}


def CatFeatureSplit(df,var,y):
    '''
    :param df:
    :param var:
    :param y:
    :return:
    '''
    avgLabel = df.groupby([var])[y].mean().to_frame()
    avgLabelSorted = avgLabel.sort_values(by=y)
    CatVar = list(avgLabelSorted.index)
    Cat2Num = {CatVar[i]:i for i in range(len(CatVar))}
    df['temp_col'] = df[var].map(Cat2Num)
    splitNumerical = NumFeatureSplit(df, 'temp_col', y)
    splitted_new_var = [k for k in Cat2Num.keys() if Cat2Num[k]<=splitNumerical['splittedPoint']]
    return {'splittedPoint':splitted_new_var,'minGini':splitNumerical['minGini']}

def TrainCART(df,feature_list,y, depth = 10000):
    '''
    :param df: 建立CART的数据集
    :param feature_list: 用于模型开发的特征的列表
    :param y: 标签，取值0，1
    :param depth: 树的深度。当指明深度时，设置该参数。
    :return: 叶子节点，或者子树。最终返回字典形式的CART树
    '''
    child = Terminate(df, feature_list, y)
    majorityClass = int(sum(df[y]) * 1.0 / df.shape[0] >= 0.5)
    if child in [0,1]:
        return child
    if depth == 0:
        return majorityClass
    featureGini = {}
    for feature in feature_list:
        if len(set(df[feature])) == 1:
            return majorityClass
        if FeatureType(df,feature) == 'numerical':
            featureSplit = NumFeatureSplit(df,feature,y)
        else:
            featureSplit = CatFeatureSplit(df, feature, y)
        featureGini[feature] = [featureSplit['splittedPoint'],featureSplit['minGini']]
    sortedFeatureGini = sorted(featureGini.items(),key=lambda x: x[1][1])
    bestFeature, bestSplit = sortedFeatureGini[0][0], sortedFeatureGini[0][1][0]

    cartResult = {bestFeature:{}}
    if type(bestSplit) == types.ListType:
        subTreeFeatures = [i for i in feature_list if i != bestFeature]
        bestFeaturesVals = list(set(df[bestFeature]))


        leftTree = df.loc[df[bestFeature].isin(bestSplit)]
        leftVals = bestSplit

        cartResult[bestFeature][str(leftVals)] = TrainCART(leftTree,subTreeFeatures,y,depth-1)

        rightTree = df.loc[~df[bestFeature].isin(bestSplit)]
        rightVals = [i for i in bestFeaturesVals if i not in set(leftVals)]
        cartResult[bestFeature][str(rightVals)] = TrainCART(rightTree, subTreeFeatures, y,depth-1)
    else:
        subTreeFeatures = [i for i in feature_list if i != bestFeature]

        leftTree = df.loc[df[bestFeature]<=bestSplit]

        cartResult[bestFeature]["<="+str(bestSplit)] = TrainCART(leftTree, subTreeFeatures, y,depth-1)

        rightTree = df.loc[df[bestFeature]>bestSplit]
        cartResult[bestFeature][">"+str(bestSplit)] = TrainCART(rightTree, subTreeFeatures, y,depth-1)

    return cartResult


def predCART(record, cart):
    root, subTree = cart.items()[0]
    for k, v in subTree.items():
        if type(v).__name__ == 'dict':
            return predCART(record, v)
        else:
            if k.find('>') > -1 or k.find('<=') > -1:
                if eval(str(record[root])+k):
                    return v
                else:
                    return 1-v
            else:
                if record[root] in eval(k):
                    return v
                else:
                    return 1-v


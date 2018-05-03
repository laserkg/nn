# encoding: utf-8
# !/usr/bin/env python2.7

# training
import graphviz as graphviz
from sklearn import tree

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# predict
predict_result = clf.predict([[2., 2.]])

predict_probality = clf.predict_proba([[2., 2.]])

print predict_result, predict_probality




# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("iris")

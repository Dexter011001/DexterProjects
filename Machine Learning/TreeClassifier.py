from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus


#Training data [Power,Seats]
X = [[380,2],[420,2,],[200,8],[240,9]]
Y = ['sport','sport','mini-van','mini-van']
target_names = ['sport','minivan']
features_name = ['power','seats']

#Training the data using decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

#Test data
prediction = clf.predict([[600,2]])
print(prediction)

#graphing the data
dot_data = StringIO()
tree.export_graphviz(clf,out_file=dot_data,
	feature_names=features_name,
	class_names=target_names,
	filled=True,rounded=True,
	impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())


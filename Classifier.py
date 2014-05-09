from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import svm

def accuracy(output,result):
	match=0	
	length = len(result)
	for i in range(0,length):
		if output[i]==result[i]:
			match=match+1
	
	return (match/(length+0.0))*100
	
		

def randomForrestClassifier(trainingFeatures,output,testFeatures):
	trainingFeatures = np.array(trainingFeatures)
	output = np.array(output)
	testFeatures = np.array(testFeatures)
	
	clf = RandomForestClassifier(n_estimators=50)
	clf = clf.fit(trainingFeatures[20:38],output[20:38])
	result = clf.predict(testFeatures[:19])
	
	acc=(accuracy(output[:19],result))
	print "randomForrest: %.2f "%(acc)

	print clf.score(testFeatures[:19],output[:19])
	clf_svm= svm.SVC(C=5)
	clf_svm = clf_svm.fit(trainingFeatures[20:38],output[20:38])
	result_2 = clf_svm.predict(testFeatures[:19])
	
	
	#print output[:19]
	#print result	
	acc=(accuracy(output[:19],result_2))
	print "SVM: %.2f "%(acc)
	print clf_svm.score(testFeatures[:19],output[:19])
	return (result)
	

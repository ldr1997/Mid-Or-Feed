'''
	main - The main program for our project.
	
	input:
	 - feature.csv
	 - labels.cav

	output: confusion matrix

	Authors:
	DELOS SANTOS, Angelo Vincent
	DEL ROSARIO, Luis Gabriel
	MIRANDA, Edrene Bryze
'''

from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix

def main():

	print("Getting files...")

	# get the feature vector
	fvFile = open('feature.csv', 'r')
	featureVect = []

	# append each line into a matrix
	for line in fvFile:
		a = line.split(',')
		a = list(map(int, a))
		featureVect.append(a)

	fvFile.close()

	# get the label vector
	rFile = open('labels.csv','r')
	labels = []

	# append each element into a list
	for line in rFile: labels.append(int(line))

	rFile.close()

	# split train and test datasets
	div = int(0.6*len(featureVect)) # 60% train, 40% test

	trainFV = featureVect[:div]
	testFV = featureVect[div:]

	trainLabels = labels[:div]
	testLabels = labels[div:]
	print("Done!\n")
	
	# scale data for better implementation with ANN
	trainFV = preprocessing.scale(trainFV)
	testFV = preprocessing.scale(testFV)

	#ANN
	annModel = MLPClassifier(activation='logistic', hidden_layer_sizes=(40), max_iter=10000)
	print("Fitting...")
	annModel.fit(trainFV, trainLabels)
	print("Done!")

	# print confusion matrices
	print("\nTraining data:\n--------------")
	print(confusion_matrix(trainLabels, annModel.predict(trainFV)))
	print("Testing data:\n-------------")
	print(confusion_matrix(testLabels, annModel.predict(testFV)))

main()
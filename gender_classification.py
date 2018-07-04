from sklearn import tree
from sklearn import ensemble
from sklearn import naive_bayes
from sklearn import discriminant_analysis
from  sklearn.metrics import accuracy_score
import numpy as np

clf= [tree.DecisionTreeClassifier(),ensemble.AdaBoostClassifier(), naive_bayes.GaussianNB(),
    discriminant_analysis.QuadraticDiscriminantAnalysis()] ;
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
#train on data
for  i in range(len(clf)):
     clf[i] = clf[i].fit(X, Y)


#user enter his/her data
height = input("Enter your height:")
weight =  input("Enter your weight:")
shoe_size = input("Enter your shoe_size:")
y_true = input("Enter your actual gender:")
inputdata = [int(height),int(weight),int(shoe_size)]

#calculate Predictions
prediction = []
for  i in range(len(clf)):
    prediction.append(clf[i].predict([inputdata]))

#calculate Scores
score =  []
for i in range(len(prediction)):
        score.append(accuracy_score([0] if y_true == "male" else [1] , [0] if prediction[i] == "male" else [1]))

print("\n Predictions: (left number -> probality of being female , right number -> probality of being male )")
#print predicts
for  i in range(len(prediction)):
    if i == 0 :
        print("DecisionTreeClassifier predicts: ",end = "")
    elif  i == 1:
        print("AdaBoostClassifier predicts: ",end = "")
    elif i == 2 :
        print("GaussianNB predicts: ",end = "")
    else :
        print("QuadraticDiscriminantAnalysis predicts: ",end = "")
    print(prediction[i] , "with probality " ,np.round((clf[i].predict_proba([inputdata])* 100),2))
    print("")

print("\n Scores: (1 -> right prediction, 0 -> wrong prediction)")
#print Scores
for  i in range(len(score)):
    if i == 0 :
        print("DecisionTreeClassifier scores: ",end = "")
    elif  i == 1:
        print("AdaBoostClassifier scores: ",end = "")
    elif i == 2 :
        print("GaussianNB scores: ",end = "")
    else :
        print("QuadraticDiscriminantAnalysis scores: ",end = "")
    print(score[i])
    print("")

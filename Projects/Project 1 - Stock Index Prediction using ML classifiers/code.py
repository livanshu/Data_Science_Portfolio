
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import time


### DATA PREPROCESSING ###

#Importing data
data = pd.read_csv (r'NASDAQ.csv')
print (data)
print (data['LABEL'].unique().tolist()) #To check number of variables i.e. should be only 2 (0 and1)
print(data.isnull().sum())
#Deleting non-useful attributes
del data['Date']

#Setting targets
y = data.LABEL
print (y)


### SPLITTING DATA ###

#Splitting training & Testing data in 3:1 ratio (only for Naive Bayesian & AdaBoost)
X = data.drop('LABEL',axis=1)
print (X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

### CLASSIFYING ###

## 1. Gaussian Naive Bayesian Classifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

#Training
start_NB_train = time.time()
gnb = GaussianNB()
gnb.fit(X_train,y_train)
end_NB_train = time.time()
print ()
print ("GAUSSIAN NAIVE BAYESIAN CLASSIFIER:")
print ("GNB Processing time : Training = %0.3fs " % (end_NB_train - start_NB_train))

#Testing
start_NB_test = time.time()
y_pred_NB = gnb.predict(X_test)
end_NB_test = time.time()
print ("GNB Processing time : Testing = %0.3fs " % (end_NB_test - start_NB_test))
print ("GNB Accuracy percentage = ",round(metrics.accuracy_score(y_test, y_pred_NB)*100,2),"%")
print ()


## 2. AdaBoost Classifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

#Training
start_AB_train = time.time()
ada = AdaBoostClassifier(DecisionTreeClassifier(), n_estimators=100, random_state = 0)
model = ada.fit(X_train, y_train)
end_AB_train = time.time()
print ("ADABOOST CLASSIFIER:")
print ("AdaBoost Processing time : Training = %0.3fs " % (end_AB_train - start_AB_train))

#Testing
start_AB_test = time.time()
y_pred_AB = ada.predict(X_test)
end_AB_test = time.time()
print ("AdaBoost Processing time : Testing = %0.3fs " % (end_AB_test - start_AB_test))
print ("AdaBoost Accuracy percentage = ",round(metrics.accuracy_score(y_test, y_pred_AB)*100,2),"%")
print ()

### Confusion Matrix
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

con_NB = confusion_matrix(y_test,y_pred_NB)
con_AB = confusion_matrix(y_test,y_pred_AB)
con_SVM = confusion_matrix(y_test,y_pred_SVM)
class_names=[0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

sns.heatmap(pd.DataFrame(con_NB), annot=True, cmap="PuRd" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix for Naive Bayesian', y=1.1)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

sns.heatmap(pd.DataFrame(con_AB), annot=True, cmap="Blues" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix for AdaBoost', y=1.1)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

sns.heatmap(pd.DataFrame(con_SVM), annot=True, cmap="Blues" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix for AdaBoost', y=1.1)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

### ROC
import sklearn.metrics as metrics
probs_gnb = gnb.predict_proba(X_test)
preds_gnb = probs_gnb[:,1]
fpr_gnb, tpr_gnb, threshold_gnb = metrics.roc_curve(y_test, preds_gnb)
roc_auc_gnb = metrics.auc(fpr_gnb, tpr_gnb)

import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr_gnb, tpr_gnb, 'b', label = 'AUC of Naive Bayesian = %0.2f' % roc_auc_gnb)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

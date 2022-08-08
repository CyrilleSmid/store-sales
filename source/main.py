# Data
import numpy as np
import pandas as pd
import numexpr

# Models
from sklearn.linear_model import LogisticRegression 
from sklearn.linear_model import Perceptron
from sklearn import svm #Support Vector Machine
from sklearn.ensemble import RandomForestClassifier 
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.naive_bayes import GaussianNB #Naive bayes
from sklearn.tree import DecisionTreeClassifier #Decision Tree
from sklearn.model_selection import train_test_split #training and testing data split
from sklearn import metrics #accuracy measure
from sklearn.metrics import confusion_matrix 
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessRegressor

# Model Helpers
from sklearn.model_selection import KFold 
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import cross_val_predict 
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn import feature_selection
from sklearn import model_selection
from sklearn import metrics

#Other
import re

if __name__ == "__main__":
    df = pd.read_csv("../datasets/train.csv")
    print(df.describe())
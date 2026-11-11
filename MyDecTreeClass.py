#-------------------------------------
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import confusion_matrix

class MyDecisionTree:

    def __init__(self):
        self.df = pd.read_csv('data_banknote_authentication.csv')
        self.df.head()
        self.X = self.df.drop('forged', axis = 'columns')
        self.y = self.df.forged
        self.seedValue = 1
        self.X_train=None
        self.X_test=None
        self.y_train=None
        self.y_test = None
        self.tree = DecisionTreeClassifier()
        self.y_hat = None
        self.cm =None

    def updateSeed(self,newValue):
        self.seedValue = newValue

    def trainData(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=50,random_state=self.seedValue, stratify=self.y)

        self.tree = DecisionTreeClassifier()
        self.tree.fit(self.X_train, self.y_train)

    def makePrediction(self, variance , skewness, curtosis, entropy):
        # Create the pandas DataFrame
        input_data = [[variance, skewness, curtosis, entropy]]
        df2 = pd.DataFrame(input_data, columns=['variance', 'skewness', 'curtosis', 'entropy'])
        cm_result = self.tree.predict(df2)
        return cm_result[0]
    def testData(self):
        self.y_hat = self.tree.predict(self.X_test)
        print('Data')
        print(self.X_test)
        # Model Accuracy, how often is the classifier correct?
        print("Accuracy:", accuracy_score(self.y_test, self.y_hat))
        #print("Accuracy:", tree.score(X_test, y_test))

        # confusion matrix
        cm = confusion_matrix(self.y_test, self.y_hat)
        return cm, accuracy_score(self.y_test, self.y_hat)

    def readCategories(self):
        result=''
        index=0
        setOfCategories = set(self.y)
        for catName in sorted(setOfCategories):
            if (index>0):
                result += " / "
            result += catName
            index+=1
        return result
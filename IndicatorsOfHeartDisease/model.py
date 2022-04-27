from tkinter.messagebox import NO
from extract import Extract
from transform import Transform
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import pd_options as pdo
import pandas as pd
import numpy as np
import sys


class Model(object):
    def __init__(self, filename):
        '''
            Currently only accepts .csv files.
        '''
        if '.csv' not in filename:
            raise Exception('The Model object only accepts .csv files at this time.')
        self.score = None
        self.filename = filename
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.predictions = None

        self.prepare_data()


    def prepare_data(self):
        try:
            self.data = pd.read_csv(self.filename)
        except Exception as ERROR:
            raise
    
        print(f'\n\nData Shape: {self.data.shape[0]}')
        print('\n\n------  Cleaning data   ------')
        print(f'\n\nNumber of Data Records: {self.data.shape[0]}')
        self.data = Transform.clean_data(self.data)
        print(f'\n\nNumber of Data Records After Dupe Drop: {self.data.shape[0]}')

        print('\n\n------  Head of data   ------')
        print(self.data.head())

        print('\n\n------  Data details   ------')
        print(self.data.describe())

        print('\n\n')

        # Input
        # X
        # Output
        # y
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data.drop(columns=['HeartDisease']), 
            self.data['HeartDisease'], 
            test_size=0.2)


    def train(self):
        ''' 
        Columns:
            HeartDisease
            BMI
            Smoking
            AlcoholDrinking
            Stroke
            PhysicalHealth
            MentalHealth
            DiffWalking
            Sex
            AgeCategory
            Race
            Diabetic
            PhysicalActivity
            GenHealth
            SleepTime
            Asthma
            KidneyDisease
            SkinCancer
    
        '''
        self.model = DecisionTreeClassifier()
        self.model.fit(pd.get_dummies(self.X_train), pd.get_dummies(self.y_train))

        print('\n\nX_train: \n', self.X_train.head()) 
        print('\n\nX_test: \n', self.X_test.head())
        print('\n\ny_train: \n', self.y_train.head())
        print('\n\ny_test: \n', self.y_test.head())
        
        return self.model


    def test(self):
        # predict_data = [22.2, 'No', 'No', 'No', 3, 10, 'No', 'Male', range(55, 59), 'No', 'Yes', 'Good', 6, 'No', 'No', 'No']
        # 
        # print('predict data: \n', pd.DataFrame(predict_data, columns=data.columns))

        # predict_data = pd.get_dummies(pd.DataFrame(predict_data, columns=data.columns))
        self.predictions = self.model.predict(pd.get_dummies(self.X_test))
        print('Test Predictions: \n', self.predictions)

        return self.predictions


    def predict(self, data):
        self.predictions = self.model.predict(pd.get_dummies(data))
        print('Predictions: \n', self.predictions)
        return self.predictions


    def get_accuracy(self):
        score = accuracy_score(pd.get_dummies(self.y_test), self.predictions)

        self.score = score
        return self.score



if __name__ == '__main__':
    # set pandas options for better visuals
    pdo.set_pandas_display_options(max_columns=1000, max_rows=1000, max_colwidth=199, width=1000)
    if not sys.argv[1]:
        raise Exception('Please provide a file name.')

    model = Model(sys.argv[1])
    model.train()
    model.test()
    print('Model Accuracy: ', model.get_accuracy())

    
    
    
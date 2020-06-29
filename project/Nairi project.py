## for data
import pandas as pd
import numpy as np

## for machine learning
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

## for validation
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation

## for plotting
import matplotlib.pyplot as plt


class realEstate:
    def __init__(self,train,test):
        self.train = train
        self.test = test

    def validation(self):
        self.schema = Schema([
            Column('condition', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(),
                                 MatchesPatternValidation('good|newly repaired|zero condition')]),
            Column('district', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(),
                                MatchesPatternValidation(
                                    'Arabkir|Center|Shengavit|Malatia-Sebastia|Avan|Nor Norq|Qanaqer-Zeytun|Davtashen|Erebuni|Achapnyak|Norq Marash|Vahagni district')]),
            Column('building_type', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(),
                                     MatchesPatternValidation('stone|panel|other|monolit')]),
            Column('price', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(), CanConvertValidation(float),
                             InRangeValidation(10000, 1000001)]),
            Column('area', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(), CanConvertValidation(float),
                            InRangeValidation(1, 1000)]),
            Column('num_bathrooms',
                   [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(), CanConvertValidation(int),
                    InRangeValidation(0, 100)]),
            Column('ceiling_height',
                   [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(), CanConvertValidation(float),
                    InRangeValidation(0, 10)]),
            Column('region', [MatchesPatternValidation('Yerevan')]),

            # below columns are not validated as the latters are dropped in the preprocessing
            Column('Unnamed: 0'),
            Column('max_floor'),
            Column('street'),
            Column('num_rooms'),
            Column('url'),
            Column('floor')
        ])

        self.errors = self.schema.validate(self.test)

        for error in self.errors:
            print(error)

    def plotting(self,x,y):

        xx = self.train[x].values.reshape(-1, 1)
        yy = self.train[y].values.reshape(-1, 1)

        linear_regressor = linear_model.LinearRegression()
        linear_regressor.fit(xx, yy)  # perform linear regression

        Y_pred = linear_regressor.predict(xx)
        plt.scatter(xx, yy)
        plt.plot(xx, Y_pred, color='red')
        plt.xlabel(x, fontsize=11)
        plt.ylabel(y, fontsize=11)
        plt.show()

    def preprocessing(self):

        # the column "url" is excluded as most of the data was unique
        # the column "Unnamed: 0" is excluded as the column name doesn't precisely describe the data included
        # the column "region" is excluded as the value was the same for the all rows
        # the columns "max_floor" and "floor" are excluded as they have insignificant correlation with the column "price"

        # the columns "area" and "num_rooms" are highly correlated with each other and the correlation between the columns
        ## "area" and "price" is nearly twofold the one between the columns "num_rooms" and "price", consequently the
        ## column "num_rooms" adds little value and can be excluded

        # the column "street" is excluded as the column "district" mainly contains the information of the column "street"
        ## and the data in the column "district" is more convenient for numeration

        self.train = self.train.drop(labels=['url', 'Unnamed: 0', 'region', 'max_floor', 'floor', 'num_rooms', 'street'],
                                 axis=1)
        self.test = self.test.drop(labels=['url', 'Unnamed: 0', 'region', 'max_floor', 'floor', 'num_rooms', 'street'],
                               axis=1)


        # numeration of the column "condition" for both train and test data (one hot encoding)
        ## train data
        self.tr_condition = pd.get_dummies(self.train['condition'], prefix='condition')
        self.train = pd.concat([self.train, self.tr_condition], axis=1)

        ## test data
        self.te_condition = pd.get_dummies(self.test['condition'], prefix='condition')
        self.test = pd.concat([self.test, self.te_condition], axis=1)

        # numeration of the column "building_type" for both train and test data (one hot encoding)
        ## train data
        self.tr_building_type = pd.get_dummies(self.train['building_type'], prefix='building_type')
        self.train = pd.concat([self.train, self.tr_building_type], axis=1)

        ## test data
        self.te_building_type = pd.get_dummies(self.test['building_type'], prefix='building_type')
        self.test = pd.concat([self.test, self.te_building_type], axis=1)

        # droping the original columns for the train data
        self.train = self.train.drop(['condition', 'building_type'], axis=1)

        # droping the original columns for the test data
        self.test = self.test.drop(['condition', 'building_type'], axis=1)


        # numeration of the column "district" for both train and test data.
        ## As the data mainly variates depending whether the house is in the center or not, the district column is filled with "1"s
        ## for the houses in the Center and with "0" otherwise.
        self.train['district'] = self.train['district'].map( {'Center': 1, 'Arabkir': 0, 'Malatia-Sebastia': 0, 'Erebuni': 0,
                                                              'Achapnyak': 0, 'Davtashen': 0, 'Qanaqer-Zeytun': 0, 'Nor Norq': 0,
                                                              'Avan': 0, 'Shengavit': 0, 'Norq Marash': 0, 'Vahagni district': 0,
                                                              'Nubarashen': 0} ).astype(int)

        self.test['district'] = self.test['district'].map( {'Center': 1, 'Arabkir': 0, 'Malatia-Sebastia': 0, 'Erebuni': 0,
                                                             'Achapnyak': 0, 'Davtashen': 0, 'Qanaqer-Zeytun': 0, 'Nor Norq': 0,
                                                             'Avan': 0, 'Shengavit': 0, 'Norq Marash': 0, 'Vahagni district': 0,
                                                             'Nubarashen': 0}).astype(int)
        return self.train, self.test

    def fit(self):
        self.train, self.test = self.preprocessing()

        # grouping the data into features (x) and value to be predicted (y) for both train and test data
        self.x_train = self.train.drop("price", axis=1)
        self.y_train = self.train["price"]

        self.regr = linear_model.LinearRegression()
        self.regr.fit(self.x_train, self.y_train)

        return self.regr.fit(self.x_train, self.y_train), self.test
        # print('Intercept: \n', self.regr.intercept_)
        # print('Coefficients: \n', self.regr.coef_)

    def predict(self):
        self.regr, self.test=self.fit()

        self.x_test = self.test.drop("price", axis=1)
        self.y_test = self.test["price"]

        return self.regr.predict(self.x_test), self.y_test

    def evaluation(self):
        self.regr.predict, self.y_test = self.predict()
        self.RMSE=np.sqrt(mean_squared_error(self.y_test, self.regr.predict))
        # self.RMSE = np.sqrt(np.average((self.y_test-self.regr.predict)**2))
        return self.RMSE


if __name__=="__main__":

    desired_width=320
    pd.set_option('display.width',desired_width)
    pd.set_option('display.max_columns',27)

    data = realEstate(pd.read_csv("houses_train.csv"),pd.read_csv("houses_test.csv"))

    data.validation()
    print(data.evaluation())
    data.plotting('area', 'price')
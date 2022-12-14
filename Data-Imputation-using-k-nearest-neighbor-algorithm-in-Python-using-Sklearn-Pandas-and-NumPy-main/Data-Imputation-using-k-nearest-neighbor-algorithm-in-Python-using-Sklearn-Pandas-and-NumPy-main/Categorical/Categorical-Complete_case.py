# import all necessary packages
import numpy as np
import pandas as pd
import math
import os
import glob

# import KNNImputer from sklearn.impute
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OrdinalEncoder
from numpy import asarray

# empty list for AE
AE_vals = []
# initialize count
count = 0

# set path=file_name in which the excel files are present
path = r'D:\Pooja\UNIVERSITY OF WINDSOR\Semester 3\Data mining\Project\Dataset and instructions\Incomplete Datasets\Incomplete Datasets Without Labels\TTTTEG'

# to read all the excel files present, use glob. Doing so, all excel files are loaded in csv_files
csv_files = glob.glob(os.path.join(path, "*.xlsx"))

# for loop to run over all the excel files
for f in csv_files:
    # load the original dataset
    real = pd.read_excel( r'D:\Pooja\UNIVERSITY OF WINDSOR\Semester 3\Data mining\Project\Dataset and instructions\Original Datasets\Original Datasets Without Labels\TTTTEG.xlsx',
        header=None)

    # load the incomplete dataset and copy the content
    df = pd.read_excel(f, header=None)
    data = df.copy()

    # complete dataframe
    df2 = pd.DataFrame(df.dropna())

    # Missing dataframe
    Incomplete_data = df[df.isnull().any(axis=1)]
    df1 = pd.DataFrame(Incomplete_data)

    # Loop runs only for the Missing values and calculates only with the complete instances
    for i in range(len(df1)):
        first = df1.head(1)
        df2 = pd.concat([first, df2], axis=0, ignore_index=False)

        # Removing the first row from the Missing Datafile
        df1 = df1.iloc[1:, :]

        # define ordinal encoding
        encoder = OrdinalEncoder()

        # transform data
        result = encoder.fit_transform(df)
        # print(result)

        # create an object for KNNImputer
        imputer = KNNImputer(n_neighbors=k, weights="uniform")

        # Perform Imputation and store it in a new dataframe
        After_imputation = imputer.fit_transform(result)
        df2 = pd.DataFrame(After_imputation)

        reverse_data_x = encoder.inverse_transform(After_imputation)
        final = pd.DataFrame(reverse_data_x)

    # compute AE
    comp = (real.to_numpy() == final.to_numpy())
    comp = pd.DataFrame(comp).replace({True: 1, False: 0})
    sumOfV = comp.values.sum()
    total = comp.count().sum()
    sumOfV, total
    AE = round(sumOfV / total, 4)
    AE_vals.append(AE)
    print(AE)

    # use count to keep track of the number of datasets that have been imputed in the loop
    count += 1
    # print(count)

print("Completed")


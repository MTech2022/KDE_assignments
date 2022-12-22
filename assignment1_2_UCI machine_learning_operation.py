import numpy as np
import pandas as pd
import scipy.stats as stats


def quntileQ1Q3IPR(data, col):
    Q3 = np.quantile(data[col], 0.75)
    Q1 = np.quantile(data[col], 0.25)
    IQR = Q3 - Q1
    print(f"{col}\n------------\nQ1={Q1}, Q3={Q3} & IQR={IQR}")
    print("``````````````````````````````````````````````````")


def dataMinMaxOtherCalculation(df):
    print("Total Datasets : ", df.size)
    print("\n~~~~~~~~~Standard deviation for all attributes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(df.std())
    print("\n\n~~~~~~~~~mean for all attributes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(df.mean())
    print("\n\n~~~~~~~~~median for all attributes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(df.median())
    print("\n\n~~~~~~~~~min for all attributes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(df.min())
    print("\n\n~~~~~~~~~max for all attributes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(df.max())
    print("`````````````````````````````````````````````````````````````````````````````````")

def normalization(columnValues):
    normalized_dataset = (columnValues - columnValues.min()) / (columnValues.max() - columnValues.min())
    return normalized_dataset;

def find_correlation(data_sets, attr1, attr2):
    attr1_value = data_sets[attr1]
    attr2_value = data_sets[attr2]
    print(attr1_value.corr(attr2_value))

# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
dataSets = pd.read_csv("./data/diabetes.csv")

dataMinMaxOtherCalculation(dataSets)

columns = dataSets.columns
print("\n\n~~~~~~~~~Q1 Q3 and IPR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
for col in columns:
    quntileQ1Q3IPR(dataSets, col)
    norm_colname = col + "_min_max_norm"
    dataSets[norm_colname] = normalization(dataSets[col])
    zscore_colname = col + "_zscore"
    dataSets[zscore_colname] = stats.zscore(dataSets[col])

print("=============Glucose, BloodPressure correlation======================")
find_correlation(dataSets, "Glucose", "BloodPressure");
print("\n=============SkinThickness, Insulin correlation======================")
find_correlation(dataSets, "SkinThickness", "Insulin");
print("\n=============SkinThickness, BloodPressure correlation======================")
find_correlation(dataSets, "SkinThickness", "BloodPressure");

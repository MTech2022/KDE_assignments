import numpy as np
import pandas as pd
import scipy.stats as stats


def quantile_Q1_Q3_IPR(data, col):
    Q3 = np.quantile(data[col], 0.75)
    Q1 = np.quantile(data[col], 0.25)
    IQR = Q3 - Q1
    print(f"{col}\n------------\nQ1={Q1}, Q3={Q3} & IQR={IQR}")
    print("``````````````````````````````````````````````````")


def data_min_max_other_calculation(df):
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
data_sets = pd.read_csv("../data/diabetes.csv")

print("==============================================================================================================\n"
    "i. Write a function which takes the datafile and attribute as parameters and \n"
    "computes the basic statistics for that attribute : numObj, minValue, maxValue, mean, stdev,Q1, median, Q3, IQR.\n"
    "Write a main program that computes the basic statistics for every attribute of the datafile and displays it.\n"
    "---------------------------------------------------------------------------------------------------------------");
print("----------------Data description : count,mean,std,min,25%,50%,75%,max-------------------------------------------")

print(data_sets.describe())
print("============================================================================")

data_min_max_other_calculation(data_sets)

print("\n\n~~~~~~~~~Q1 Q3 and IPR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
columns = data_sets.columns
for col in columns:
    quantile_Q1_Q3_IPR(data_sets, col)

print("ii. Write a function that takes the attribute which has to be normalised and the type of Normalization(min_max, z_score).\n"
      "Based on the normalisation type that is mentioned, apply the appropriate formula and \n"
      "return a dictionary where key = original value in the dataset, value = normalised value\n")
columns = data_sets.columns
for col in columns:
    norm_col_name = col + "_min_max_norm"
    data_sets[norm_col_name] = normalization(data_sets[col])
    zscore_col_name = col + "_zscore"
    data_sets[zscore_col_name] = stats.zscore(data_sets[col])
print("\nmin_max_norm for all the columns [Displaying only 10 records]\n")
for data in range(0, len(data_sets.head(10))) :
    print(data_sets["Pregnancies_min_max_norm"][data],"," ,data_sets["Glucose_min_max_norm"][data],"," ,
          data_sets["BloodPressure_min_max_norm"][data],"," ,data_sets["SkinThickness_min_max_norm"][data],"," ,
          data_sets["Insulin_min_max_norm"][data],"," ,data_sets["BMI_min_max_norm"][data],"," ,data_sets["DiabetesPedigreeFunction_min_max_norm"][data],"," ,
          data_sets["Age_min_max_norm"][data],"," ,data_sets["Outcome_min_max_norm"][data])

print("\nZ-score for all the columns [Displaying only 10 records]\n")
for data in range(0, len(data_sets.head(10))) :
    print(data_sets["Pregnancies_zscore"][data],"," ,data_sets["Glucose_zscore"][data],"," ,
          data_sets["BloodPressure_zscore"][data],"," ,data_sets["SkinThickness_zscore"][data],"," ,
          data_sets["Insulin_zscore"][data],"," ,data_sets["BMI_zscore"][data],"," ,data_sets["DiabetesPedigreeFunction_zscore"][data],"," ,
          data_sets["Age_zscore"][data],"," ,data_sets["Outcome_zscore"][data])

# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome

print("\n\niii. Write a function that takes 2 arguments which are the pair of attributes for which correlation has to be found out \n"
      "and computes the correlation between the two arguments.\n"
      "Write a main program that computes the correlation between every pair of attributes.\n")
print("\n=============Glucose, BloodPressure correlation======================")
find_correlation(data_sets, "Glucose", "BloodPressure");

print("\n=============SkinThickness, Insulin correlation======================")
find_correlation(data_sets, "SkinThickness", "Insulin");

print("\n=============SkinThickness, BloodPressure correlation======================")
find_correlation(data_sets, "SkinThickness", "BloodPressure");

import pandas as pd
from apyori import apriori

dataFrame = pd.read_csv('data/store_data.csv', header=None)
dataFrame.fillna(0, inplace=True);  # fill NaN to 0

transactions = []
for i in range(0, len(dataFrame)):
    transactions.append([str(dataFrame.values[i, j]) for j in range(0, 20) if str(dataFrame.values[i, j]) != '0'])
print("--------------------------------------------------------------------------");
print("Total number of Data for the apriori frequent pattern ", len(transactions));
print("--------------------------------------------------------------------------");
# print("=================================Data for the apriori frequent pattern finding=================================");
# for idx, i in enumerate(transactions):
#     print(f"{idx} :{i}")
#     print("---------------------------------------------------------------------------------------------------------------------------------");

print(
    "\nExample 1 : .................................................................With min_support=0.003..............................................................................................\n")
associationRules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)
aprioriRuleResults = list(associationRules)
print("Total Association Rules (With min_support=0.003) : ", len(aprioriRuleResults))
for idx, res in enumerate(aprioriRuleResults):
    print(idx, " : ", res)
print(
    "``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")

print(
    "\n\nExample 2 : .................................................................with min_support=0.004..............................................................................................\n")
associationRules = apriori(transactions, min_support=0.004, min_confidence=0.2, min_lift=3, min_length=2)
aprioriRuleResults = list(associationRules)
print("Total Association Rules (with min_support=0.004): ", len(aprioriRuleResults))

for idx, res in enumerate(aprioriRuleResults):
    print(idx, " : ", res)
print(
    "``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")

dataFrameResults = pd.DataFrame(aprioriRuleResults)
support = dataFrameResults.support

first_values = []
second_values = []
third_values = []
fourth_value = []

for i in range(dataFrameResults.shape[0]):
    single_list = dataFrameResults['ordered_statistics'][i][0]
    first_values.append(list(single_list[0]))
    second_values.append(list(single_list[1]))
    third_values.append(single_list[2])
    fourth_value.append(single_list[3])

lhs = pd.DataFrame(first_values)
rhs = pd.DataFrame(second_values)
confidence = pd.DataFrame(third_values, columns=['Confidence'])
lift = pd.DataFrame(fourth_value, columns=['lift'])

df_final = pd.concat([lhs, rhs, support, confidence, lift], axis=1)
df_final.fillna(value=' ', inplace=True)

df_final.columns = ['lhs', 1, 2, 'rhs', 3, 'support', 'confidence', 'lift']
df_final['lhs'] = df_final['lhs'] + str(", ") + df_final[1] + str(", ") + df_final[2]

df_final.drop(columns=[1, 2, 3], inplace=True)

print("=============> DISPLAYING ONLY HEAD 7 RECORDS...")
print(f"{df_final.head(7)}")

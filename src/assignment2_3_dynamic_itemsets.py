# Roll No : 12
# This is the basic implementation of DIC(Dynamic itemset algotithm)

import copy
import itertools


def generate_subset(S, n):
    #print(S)
    #print("---------- : generate_subset")
    a = itertools.combinations(S, n)
    result = []
    for i in a:
        result.append(set(i))
    return (result)


def generate_superset(S, unique_itemset):
    #print(S)
    #print("========== : generate_superset")
    result = []
    a = set()
    for i in unique_itemset:
        if i.intersection(S) == set():
            a = i.union(S)
            result.append(a)
            a = set()

    return (result)


def check_subset(S, FIS):
    subset = generate_subset(S, len(S) - 1)
    flag = 1
    temp = []

    for i in FIS:
        temp.append(i[0])

    FIS = temp
    for i in subset:
        if i not in FIS:
            flag = 0
            break

    if flag:
        return (True)
    else:
        return (False)


def transaction_to_itemset(T):
    result = set()
    for i in range(len(T)):
        if T[i] != 0:
            result.add(i + 1)

    return (result)


datasets = [[1, 1, 0], [1, 0, 0], [0, 1, 1], [0, 0, 0]]
unique_itemset = [{1}, {2}, {3}]
# datasets = [[1,1,0,1,1],[0,1,1,0,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,1],[0,1,1,1,0]]
# unique_itemset =[{1},{2},{3},{4},{5}]
min_support = 1
M = 2
dataset_size = len(datasets)

# 4 lists are implemented which store the state if itemsets in the database
DC = []
DS = []
SC = []
SS = []

print("==============================================================================================================\n"
      "I.Implement the following algorithms in Python for finding the frequent itemsets\n"
      "\tiii. Dynamic itemset Counting Algorithm.\n"
      "-------------------------------------------------------------------------------------------------------------\n")
print(f"Initial unique itemset : {unique_itemset}")
DC = [[i, 0, 0] for i in unique_itemset]
print("Initial Dynamic Count : ", DC, "\n")

counter = 0
T = []
while DC != [] or DS != []:
    for i in range(counter, counter + M):
        index = i % dataset_size
        T = transaction_to_itemset(datasets[index])
        print("Transaction :", T)
        print(
            f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{i}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for item in DC:
            item[2] += 1
            if item[0].issubset(T):
                item[1] += 1
        for item in DS:
            item[2] += 1
            if item[0].issubset(T):
                item[1] += 1

    for item in copy.copy(DC):
        if (item[1] >= min_support):
            DS.append(item)
            DC.remove(item)

    for item in copy.copy(DS):
        if (item[2] == dataset_size):
            SS.append(item)
            DS.remove(item)
    for item in copy.copy(DC):
        if (item[2] == dataset_size):
            SC.append(item)
            DC.remove(item)
    # print(DC)

    FIS = copy.copy(DS)
    FIS.extend(SS)
    for item in FIS:
        S = generate_superset(item[0], unique_itemset)
        for i in S:
            if check_subset(i, FIS):
                flag = 1
                for x in DC:
                    if x[0] == i:
                        flag = 0
                for x in DS:
                    if x[0] == i:
                        flag = 0
                for x in SC:
                    if x[0] == i:
                        flag = 0
                for x in SS:
                    if x[0] == i:
                        flag = 0
                if flag:
                    DC.append([i, 0, 0])

    counter += M
    print("DS(Dashed Square) - suspected frequent : ", DS)
    print("DC(Dashed Circle) - suspected infrequent : ", DC)
    print("SS(Solid Square) - frequent : ", SS)
    print("SC(Solid Circle) - infrequent: ", SC)
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

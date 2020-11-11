# -*- coding: utf-8 -*-
"""
Find the label.

@author: laith
"""

import csv
from copy import deepcopy
from operator import itemgetter


def k_selection(k, lineTest, dataTrain):
    dataSorted = dataSort(lineTest, dataTrain)
    return dataSorted[:k]  # get the k closer


def dataSort(lineTest, dataTrain):
    dataTrain_copie = deepcopy(dataTrain)
    for tab in dataTrain_copie:
        tab.append(distance(lineTest, tab))  # we add a 5th value in a copie of the dataset that represents the distance
    return list(sorted(dataTrain_copie, key=itemgetter(5)))  # sorted regarding the distance


def distance(L1, L2):
    """Euclidean distance."""
    return abs((((L1[0] - L2[0])**2 +
                 (L1[1] - L2[1])**2 +
                 (L1[2] - L2[2])**2 +
                 (L1[3] - L2[3])**2)**0.5))


def distribution(dataSelec):
    repart = [[dataSelec[0][4], 1]]  # initialisation, 1 is the occurence
    for tab in dataSelec[1:]:
        existe = False
        for r in repart:
            if tab[4] in r:  # 4th index is the label
                existe = True
                r[1] += 1  # occurence + 1
        if existe == False:
            repart.append([tab[4], 1])
    return repart  # fist value is the label, second is its occurence


def getlabel(dataSelec):
    """Get the most recurrent label."""
    repart = distribution(dataSelec)
    repartTrie = list(sorted(repart, key=itemgetter(1), reverse=True))  # most recurrent first
    return repartTrie[0][0]

# ________________________________________ Best K


def findlabel(k, dataTest, dataTrain):
    """Find all the label of a certain dataset."""
    label = []

    for lineTest in dataTest:
        irisSelec = k_selection(k, lineTest, dataTrain)  # get the top k data
        labelReturned = getlabel(irisSelec)  # get the label from the k top data
        label.append(labelReturned)

    return label


# ________________________________________ MAIN
if __name__ == '__main__':

    dataTrain = []
    f_train = open('Data/data.csv', 'r')
    reader = csv.reader(f_train, delimiter=';')
    for line in reader:
        for i in range(4):
            line[i] = float(line[i])  # Conversion des valeurs (string) en float
        dataTrain.append(line)
    f_train.close()

    dataTest = []
    f_test = open('Data/finalTest.csv', 'r')
    reader = csv.reader(f_test, delimiter=';')
    for line in reader:
        for i in range(4):
            line[i] = float(line[i])
        dataTest.append(line)
    f_test.close()

    k = 8  # according to the bestK opperation

    label = findlabel(k, dataTest, dataTrain)

    with open('Data/El_Mershati_Laith_Classification.txt', 'w') as out:
        for val in label:
            out.write(f'{val}\n')

# -*- coding: utf-8 -*-
"""
Find the k with the best accuracy for the main classification.

@author: laith
"""

import csv
import matplotlib.pyplot as plt
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


def bestK(dataTest, dataTrain):
    """Display a graphical representation of the amount of errors for each value of k, and the percentage of the best one."""
    vect_k = []
    vect_out = []

    for k in range(4, 12, 1):  # 7 data for k : approximately 60 seconds
        error = 0
        for lineTest in dataTest:
            labelTest = lineTest[4]  # get the true label of the data tested

            irisSelec = k_selection(k, lineTest, dataTrain)  # get the top k data
            labelReturned = getlabel(irisSelec)  # get the label from the k top data

            if labelTest != labelReturned:
                error += 1

        vect_k.append(k)
        vect_out.append(error)

    plt.plot(vect_k, vect_out)
    plt.title("Errors in the confusion matrix regarding k value\n")
    axes = plt.gca()
    axes.set_xlabel('k')
    axes.set_ylabel('errors')
    plt.show()

    minerror = min(vect_out)
    minindex = vect_out.index(minerror)
    bestk = vect_k[minindex]
    accuracy = 100 - (minerror/len(dataTest))*100

    print("Best K : ", bestk)
    print("Accuracy : {:.2f} %".format(accuracy))


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
    f_test = open('Data/preTest.csv', 'r')
    reader = csv.reader(f_test, delimiter=';')
    for line in reader:
        for i in range(4):
            line[i] = float(line[i])
        dataTest.append(line)
    f_test.close()

    bestK(dataTest, dataTrain)

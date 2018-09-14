import csv
import matplotlib.pyplot as plt
import numpy as np


def lerAquivo (file):
    arq_open = open(file)
    arq_read = arq_open.read()
    arq_format = arq_read.split("\n")
    arq_list = []
    for rows in arq_format:
        line = rows.split(",")
        arq_list.append(line)
    return arq_list

def getRow(list, row1, row2):
    new_list = []
    list_1 = []
    list_2 = []
    for row in list:
        list_1.append(row[row1])
        list_2.append(row[row2])
    new_list.append(list_1)
    new_list.append(list_2)
    return new_list

list  = lerAquivo("google.csv")
#new_data = getRow(list, 0, 1)
np_data = np.array(list)


print(list)

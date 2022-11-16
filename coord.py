#!/usr/bin/python
#Esse programa lê as coordenadas xyz do gmx traj do gromacs e plota em uma caixa 3D. Tornando possível visualizar o rastro da mesma.
#Necessario salvar em .csv e colocar no cabecalho t1;x1;y1;z1
###############################################################################################################################
#Criado por Flavia Assis#
# -*- coding: utf-8 -*-
# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
import pickle
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import sys

if (len(sys.argv) !=4):
    print("Invalid number of arguments.... try run \"python exec.py <input.csv> <boxkant(nm)> <output>\"")
else:
    try:
         input = open(sys.argv[1],'r')
         box = sys.argv[2]
         output = sys.argv[3]
         dataset = pd.read_csv(input, sep=';',parse_dates=True)
    except IOError:
        print("File not found...")
        exit()
    print('Running...')
    type(dataset)
    dataset.head()
    dataset.columns
    dataset.count()
    dataset.describe()
    threedee = plt.figure().gca(projection='3d')
    threedee.scatter(dataset['x1'], dataset['y1'], dataset['z1'], s=10)
    threedee.set_xlabel('x1')
    threedee.set_ylabel('y1')
    threedee.set_zlabel('z1')
    plt.ylim([0,float(box)])
    plt.xlim([0,float(box)])
    threedee.set_zlim(0,float(box))
    plt.show()
    plt.savefig(str(output)+'.png')

 print('**END**')


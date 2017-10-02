import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity='all' # - 전체 다 나온다 

import operator

import matplotlib.pyplot as plt
%matplotlib inline

def createDataSet():
    group = np.array([
        [1.0,1.1], [1.0,1.0], [0,0], [0,0.1],
        [2.0,2.1], [2.0,2.2], [1.0,0], [1.1,0]
    ])
    labels = ['A','A','B','B', 'C','C','D','D']
    return group, labels

def classfy0(inX, dataSet, labels, k):
       
    distances=((dataSet -inX)**2).sum(axis=1)
    sortIdx=distances.argsort()
    countArr={}
    
    
    for i in range(k) :
        countArr[labels[sortIdx[i]]] = countArr.get(labels[sortIdx[i]],0) + 1
    
    plt.scatter(x=dataSet[:,0], y=dataSet[:,1], label=labels, marker= True)
    plt.scatter(inX[0], inX[1])
    sortedArr=(sorted(countArr, key=countArr.get, reverse=True))
    
    for i in sortedArr:
        print("label :", i, "count :", countArr.get(i))
    
    
    #labeling for each point at Scatter diagram 
    for i, txt in enumerate(labels):
        plt.annotate(txt, (dataSet[i,0], dataSet[i,1]))
    print("\n", "It seems highly: ", sortedArr[0])   
       
    return countArr  
    

for i in range(group.shape[0]):
    print(group[i,0], group[i,1])

#Test

inX=[1.4,0.1]
group, labels = createDataSet()
a=classfy0(inX, group, labels, 3)
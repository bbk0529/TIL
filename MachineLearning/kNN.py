import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity='all' # - 전체 다 나온다 

import operator

import matplotlib.pyplot as plt
       

def classfy0_g(inX, dataSet, labels, k):
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

def classfy0(inX, dataSet, labels, k):
    distances=((dataSet -inX)**2).sum(axis=1)
    sortIdx=distances.argsort()
    countArr={}
    for i in range(k) :
        countArr[labels[sortIdx[i]]] = countArr.get(labels[sortIdx[i]],0) + 1
    sortedArr=(sorted(countArr, key=countArr.get, reverse=True))
    return  sortedArr[0]  
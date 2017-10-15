def file2mat(filename) :
    import numpy as np
    f=open(filename)
    mat=[]
    ans=[]
    for i in f.readlines() :
        curLine=i.split('\t')
        a = [float(x) for x in curLine[:-1]]
        mat.append(a)
        ans.append(int(curLine[-1]))
        nummat=np.array(mat)
        #returnMatrix=(nummat - nummat.min(0)) / (nummat.max(0) - nummat.min(0)) #normalization
    return nummat, ans

def norm (mat) :
    returnMatrix=(mat - mat.min(0)) / (mat.max(0) - mat.min(0)) #normalization
    return returnMatrix

import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import imp
imp.reload(kNN)

result={3: 'largeDoses', 2: 'smallDoses', 1: 'didntLike'}


mat, ans = file2mat('datingTestSet2.txt') #datatingTestset - label : texts, datingtestset2 - label : number
returnMat = norm(mat)


number=0
ratio=0.1
testNum = int(returnMat.shape[0] * ratio)
for i in range(testNum) : 
    classfyedResult=kNN.classfy0(returnMat[i, :], returnMat[testNum:, :], np.array(ans[testNum:]), 3)
    if classfyedResult != ans[i] : 
        number+=1
        print ('erroed number', i ,'   ',result[classfyedResult], '   ', result[ans[i]])
print('error rate is : ', number / testNum) 

### PLOT BY SCATTERING 

fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(mat[:,0], mat[:,1], 10*np.array(ans), 10*np.array(ans) )

fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(mat[:,0], mat[:,2], 10*np.array(ans), 10*np.array(ans))

 classfyedResult=kNN.classfy0_g(returnMat[1, :], returnMat[testNum:, :], np.array(ans[testNum:]), 3)
import re, math
import numpy as np

def clust(X, eps):
    key = 1
    clust = {key:[X[0]]}
    for i in range(len(X)-1):
        if (X[i+1] - X[i]) <= eps:
            clust[key].append(X[i+1])
        else:
            key += 1
            clust[key] = [X[i+1]]
    return clust

# file "data_temp.txt" contains only lines with middle frequencies, starting
# with ";CHIMERA..."
f = open("data_temp.txt", 'r')
StrF = f.read()
f.close()
StrF = StrF[1:]+';'
loopCounter = StrF.count(';')
for i in range(loopCounter):
    FrameParam = StrF[:StrF.index('[')]
    print(FrameParam)
    StrVal = StrF[StrF.index('[')+4:StrF.index(';')-3]
    ListVal = re.split('\ \]\ \[\ [0-9]+\ ', StrVal)
    StrF = StrF[StrF.index(';')+1:]
    ListVal = [float(i) for i in ListVal]
    ListValn = np.array(ListVal).reshape(-1,1)
    ListVal.sort()
    # TEMP
    std = np.std(ListVal)
    print('std: {}'.format(std))
    print('5%: {}'.format((ListVal[-1]-ListVal[0])*0.05))
    # END TEMP
    clustdict = clust(ListVal, eps=(ListVal[-1]-ListVal[0])*0.05)
    clustLimitDict = {i[0]:(min(i[1]), max(i[1]), i[1][len(i[1])//2]) for i in clustdict.items()}

    # Quantity elements in clusters:
    print('Number of clusters: {}'.format(max(clustLimitDict)))
    print('Number of elements in clusters: ', end = '')
    for i in clustdict.items():
        print('{0} : {1}'.format(i[0], len(i[1])), end=', ')
    print()
    # Medians:
    for i in clustLimitDict.items():
        print('Median of cluster {0}: {1}'.format(i[0], i[1][2]))
    print()
    print("============================")

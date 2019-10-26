import re, math
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from sklearn.cluster import OPTICS

# file "data_temp.txt" contains only lines with middle frequencies, starting with ";CHIMERA..."
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
    ListVal = list(set(ListVal))
    ListVal = np.array(ListVal).reshape(-1,1)
    
    print(len(ListVal))
    opt = OPTICS(min_samples=int(13*len(ListVal)/100))
    y_opt = opt.fit_predict(ListVal)
    count = Counter(y_opt)
    print(count)
    NClust = max(count.keys())+1
    print("{0} clusters".format(NClust))
    
    fig, ax = plt.subplots()
    # ax.plot(X_plot[:, 0], np.exp(log_dens), '-')
    ax.plot(ListVal[:, 0], -0.005 - 0.01 * np.random.random(ListVal.shape[0]), '+k')
    plt.show()


    # Quantity elements in clusters:
    '''
    count = Counter(y_km)
    print "Number of elements in clusters: ",
    for i in count:
        print count[i],
	print ' ',
    print("")
    # Medians:
    closest, _ = pdam(km.cluster_centers_, ListVal)
    for i, j in enumerate(closest):
        print("Median of cluster {0}: {1}".format(i+1, ListVal[j][0]))
    print("")
    print("============================")
    '''


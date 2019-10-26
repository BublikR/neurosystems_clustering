import re, math, pdb
import numpy as np
from collections import Counter
from sklearn.neighbors import KernelDensity
from matplotlib import pyplot as plt

def extrmin(l: list) -> list:
    '''Return list indexes minimums l'''
    list_min = []
    i = 1
    if len(extrmax(l)) == 1:
        list_min.extend([0, len(l)-1])
        return list_min
    if l[0] < l[1]:
        list_min.append(0)
    if l[0] == l[1]:
        i = 1
        k = i+1
        while k < len(l):
            if l[i] < l[k]:
                list_min.append(i+(k-i)//2)
                i = k
                break
            elif l[i] == l[k]:
                k += 1
            else:
                i = k
                break
    while i < len(l):
        if l[i] < l[i-1]:
            if i == len(l)-1 or l[i] < l[i+1]:
                list_min.append(i)
            elif l[i] == l[i+1]:
                j = i+1
                while j < len(l):
                    if l[i] == l[j]:
                        j += 1
                    elif l[i] > l[j]:
                        i = j-1
                        break
                    else:
                        list_min.append(i+(j-i)//2)
                        i = j-1
                        break
        i += 1
    return list_min

def extrmax(l: list) -> list:
    '''Return list indexes maximus l'''
    list_max = []
    if l[0] < l[1]:
        i = 1
    if len(set(l)) == 1:
        list_max.append(len(l)//2)
        return list_max
    if l[0] > l[1]:
        list_max.append(0)
        i = 1
    if l[0] == l[1]:
        i = 1
        k = i+1
        while k < len(l):
            if l[i] == l[k]:
                k +=1
            elif l[i] > l[k]:
                list_max.append(i+(k-i)//2)
                i = k
                break
            else:
                i = k
                break
    while i < len(l):
        if l[i] > l[i-1]:
            if i == len(l)-1 or l[i] > l[i+1]:
                list_max.append(i)
            elif l[i] == l[i+1]:
                j = i+1
                while j != len(l)-1:
                    if l[i] > l[j]:
                        list_max.append(i+(j-i)//2)
                        i = j-1
                        break
                    elif l[i] < l[j]:
                        i = j-1
                        break
                    else:
                        j += 1
        i += 1
    if list_max == []:
        list_max.append(len(l)//2)
    return list_max

def unionlist(sumlist: list, maxdict: dict) -> dict:
    new_dict = {}
    for i in sumlist:
        if len(i) == 1:
            new_dict[i[0]] = (maxdict[i[0]])
        else:
            temp = {np.exp(log_dens[k]):k for k in i}
            print('temp: {}'.format(temp))
            ctemp = temp.copy()
            maxtemp = max(temp)
            temp.pop(maxtemp)
            minlist = [maxdict[h] for h in i]
            mlist = []
            for y in minlist:
                mlist.extend(y)
            new_dict[ctemp[maxtemp]] = (min(mlist), max(mlist))
            if max(ctemp) > maxtemp*0.707:
                new_dict[ctemp[maxtemp]] = (min(mlist), max(mlist))
            else:
                if len(i)%2 == 0:
                    new_dict[min(i)+(max(i)-min(i))//2] = (min(mlist), max(mlist))
                else:
                    new_dict[i[len(i)//2]] = (min(mlist), max(mlist))
    return new_dict


# file "data_temp.txt" contains only lines with middle frequencies,
# starting with ";CHIMERA..."
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
    #ListVal = list(set(ListVal))
    ListVal.sort()
    maxListVal = max(ListVal)
    minListVal = min(ListVal)
    ListValNorm = [ (i - minListVal)/(maxListVal-minListVal) for i in ListVal ]
    print('ListValNorm length: {}'.format(len(ListValNorm)))
    print('ListValNorm STD: {}'.format(np.std(ListValNorm)))
    print('BW: {}'.format(np.std(ListValNorm, ddof=1)/math.sqrt(len(ListValNorm)))) #1.06*np.std(ListValNorm, ddof=1)*
    #        ((len(ListValNorm))**(-1/5))))
    ListValNorm = np.array(ListValNorm).reshape(-1,1)

    X_plot = np.linspace(min(ListValNorm), max(ListValNorm),
        2*len(ListValNorm))[:, np.newaxis]
    kde = KernelDensity(
        kernel='gaussian',
        bandwidth = 0.02
        #bandwidth=np.std(ListValNorm, ddof=1)/math.sqrt(len(ListValNorm))).fit(ListValNorm) #1.06*(np.std(ListValNorm, ddof=1))*
        #    ((len(ListValNorm))**(-1/5))).fit(ListValNorm)
        ).fit(ListValNorm)
    log_dens = kde.score_samples(X_plot)

    # indexes max and min l
    lmaxi = extrmax(np.exp(log_dens))
    print(lmaxi)
    #print(len(lmaxi))
    lmini = extrmin(np.exp(log_dens))
    print(lmini)
    #print(len(lmini))

    # indexes max and min LV
    LVmaxi = [i//2 for i in lmaxi]
    #print(LVmaxi)
    #print(len(LVmaxi))
    LVmini = [i//2 for i in lmini]
    #print(LVmini)
    #print(len(LVmini))

    # 5% values
    ldmaxv = [np.exp(log_dens[i]) for i in lmaxi]
    ldminv = [np.exp(log_dens[i]) for i in lmini]
    #p = math.sqrt((max(ldmaxv)-min(ldminv))**2) * 0.95
    #proc = min(ldminv) + p
    proc = max(ldmaxv)*0.05#*len(ListVal)/2000
    '''    
    fig, ax = plt.subplots()
    ax.plot([X_plot[:, 0][0], X_plot[:, 0][-1]], [proc, proc], '-')
    ax.plot(X_plot[:, 0], np.exp(log_dens), '-')
    #ax.plot(ListValNorm[:, 0], np.random.random(ListValNorm.shape[0]), 'k.')
    plt.show()
    '''
    lmaxd = { lmaxi[i]:j for i, j in enumerate(ldmaxv) if j >= proc }
    lmaxmind = {}
    if lmini[0] > lmaxi[0] and min(lmaxd.keys()) == lmaxi[0]:
        l = None
        r = lmini[0]
        lmaxmind[lmaxi[0]] = (l,r)
    if lmini[0] > lmaxi[0] and max(lmaxd.keys()) == lmaxi[-1]:
        l = lmini[-1]
        r = None
        lmaxmind[lmaxi[-1]] = (l,r)
    for j in lmaxd.keys():
        index = lmaxi.index(j)
        if lmini[0] < lmaxi[0]:
            l = lmini[index]
            r = None if (index+1 >= len(lmini)) else lmini[index+1]
        else:
            l = lmini[index-1] if (index != 0) else None
            if index > len(lmini)-1:
                r = None
            else:
                r = lmini[index]
        lmaxmind[j] = (l,r)    
    print('lmaxmind: {}'.format(lmaxmind))
    #print(len(lmaxmind))
    
    '''  
    sumlist = [ d[0] for d in lmaxmind.items() if (np.exp(log_dens[d[1][0]]) if d[1][0] != None else proc-1) >= np.exp(log_dens[d[0]])*0.707 or (np.exp(log_dens[d[1][1]]) if d[1][1] != None else proc-1) >= np.exp(log_dens[d[0]])*0.707 ]
    '''
    # new sumlist:
    
    sumlist = []
    templist = []
    tempdict = [[i,j] for i,j in lmaxmind.items()]
    sortdict = sorted(tempdict, key=lambda el: el[0])
    valuesortdictmax = [np.exp(log_dens[i[0]]) for i in sortdict]
    print(max(valuesortdictmax)*0.707)
    valuesortdictmin = []
    [valuesortdictmin.extend(list(i[1])) for i in sortdict]
    valuesortdictmin = list(set(valuesortdictmin[1:-1]))
    valuesortdictmin = [np.exp(log_dens[i]) for i in valuesortdictmin]
    print('sortdict: {}'.format(sortdict))
    if len(valuesortdictmax) > 1 and max(valuesortdictmax)*0.707 < min(valuesortdictmin):
        sumlist.append([ i[0] for i in sortdict ])
    else:
        for d in sortdict:
            templist.append(d[0])
            if (True if d[1][0] == None else np.exp(log_dens[d[1][0]])) < np.exp(log_dens[d[0]])*0.707 and (True if d[1][1] == None else np.exp(log_dens[d[1][1]])) < np.exp(log_dens[d[0]])*0.707:
                if len(templist) > 1:
                    if (True if lmaxmind[templist[-2]][0] == None else np.exp(log_dens[lmaxmind[templist[-2]][0]])) < np.exp(log_dens[templist[-2]])*0.707 and (True if lmaxmind[templist[-2]][1] == None else np.exp(log_dens[lmaxmind[templist[-2]][1]])) < np.exp(log_dens[templist[-2]])*0.707:
                        sumlist.append(templist[:-1])
                        templist = templist[-1:]
                    else:
                        if np.exp(log_dens[lmaxmind[templist[-2]][0]]) < np.exp(log_dens[lmaxmind[templist[-2]][1]]):
                            sumlist.append(templist[:-2])
                            templist = templist[-2:]
                        else:
                            sumlist.append(templist[:-1])
                            templist = templist[-1:]
            elif np.exp(log_dens[d[0] if d[1][0] == None else d[1][0]]) < np.exp(log_dens[d[0] if d[1][1] == None else d[1][1]]):
                if len(templist) > 1 and np.exp(log_dens[lmaxmind[templist[-2]][0]]) > np.exp(log_dens[lmaxmind[templist[-2]][1]]):
                    sumlist.append(templist[:-1])
                    templist = templist[-1:]
            if templist[-1] == sortdict[-1][0]:
                sumlist.append(templist)

    new_sumlist = []
    for y in sumlist:
        if y != []:
            new_sumlist.append(y)
    print('sumlist: {}'.format(new_sumlist))         
    clustdict = unionlist(new_sumlist, lmaxmind)
    
    if len(clustdict) == len(ListValNorm):
        clustdict = {len(X_plot)//2:(0,len(X_plot)-1)}
    print(clustdict)
    print(len(clustdict))


    
    fig, ax = plt.subplots()
    ax.plot(X_plot[:, 0], np.exp(log_dens), '-')
    ax.plot([X_plot[:, 0][0], X_plot[:, 0][-1]], [proc, proc], '-')
    Temp = list(clustdict.keys())
    Temp.sort()
    X_point = [ X_plot[i][0] for i in Temp ]
    Y_point = [ np.exp(log_dens[i]) for i in Temp ]
    ax.scatter(X_point, Y_point, marker='o', color='red')
    ax.plot(ListValNorm[:, 0], 0.005*np.random.random(ListValNorm.shape[0]), 'k.')
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
    closest, _ = pdam(km.cluster_centers_, ListValNorm)
    for i, j in enumerate(closest):
        print("Median of cluster {0}: {1}".format(i+1, ListValNorm[j][0]))
    print("")
    print("============================")
    '''


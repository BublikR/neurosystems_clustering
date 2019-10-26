# Master's degree work 
Title of the degree work: "Automated classification of massive neurosystems modeling results."
Taras Shevchenko National University of Kyiv, Faculty of Radio Physics, Electronics and Computer Systems, 2019.

## Abstract
Chimera states revealed in the simulation of neural systems are an interesting object of study. With massive modeling, there is a need to automate the analysis of obtained results. We investigated a network of three-dimensional identical oscillators constructed according to the Kuramoto-Sakaguchi model, which is used for description synchronization phenomena in neural systems. The simulation results are different structures of synchronized, unsynchronized and chimera states. In present paper we applied various clustering and classification algorithms for automatic classification of spatial shapes of coherence and incoherence regions. The developed clustering model allows you to automate the classification of massive modeling results.

## Numerical simulation
Numerical simulation was based on the Runge–Kutta solver DOPRI5 that has been integrated into software for large nonlinear dynamical networks [2], allowing for parallelized simulations with different sets of parameters and initial conditions. The simulations and clustering were performed on a computer cluster [“Chimera”](http://nll.biomed.kiev.ua/cluster) and Ukrainian Grid Infrastructure providing distributed cluster resources and the parallel software [3].

## Clustering
### Clustering the chimera states descriptors
Clustering was applied to the descriptors of the obtained simulation results, as parameters uniquely characterizing the model. The descriptors are the set of spatial integrals of shape’s 3D Fourier spectrum sorted in ascending order. A total of 4618 descriptors were analyzed. The k-means method and agglomerative hierarchical clustering with three different measures for estimating the distance between clusters were used. 
The k-means method required a preliminary determination of the optimal number of clusters. To solve this problem, the “elbow” method was applied, which, based on the dependence of the sum of the intra-cluster distance of the cluster points to the cluster center on the number of clusters, gives such an estimate [4]. According to the graph of this dependence (Fig. 1) the optimal number of clusters (3) was found. Three clusters with 343, 509 and 3766 elements were obtained. When performing agglomerative clustering, hierarchical trees were constructed using three different clustering measures – complete (Fig. 2), average (Fig. 3), ward (Fig. 4) [5].

* Fig. 1. The optimal number of clusters by “Elbow” method:
![The optimal number of clusters by “Elbow” method](/img/elbow.png)
* Fig. 2. Hierarchical clustering using “Complete” measure:
![Fig. 2. Hierarchical clustering using “Complete” measure](/img/Complete.png)
* Fig. 3. Hierarchical clustering using “Average” measure:
![Fig. 3. Hierarchical clustering using “Average” measure](/img/Average.png)
* Fig. 4. Hierarchical clustering using “Ward” measure:
![Fig. 4. Hierarchical clustering using “Ward” measure](/img/Ward.png)

Clustering using the method of constructing hierarchical trees gave the same result as the k-means method, with the same order of the number of elements in the clusters (347, 472 and 3799 for "complete"; 345, 345 and 3928 for "average"; 347, 966 and 3305 for "ward") and typical representatives of each cluster as medians of these clusters (Fig. 5).
After analyzing the obtained results, one can see that chimera states are mostly found in the first cluster (Fig.5 b), chaotic states are almost in the second cluster (Fig.5c), and synchronized states are almost in the third cluster (Fig.5a).

Fig. 5. Median cluster elements in average frequency space a) – synchronized, b) spiral chimera state, c) chaotic state.:
![Median cluster elements](/img/Median.png)

* Сomparison of all results:
![Comparison of all results](/img/comparison_of_results.png)

After analyzing the obtained results, one can see that it was chimeric states that were in the first cluster, the second was mostly chaos, and the third were synchronized states.

### Frequency clusters in Kuramoto-Skaguchi model with inertia – global coupling
In addition, the clustering of the average frequencies of two-dimensional states with a global coupling was carried out.
Clustering results were presented at School and Workshop on Patterns of Synchrony: Chimera States and Beyond in Trieste (Italy) in May 2019.
* The results of two-dimensional clustering states with a global coupling:
![states_with_a_global_coupling](/img/states_with_a_global_coupling.png)

## References
    1. Kuramoto Y and Battogtokh D 2002 Coexistence of coherence and incoherence in nonlocally coupled phase oscillators Nonlinear Phenom. Complex Syst. 5 380–5
    2. Yuriy Maistrenko, Oleksandr Sudakov, Oleksiy Osiv, Volodymyr Maistrenko .Chimera States in Three-Dimensions. New Journal of Physics, vol. 17, 073037 (2015)
    3. Salnikov A, Levchenko R and Sudakov O 2011 Integrated grid environment for massive distributed computing in neuroscience Proc. 6th IEEE Workshop IDAACS’2011 pp 198–202
    4. Zynovyev M, Svistunov M, Sudakov O and Boyko Yu 2007 Ukrainian grid infrastructure practical experience Proc. 4th IEEE Workshop IDAACS 2007 (Dortmund, Germany, 6–8 September 2007) pp 165–9
    5. Milligan G.W. and Cooper M.C. An examination of procedures for determining the number of clusters in a data set, Psychometrika, 1985, 50, 159-179p
    6. Fernández, Alberto; Gómez, Sergio (2008). "Solving Non-uniqueness in Agglomerative Hierarchical Clustering Using Multidendrograms". Journal of Classification. 25 (1): 43–65

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:19:47 2019

@author: Ashlin
"""
import numpy as np
from itertools import combinations, permutations

#function to calculate kendall tau distance based on KCC
def kendalltau_distance(rank_a, rank_b):
    tau = 0
    n_candidates = len(rank_a)
    for i, j in combinations(range(n_candidates), 2):
        tau += (np.sign(rank_a[i] - rank_a[j]) ==
                -np.sign(rank_b[i] - rank_b[j]))
    return tau


activity_options="Top_Golf Miniature_Golf Bowling".split()
ranks=np.array([[1,2,3],
               [2,3,1],
               [3,2,1],
               [3,2,1],
               [3,2,1],
               [3,2,1]])
    
# Performing Kemeny Aggregation

def rank_aggregation(ranks):
    min_dist=np.inf
    best_rank=None
    voters,activity_options=ranks.shape
    for activity_rank in permutations(range(activity_options)):
        
            dist = np.sum(kendalltau_distance(activity_rank, rank) for rank in ranks)
            if dist < min_dist:
             min_dist = dist
             best_rank = activity_rank
    return min_dist, best_rank
dist, aggr = rank_aggregation(ranks)
print("A Kemeny-Young aggregation with score {} is: {}".format(
    dist,
    ", ".join(activity_options[i] for i in np.argsort(aggr))))
    


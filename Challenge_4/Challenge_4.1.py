#!/usr/bin/env python
# coding: utf-8

# Question is a maximum flow problem with multiple source miltiple sinks
# The method used to solve the question is Ford–Fulkerson algorithm with a depth-first search on residual network

# References: 
# https://vitaminac.github.io/Google-Foobar-Escape-Pods/
# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
# http://www.cs.ust.hk/mjg_lib/Classes/COMP572_Fall07/Notes/Max_Flow.pdf
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
import math

# Transform matrix into a supersource and a supersink maximum flow problem
def transform(path, en, ex):
    output=[]
    for row in range(len(path)+2):
        temp=[]
        for col in range(len(path)+2):
            if col==0:
                temp.append(0)
            elif row==0:
                if col-1 in en:
                    temp.append(math.inf) # Using float('inf') for Python2
                else: temp.append(0) 
            elif row!=len(path)+1:
                if col!=len(path)+1: temp.append(path[row-1][col-1])
                elif col==len(path)+1 and row-1 not in ex: temp.append(0)
                elif col==len(path)+1 and row-1 in ex: temp.append(math.inf)
            elif row==len(path)+1:
                temp.append(0) 
        output.append(temp)
    return output

# Calculate the residual network: cf=capacity-flow
def residual_cap(path, f):
    cf=[]
    for idx, i in enumerate(path):
        temp=[]
        for jdx, j in enumerate(i):
            temp.append(j-f[idx][jdx])
        cf.append(temp)
    return cf

# DFS search for path p from supersource s to supersink t
def dFS_path(cf):
    S=[]
    visited=[] #Record the visited node during DFS
    output=[]
    tree={} #Dictionary to store the tree (key:searched node, value:parent node)
    S.append(0)

    # DFS algorithm
    while S !=[]:
        search=S.pop()
        # Stopping criteria (when reaching supersink t)
        if search==len(cf)-1:
            visited.append(search)
            output.append(search)
            # Extract path by searching parent nodes in tree dict, starting on last visited node 
            for node in reversed(visited):
                output.append(tree[node]) 
                if tree[node]==0: break
            return list(reversed(output))
        
        if search not in visited:
            visited.append(search)
            for idx, e in enumerate(cf[search]):
                if e!=0 and idx not in visited:
                    S.append(idx)
                    tree[idx]=search
    return [0]

# Calculate the minimum capacity within the path
def cf_min(cf, visited):
    path_cf=[]
    if visited==[]:
        return 0
    for i in range(len(visited)-1):
        path_cf.append(cf[visited[i]][visited[i+1]])
    return min(path_cf)

# Update the flow
def update_f(f, cf_min, visited):
    for node in range(len(visited)-1):
        i, j=visited[node], visited[node+1]
        f[i][j]+=cf_min
        f[j][i]-=cf_min
    return f

# Main program
def solution(en,ex,path):
    max_f=0
    transform_path=transform(path, en, ex)
    f=[[0 for _ in range(len(transform_path))] for _ in range(len(transform_path))]

    while True:
        cf = residual_cap(transform_path, f)
        visited=dFS_path(cf)
        if visited==[0]: break
        capacity=cf_min(cf ,visited)
        max_f+=capacity
        update_f(f, capacity, visited)
        
    return max_f


path=[[0, 0, 4, 6, 0, 0], 
      [0, 0, 5, 2, 0, 0], 
      [0, 0, 0, 0, 4, 4], 
      [0, 0, 0, 0, 6, 6], 
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0]]
ex=[4,5]
en= [0,1]
solution(en,ex,path)


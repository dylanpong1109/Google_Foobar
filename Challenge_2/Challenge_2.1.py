#!/usr/bin/env python
# coding: utf-8

# Question is equivalent to finding parent nodes of binary tree with postorder traversal
# Reference: https://www.geeksforgeeks.org/find-parent-of-given-node-in-a-binary-tree-with-given-postorder-traversal/?ref=lbp
def solution(h, q):
    def total_node(h):
        num=0
        for n in range(h):
            num += 2**n
        return num

    def find_parent(end, target, start=1, top_node=True):        
        # Return -1 if it is a top node
        if target==end and top_node:
            return -1
        
        # Use binary search to locate target node
        if target < (start+end)/2:
            if target == (start+end)/2-1:
                return end
            end=int((start+end)/2-1)
            return find_parent(end, target, start, top_node=False)
        else:
            if target == end-1:
                return end
            start = int((start+end)/2)
            end = end-1
            return find_parent(end, target, start, top_node=False)
    
    def find_multi_targets(total, targets):
        for i in targets:
            yield find_parent(total,i) 
    
    total = total_node(h)
    return list(find_multi_targets(total, q))

solution(5, [19, 14, 28])




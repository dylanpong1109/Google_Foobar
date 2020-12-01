#!/usr/bin/env python
# coding: utf-8

# Solution: Calculate the difference between sum of geometric sequence and sum of fibonacci sequence
def solution(s):
    import math
    def generous(s):
        # Sum of 1+2+4+8+....+2**(n-1)=(1-2**n)/(1-2)=2**n-1
        return int(math.log(s+1,2))
    def stingy(s):
        F=[1,1]
        i=0
        # Sum of 1+1+2+3+5+....+F[n]=F[n+2]-1
        while F[i]-1<=s:
            F.append(F[i]+F[i+1])
            i+=1
        return i-2
    return stingy(s)-generous(s)


solution(100000000)


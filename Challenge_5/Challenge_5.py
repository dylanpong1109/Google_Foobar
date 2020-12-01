#!/usr/bin/env python
# coding: utf-8

## Question is equivalent of asking the sum of Beatty sequence with square root 2
## Reference
## https://en.wikipedia.org/wiki/Beatty_sequence#Rayleigh_theorem
## https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

from decimal import Decimal, getcontext
getcontext().prec = 101
def solution(n):
    n=int(n) # long() for Python2
    def sum_sequence(n):
        if n==0:
            return 0
        n1 = long((Decimal(2).sqrt()-1)*n) # long() for Python2
        output=n*n1 + n*(n+1)/2 - n1*(n1+1)/2 - sum_sequence(n1)
        return output
        
    output=sum_sequence(n)
    
    return str(output)
    
    
solution('5')


#!/usr/bin/env python
# coding: utf-8

# Check whether two numbers are co-prime, then calculate the number of reduction steps
def bomb(x,y):
    l=max(int(x),int(y))
    s=min(int(x),int(y))
    # If two numbers have common factors, it's impossible to make the bomb
    # If two numbers are co_prime, the fewest number of generation will be the number of division we made during reduction
    # E.g. (4,7) -> (4,3) -> (1,3) -> (1,2) -> (1,1) = 7//4 + 4//3 + 3//1 - 1 = 4 generations needed
    counter=0
    while True:
        if s==1: return str(counter+l-1)
        if s==0: return 'impossible'
        counter+=l//s
        l,s = s,l%s


bomb('4','7')






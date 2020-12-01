#!/usr/bin/env python
# coding: utf-8

# Generate list of prime number
def solution(i):
    string_id='2'
    loop_id=int(string_id)
    prime_list=[int(string_id)]
    while len(string_id)<10005:
        prime=True
        loop_id+=1
        for n in prime_list:
            if loop_id % n == 0:
                break
        else:
            prime_list.append(loop_id)
            string_id+=str(loop_id)
    return string_id[i:i+5]    # Your code here


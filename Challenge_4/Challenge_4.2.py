#!/usr/bin/env python
# coding: utf-8

# Solution: Calculate the mirrored position of target and source, find the mirrored distance from the actual source and record hit if distance < input distance 
# Reference:
# https://peter-ak.github.io/2020/05/10/Brining_a_gun_to_a_guard_fight.html
# https://stackoverflow.com/questions/42792375/google-foobar-bringing-a-gun-to-a-guard-fight

import math

# Construct the mirrored location from original position 
def mirror_point(pos, dim, dist):
    mirror_list=[]
    for axis in range(2):
        point=[]
        ceil=int(math.ceil(dist / dim[axis]))
        for idx in range(ceil+1):            
            if idx == 0:
                point.append(pos[axis])
                point.append(-pos[axis])
            else:
                for sign in [(1, 1), (1, -1), (0, 1), (0, -1)]:
                    point.append((-1) ** sign[0] * 2 * dim[axis] * (idx) + sign[1]*pos[axis])
        mirror_list.append(point)
    return mirror_list

# Record distances and angles from mirrored position to source position
def record_angle(pos_list, pos0):
    angle_dict={}
    for x in pos_list[0]:
        for y in pos_list[1]:
            if (x,y)!=(pos0[0],pos0[1]):
                p_angle=math.atan2(x-pos0[0],y-pos0[1])
                p_dist=math.sqrt((x-pos0[0])**2+(y-pos0[1])**2)
                if p_angle not in angle_dict:
                    angle_dict[p_angle]=p_dist
                elif p_dist<angle_dict[p_angle]:
                    angle_dict[p_angle]=p_dist
    return angle_dict
            
def solution(dim, pos0, pos1, dist):
    counter=0
    # Generate mirrored position list for target and source
    target_mirror=mirror_point(pos1, dim, dist)
    source_mirror=mirror_point(pos0, dim, dist)
    # Record distances and angles from mirrored source to real source
    angle_dict=record_angle(source_mirror, pos0)

    

    for x in target_mirror[0]:
        for y in target_mirror[1]:    
            target_angle=math.atan2(x-pos0[0],y-pos0[1])
            target_dist=math.sqrt((x-pos0[0])**2+(y-pos0[1])**2) 
            if target_dist<=dist:
                # Case1: Angles from mirrored targets to actual source is unique (not the same angle from mirrored source to actual source) 
                if target_angle not in angle_dict:
                    # set distance into zero -> no other mirrored target with the same angle can be hitted
                    # (the laser can only hit each unique angle once and disappear)
                    angle_dict[target_angle]=0 
                    counter+=1
                # Case2: Angles from mirrored targets to actual source are the same as the angle from mirrored source to actual source, 
                # record hit if distance from mirrored targets to actual source is shorter than distance from mirrored source to actual source 
                # (otherwise the source will block the target, the laser will hit the source first)
                elif angle_dict[target_angle]>target_dist:
                    angle_dict[target_angle]=0
                    counter+=1
    return counter            


solution([2,5], [1,2], [1,4], 11)



#Finds the "Hourglass" shape with
#The highest sum within a 6x6 array

import math
import sys
data = sys.stdin.readlines()

def reader(data):
    lines = [i.split() for i in data]
    nums = []
    for line in lines:
        nums.append([int(x) for x in line])
    return nums

def Hg_Sum(nums,left,top):
    slice_1 = sum(nums[top][left:left+3])
    slice_2 = nums[top+1][left+1]
    slice_3 = sum(nums[top+2][left:left+3])
    sums = slice_1+slice_2+slice_3
    return sums

def line_max(nums,line):
    for i in range(4):
        if i == 0:
            max = Hg_Sum(nums,i,line)
        else:
            val = Hg_Sum(nums,i,line)
            if val > max:
                max = val
    return max

def hourglassMax(data):
    nums = reader(data)
    for i in range(4):
        if i == 0:
            max = line_max(nums,i)
        else:
            val = line_max(nums,i)
            if val > max:
                max = val
    return max

val = hourglassMax(data)
print(val)

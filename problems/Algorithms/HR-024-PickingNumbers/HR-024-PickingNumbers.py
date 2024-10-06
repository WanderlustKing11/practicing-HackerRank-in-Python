# HackerRank - Algorithms
# Picking Numbers
# By Douglas Horville

# Given an array of integers, find the longest subarray where the 
# absolute difference between any two elements is less than or equal to 1.

# pickingNumbers has the following parameter(s):
# int a[n]: an array of integers

# Returns:
# int: the length of the longest subarray that meets the criterion



###############################################################
###########  Solve  ###########

import os

def pickingNumbers(a):
  max_length = 0
  ints_dict = {}
  for i in a:
    if i in ints_dict:
      ints_dict[i] += 1
    else:
      ints_dict[i] = 1
  print(ints_dict)

  for num in ints_dict.keys():
    if not ints_dict:
      return 0
    if ints_dict[num] > max_length:
      max_length = ints_dict[num]
    
    if num + 1 in ints_dict:
      if ints_dict[num] + ints_dict[num + 1] > max_length:
        max_length = ints_dict[num] + ints_dict[num + 1]
  return max_length

###############################################################
###########  Main ###########

def main():
  print(pickingNumbers([]))
  print(pickingNumbers([1]))
  print(pickingNumbers([1,1,2,2,4,4,5,5,5]))
  print(pickingNumbers([4,6,5,3,3,1]))


main()
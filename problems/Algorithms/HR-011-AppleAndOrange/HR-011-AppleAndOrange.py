# HackerRank - Alogrithms
# Apple And Orange
# By Douglas Horville

# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
# Using the information given below, determine the number of apples and oranges that 
# land on Sam's house.

# In the diagram below:
# The red region denotes the house, where s is the start point, and t is the endpoint. 
# The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point a, 
# and the orange tree is at point b.
# When a fruit falls from its tree, it lands d units of distance from its tree of 
# origin along the x-axis.
# ** A negative value of d means the fruit fell d units to the tree's left, and a 
# positive value of d means it falls d units to the tree's right. **

# Given the value of d for m apples and n oranges, determine how many apples and oranges 
# will fall on Sam's house (i.e., in the inclusive range [s,t])?

# Complete the countApplesAndOranges function in the editor below. 
# It should print the number of apples and oranges that land on Sam's house, each on a separate line.

# countApplesAndOranges has the following parameter(s):

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.


#############################################################################
###########  Solution  ###########
import os

def countApplesAndOranges(s, t, a, b, apples, oranges):
  apple_count = 0
  # Loop through apples
  for apple in apples:
    # Add apples distance to a (tree position)
  # a + apples[i] -> [a1, a2, a3...]
    ad = a + apple  # ad is the apple distance from a (tree)
  # Count how many apples[i] are in between s & t (inclusive)
    if ad >= s and ad <= t:
      apple_count += 1

  orange_count = 0
  # Loop through oranges
  for orange in oranges:
  # add oranges distance to b (tree position)
  # b + oranges[i] -> [o1, o2, o3...]
    od = b + orange  # od is the orange distance from b (tree)
  # Count how many oranges[i] are in between s & t (inclusive)
    if od >= s and od <= t:
      orange_count += 1
  print(apple_count)
  print(orange_count)


#############################################################################
###########  Main  ###########

def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'A-011-input.txt')

  outFile = open(input_file_path, 'r')
  content = outFile.readlines()
  outFile.close()

  # First line: s and t
  first_multiple_input = content[0].rstrip().split()
  s = int(first_multiple_input[0])
  t = int(first_multiple_input[1])

  # Second line: a and b
  second_multiple_input = content[1].rstrip().split()
  a = int(second_multiple_input[0])
  b = int(second_multiple_input[1])

  # Third line: m and n
  third_multiple_input = content[2].rstrip().split()
  m = int(third_multiple_input[0])
  n = int(third_multiple_input[1])

  # Fourth line: distances of apples
  apples = list(map(int, content[3].rstrip().split()))

  # Fifth line: distances of oranges
  oranges = list(map(int, content[4].rstrip().split()))

  countApplesAndOranges(s, t, a, b, apples, oranges)



main()
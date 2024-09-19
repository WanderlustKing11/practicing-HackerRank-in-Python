# HackerRank - Algorithms
# Counting Valleys
# By Douglas Horville

# An avid hiker keeps meticulous records of their hikes. During the last hike that 
# took exactly steps steps, for every step it was noted if it was an uphill, U, or 
# a downhill, D step. Hikes always start and end at sea level, and each step up or 
# down represents a 1 unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a 
# step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step 
# down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the 
# number of valleys walked through.

# countingValleys has the following parameter(s):
# int steps: the number of steps on the hike
# string path: a string describing the path

# Returns:
# int: the number of valleys traversed

# Input Format consists of 2 lines:
# The first line contains an integer steps, the number of steps in the hike.
# The second line contains a single string path, of steps characters that describe the path.

###############################################################
###########  Solve  ###########

import os

def countingValleys(steps, path):
  num_of_valleys = 0
  stack = []
  sea_level = 0

  for step in path:
    if step == 'D':
      sea_level -= 1
    elif step == 'U':
      sea_level += 1
    
    if sea_level > 0:
      pass
    elif sea_level < 0: # or (sea_level == 0 and step == 'D'):
      stack.append(step)
    elif sea_level == 0 and len(stack) > 0:
      num_of_valleys += 1
      for x in range(len(stack)):
        stack.pop()
    print(f'Stack = {stack}, sea_level = {sea_level}, num_of_Valleys = {num_of_valleys}')
    return num_of_valleys


###############################################################
###########  Main ###########


def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'A-021-input.txt')

  with open(input_file_path, 'r') as inputFile:
    content = inputFile.read().strip()
    test_cases = content.split('\n\n')

    results = []
    for case in test_cases:
      lines = case.split('\n')
      steps = int(lines[0].strip())
      path = str(lines[1].strip())
      if steps != len(path):
        print("Error: Given 'Path' length doesn't match given input 'Steps'")
      else:
        print(countingValleys(steps, path))

if __name__ == '__main__':
  main()
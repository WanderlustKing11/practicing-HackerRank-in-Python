# HackerRank - Algorithms
# Migratory Birds
# By Douglas Horville

# Given an array of bird sightings where every element represents a 
# bird type id, determine the id of the most frequently sighted type. 
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# migratoryBirds has the following parameter(s):
# int arr[n]: the types of birds sighted

# Return int: the lowest type id of the most frequently sighted birds

###############################################################
###########  Solve  ###########

import os

def migratoryBirds(arr):
  birds = {}
  matching_max_values = []
  for bird_id in arr:
    if bird_id in birds:
      birds[bird_id] += 1
    else:
      birds[bird_id] = 1
  maxBirds = max(zip(birds.values(), birds.keys()))[1]
  for i in birds:
    if birds[i] == birds[maxBirds]:
      matching_max_values.append(i)
  matching_max_values.sort()
  print('Bird sightings:', arr)
  print('Bird log:', birds)
  print('Most frequent lowest type id bird:', matching_max_values[0])
  return matching_max_values[0]

  # print('Arr of birds:', arr)
  # print('Amount of birds:', birds)
  # print('Max birds:', maxBirds)


###############################################################
###########  Main ###########

def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'A-017-input.txt')

  with open(input_file_path, 'r') as inputFile:
    content = inputFile.read().strip()
    test_cases = content.split('\n\n')

    results = []
    for case in test_cases:
      lines = case.split('\n')
      n = int(lines[0].strip())
      ar = list(map(int, lines[1].strip().split()))
      if n != len(ar):
        print("Error: Given input length doesn't match given input list")
      else:
        print(migratoryBirds(ar))

if __name__ == '__main__':
  main()

# HackerRank - Algorithms
# Sales By Match
# By Douglas Horville

# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.

# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock

# Returns int: the number of pairs

###############################################################
###########  Solve  ###########

import os

def sockMerchant(n, ar):
  socks = {}
  sock_pairs = 0
  for i in ar:
    if i in socks:
      socks[i] += 1
    else:
      socks[i] = 1

  for x in socks:
    if socks[x] % 2 == 0:
      sock_pairs += socks[x] / 2
    else:
      socks[x] -= 1
      sock_pairs += socks[x] / 2
  return int(sock_pairs)

###############################################################
###########  Main ###########

def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'A-019-input.txt')

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
        print(sockMerchant(n, ar))

if __name__ == '__main__':
  main()

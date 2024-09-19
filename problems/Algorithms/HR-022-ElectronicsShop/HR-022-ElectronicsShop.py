# HackerRank - Algorithms
# Electronics Shop
# By Douglas Horville

# A person wants to determine the most expensive computer keyboard and USB drive that can be 
# purchased with a given budget. Given the price lists for keyboards and USB drives and a budget, 
# find the cost to buy them. If it is not possible to buy both items, return -1.

# getMoneySpent has the following parameter(s):
# int keyboards[n]: the keyboard prices
# int drives[m]: the drive prices
# int b: the budget

# Returns:
# int: the maximum that can be spent, or  if it is not possible to buy both items

###############################################################
###########  Solve  ###########

import os

def getMoneySpent(keyboards, drives, b):
  # Initialize max_cost to -1, to return if no valid combination exists
  max_cost = -1
  

  # Iterate through each keyboard price
  for k_price in keyboards:
    # Iterate through each drive price
    for d_price in drives:
      cost = k_price + d_price
      # If the total cost is withihn the budget and higher than the current max_cost:
      if cost <= b and cost > max_cost:
        max_cost = cost
  
  return max_cost



###############################################################
###########  Main ###########


def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  intput_file_path = os.path.join(script_dir, 'test', 'A-022-input.txt')

  with open(intput_file_path, 'r') as inputFile:
    content = inputFile.read().strip()
    test_cases = content.split('\n\n')

    results = []
    for case in test_cases:
      lines = case.split('\n')
    
      list1 = lines[0].split(' ')
      quantity = [int(i) for i in list1]
      b = quantity[0]
      n = quantity[1]
      m = quantity[2]

      list2 = lines[1].split(' ')
      keyboards = [int(j) for j in list2]

      list3 = lines[2].split(' ')
      drives = [int(k) for k in list3]

      # print(f'quantity = {b}, {n}, {m}; keyboards = {keyboards}; drives = {drives}')

      if n != len(keyboards):
        print("Given 'n' does not match number of 'keyboards'")
      elif m != len(drives):
        print("Given 'm' does not match number of 'drives'")
      else:
        print(getMoneySpent(keyboards, drives, b))



if __name__ == '__main__':
  main()
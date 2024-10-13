# HackerRank - Algorithms
# Utopian Tree
# By Douglas Horville

# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it 
# doubles in height. Each summer, its height increases by 1 meter.
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. 
# How tall will the tree be after n growth cycles?

# utopianTree has the following parameter(s):
# int n: the number of growth cycles to simulate

# Returns int: the height of the tree after the given number of cycles

###############################################################
###########  Solve  ###########

def utopianTree(n):
  if n == 0:
    return 1
  
  i = 1
  height = 1
  while i <= n:
    if i % 2 == 0:
      height += 1
    else:
      height *= 2
    i += 1
  return height
    
      


###############################################################
###########  Main ###########

def main():
  print(utopianTree(1))
  print(utopianTree(2))
  print(utopianTree(3))
  print(utopianTree(4))
  print(utopianTree(5))
  print(utopianTree(6))
  print(utopianTree(7))
  print(utopianTree(8))
  print(utopianTree(9))

main()

# Std In is not complete. Will update input file and main function soon
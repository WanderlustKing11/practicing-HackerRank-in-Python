# HackerRank - Algorithms
# Cats and a Mouse
# By Douglas Horville

# Two cats and a mouse are at various positions on a line. You will be given 
# their starting positions. Your task is to determine which cat will reach the 
# mouse first, assuming the mouse does not move and the cats travel at equal speed. 
# If the cats arrive at the same time, the mouse will be allowed to move and it 
# will escape while they fight.

# You are given q queries in the form of x, y, and z representing the respective 
# positions for cats A and B, and for mouse C. Complete the function to return the 
# appropriate answer to each query, which will be printed on a new line.
# - If cat A catches the mouse first, print Cat A.
# - If cat B catches the mouse first, print Cat B.
# - If both cats reach the mouse at the same time, print Mouse C as the two cats 
#   fight and mouse escapes.

# catAndMouse has the following parameter(s):
# int x: Cat 's position
# int y: Cat 's position
# int z: Mouse 's position

# Returns:
# string: Either 'Cat A', 'Cat B', or 'Mouse C'


###############################################################
###########  Solve  ###########

import os

def catAndMouse(x, y, z):
  cat_A = abs(x - z)
  cat_B = abs(y - z)
  if cat_A < cat_B:
    return "Cat A"
  elif cat_B < cat_A:
    return "Cat B"
  else:
    return "Mouse C"



###############################################################
###########  Main ###########


def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'A-023-input.txt')

  with open(input_file_path, 'r') as inputFile:
    content = inputFile.read().strip()
    lines = content.splitlines()

    # First line contains the number of test cases
    t = int(lines[0])
    index = 1  # Start from the second line
    for _ in range(t):
      # Get x, y and z
      x, y, z = (int(num) for num in lines[index].split())
      print(f'test case #{index}: {x, y, z}')
      print(catAndMouse(x, y, z))
      index += 1



if __name__ == '__main__':
  main()
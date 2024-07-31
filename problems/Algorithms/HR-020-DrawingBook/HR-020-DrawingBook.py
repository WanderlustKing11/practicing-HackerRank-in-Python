# HackerRank - Algorithms
# Drawing Book
# By Douglas Horville

# A teacher asks the class to open their books to a page number. 
# A student can either start turning pages from the front of the 
# book or from the back of the book. They always turn pages one at 
# a time. When they open the book, page 1 is always on the right side.

# When they flip page 1, they see pages 2 and 3. Each page 
# except the last page will always be printed on both sides. 
# The last page may only be printed on the front, given the 
# length of the book. If the book is n pages long, and a student 
# wants to turn to page p, what is the minimum number of pages to 
# turn? They can start at the beginning or the end of the book.

# Given n and p, find and print the minimum number of pages that 
# must be turned in order to arrive at page p.

###############################################################
###########  Solve  ###########

import os
import math

def pageCount(n, p ):
  page_turns = 0
  diff = n - p
  # Find if book should open from front or back
  if p - 1 < diff:
    page_turns = math.floor(p / 2)
  else:
    if n % 2 == 0 and diff == 1:
      page_turns = 1
    else:
      page_turns = math.floor(diff / 2)
  return page_turns

###############################################################
###########  Main ###########

def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'A-020-input.txt')

  with open(input_file_path, 'r') as inputFile:
    content = inputFile.read().strip()
    test_cases = content.split('\n\n')

    results  = []
    for case in test_cases:
      lines = case.split('\n')
      n = int(lines[0].strip())
      p = int(lines[1].strip())
      print(pageCount(n, p))

if __name__ == '__main__':
  main()
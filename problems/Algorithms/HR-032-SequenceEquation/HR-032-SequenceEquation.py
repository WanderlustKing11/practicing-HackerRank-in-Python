# HackerRank - Algorithms
# Sequence Equation
# By Douglas Horville

# Given a sequence of n integers, p(1),p(2),...,p(n) where each element is distinct and satisfies 
# 1 <= p(x) <= n. For each  where 1 <= x <= n, that is x increments from 1 to n, find any 
# integer y such that p(p(y)) == x and keep a history of the values of y in a return array.

# permutationEquation has the following parameter(s):
# int p[n]: an array of integers

# Returns int[n]: the values of y for all x in the arithmetic sequence 1 to n

###############################################################
###########  Solve  ###########

def permutationEquation(p):
    y_history_array = [0] * len(p)
    y_index_table = {}
    for i in range(len(p)):
        # print(f'i = {i}')
        x = p[i]
        # print(f'x = {x}')
        for y in range(len(p)):
            if p[y] == i + 1:
                # print(f'y = {y}, p[y] = {p[y]}, and i + 1 = {i + 1}')
                y_index_table[y] = x 
                # print(y_index_table)
    
    for y_key in y_index_table:
        y_history_array[y_key] = y_index_table[y_key]
        # print(y_index_table[y_key])


    # print(y_index_table)
    # print()
    return y_history_array


###############################################################
###########  Main ###########

def main():
  print(permutationEquation([5,2,1,3,4])) # expected output: [4,2,5,1,3]
  print(permutationEquation([2,3,1])) # expected output: [2,3,1]
  print(permutationEquation([4,3,5,1,2])) # expected output: [1,3,5,4,2]

main()

# Std In is not complete. Will update input file and main function soon
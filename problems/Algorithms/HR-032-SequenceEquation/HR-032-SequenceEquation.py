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
    result = []
    position_map = {}
    
    # Fill dictionary with x values and their 1-based index
    for i in range(len(p)):
        position_map[p[i]] = i + 1

    # Loop through the map for x's position1 to find position 2 (y)
    for x in range(1, len(p) + 1):
        pos1 = position_map[x]
        pos2 = position_map[pos1]
        result.append(pos2)

    return result


###############################################################
###########  Main ###########

def main():
    print(permutationEquation([5,2,1,3,4])) # expected output: [4,2,5,1,3]
    print(permutationEquation([2,3,1])) # expected output: [2,3,1]
    print(permutationEquation([4,3,5,1,2])) # expected output: [1,3,5,4,2]

main()

# Std In is not complete. Will update input file and main function soon
# HackerRank - Algorithms
# Jumping On The Clouds [Revisited]
# By Douglas Horville

# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds 
# that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until 
# it reaches the start again.

# There is an array of clouds, c and an energy level e = 100. The character starts from c[0] and 
# uses 1 unit of energy to make a jump of size k to cloud c[(i + k) % n]. If it lands on a 
# thundercloud, c[i] = 1, its energy (e) decreases by 2 additional units. The game ends when the 
# character lands back on cloud 0.

# Given the values of n, k, and the configuration of the clouds as an array c, determine the 
# final value of e after the game ends.

# jumpingOnClouds has the following parameter(s):
# int c[n]: the cloud types along the path
# int k: the length of one jump

# Returns int: the energy level remaining.

###############################################################
###########  Solve  ###########

def permutationEquation(c, k):
    e = 100
    n = len(c)
    i = 0

    # print(f'c: {c}')
    while i != 0 or e == 100:
        # print(f'i = {i}, k = {k}, and n = {n}')
        i = (i + k) % n
        # print(f'jump lands i: {i}')
        # print(f'cloud is {c[i]}')
        if c[i] == 0:
            e -= 1
            # print(f'so e = {e}')
        else:
            e -= 3
            # print(f'so e = {e}')

    return e


###############################################################
###########  Main ###########

def main():
    print(permutationEquation([0,0,1,0], 2)) # expected output: 96
    print(permutationEquation([0,0,1,0,0,1,1,0], 2)) # expected output: 92

main()

# Std In is not complete. Will update input file and main function soon
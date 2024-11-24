# # HackerRank
# # Douglas Horville
# # JoC - Medium 

# The evil forest is guarded by vicious mandragoras. Garnet and her pet must make a journey through. She starts with  health point () and  experience points.

# As she encouters each mandragora, her choices are:

# Garnet's pet eats mandragora . This increments  by  and defeats mandragora .
# Garnet's pet battles mandragora . This increases  by  experience points and defeats mandragora .
# Once she defeats a mandragora, it is out of play. Given a list of mandragoras with various health levels, determine the maximum number of experience points she can collect on her journey.

# For example, as always, she starts out with  health point and  experience points. Mandragoras have the following health values: . For each of the beings, she has two choices, at or attle. We have the following permutations of choices and outcomes:

def mandragora(H):
    s = 1
    p = 0
    healthMap = {}
    index = 0
    # brute force, nested for loops
    ## loop once to assign everything as 'eat'
    ## loop the amount of elements in a list to change every variation of e/b

    # more optimal: loop once and put every health value in a dictionary
    ## find the largest number, add health from the other ones (eat) and battle the largest number (battle)
    for health in H:
        healthMap[index] = health
        index += 1
        # if 'e' then s + 1
        # if 'b' then p * H[i]
        



def main():
    print(mandragora([3,2,5]))


if __name__ == '__main__':
    main()
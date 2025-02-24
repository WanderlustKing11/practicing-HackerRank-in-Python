
def jumpingOnClouds(c):
    #1 create a tracker "jumps" (to return)
    #2 create a tracker array (path[])
    #3 while loop through the array 'c' with i (index)
    #4 conditional statement: if i (index) + 2 == 0 --> then jump to that index
    ## --> if not, then try i + 1 == 0 --> then jump to that index
    ## --> if not, then that must be the end of the array, and now we have to count number of jumps
    #5 at every jump, append the index number into the (path[]) array

    jumps = 0
    path = []
    i = 0
    while i < len(c):  # less than the last index + 1
        path.append(i)
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
            jumps += 1
        elif i + 1 < len(c) and c[i + 1] == 0:
            i += 1
            jumps += 1
        else:
            break
    print(path)
    return jumps






def main():
    print(jumpingOnClouds([0,1,0,0,0,1,0]))  # 3
    print()
    print(jumpingOnClouds([0,0,1,0,0,1,0]))  # 4
    print()
    print(jumpingOnClouds([0,0,0,0,1,0]))  # 3


if __name__ == '__main__':
    main()
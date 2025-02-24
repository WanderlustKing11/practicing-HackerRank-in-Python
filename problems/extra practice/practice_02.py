

def equalizeArray(arr):
    #1 declare a dicitonary (num_count)
    num_count = {}
    #2 for loop:
    for num in arr:
    #3 conditional: if num in num_count
        if num in num_count:
    ## --> then add + 1 to value
            num_count[num] += 1
    ## --> then add num as key
        else:
            num_count[num] = 1
    
    #4 another for loop to iterate through dictionary and find the largest value
    num_max = max(zip(num_count.values(), num_count.keys()))[1]
    print(f'num max:{num_max}')
    count = len(arr) - num_max
    print(f'count {count}')
    return count



def main():
    print(equalizeArray([1,2,2,3]))  # 2
    print()
    print(equalizeArray([3,3,2,1,3]))  # 2

main()
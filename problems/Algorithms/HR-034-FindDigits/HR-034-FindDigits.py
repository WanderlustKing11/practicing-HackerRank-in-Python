##############################################
#### Solve ####

def findDigits(n):
    # Write your code here
    num_of_divisors_occurring = 0
    arr_strings = list(str(n))
    for digit in arr_strings:
        if int(digit) != 0:
            if n % int(digit) == 0:
                num_of_divisors_occurring += 1
    return num_of_divisors_occurring

##########################################################
###### Main #######

def main():
    print(findDigits(12))
    print(findDigits(1012))


if __name__ == '__main__':
    main()
# HackerRank - Algorithms
# Find Digits
# By Douglas Horville

##############################################

# An integer d is a divisor of an integer n if the 
# remainder of n / d = 0.

# Given an integer, for each digit that makes up the integer 
# determine whether it is a divisor. Count the number of 
# divisors occurring within the integer.

# findDigits has the following parameter(s):
# int n: the value to analyze
# Returns int: the number of digits in  that are divisors of 

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
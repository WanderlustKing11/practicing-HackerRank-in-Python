# HackerRank - Algorithms
# Staircase
# By Douglas Horville

def staircase(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

def main():
    staircase(6)

main()
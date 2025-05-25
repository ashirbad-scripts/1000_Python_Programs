# Python Program to print all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50.

for n in range(0, 51):
    if (n % 2 != 0 and n % 3 !=0):
        print(n)

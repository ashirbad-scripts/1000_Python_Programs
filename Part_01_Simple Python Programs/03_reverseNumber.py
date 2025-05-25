# First approach
print("First Method")
n = int(input("Enter a number : "))
rev = 0

while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

print(f"Reversed number is {rev}")



print("\n-------------------------\n")



# Short approach
number = int(input("Enter a number :- "))
reversed_number = int(str(number)[::-1])
print(f"Reversed Number is {reversed_number}")

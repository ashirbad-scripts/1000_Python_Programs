a = int(input("Enter Starting value : "))
b = int(input("Enter Ending value : "))
n = int(input("Enter number to check : "))

for i in range(a,b):
  if (i%n == 0):
    print(f"'{i}' is divisible by {n}")

n = int(input("Enter a number : "))
total = 0

while (n>0):
  digit = n % 10
  total = total + digit
  n = n // 10

print(f"The total sum is '{total}'")

print("\n")

# Other approach
l = []
b = int(input("Enter a number : "))
while (b>0):
  dig = b % 10
  l.append(dig)
  b = b // 10
print("Sum is: ", sum(l))

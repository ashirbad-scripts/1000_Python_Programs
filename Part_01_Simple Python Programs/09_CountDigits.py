n = int(input("Enter a number : "))
count = 0
while (n>0):
  count = count + 1
  n = n // 10
print("The number of digits in given number are : ", count)

n = int(input("Enter any number: "))
sum = 0
for i in range(1, n):
  if (n % i == 0):
    sum = sum + i

if (sum == n):
  print("Perfect number")
else:
  print("Not Perfect")

# Explanation
'''
for eg. 
5 % 1 == 0 no
5 % 2 == 0 no
5 % 3 == 0 no
5 % 4 == 0 no
range was upto 4, so 5 is not perfect

for eg.
6 % 1 == 0, no
6 % 2 == 0, yes ---> sum = 0 + 2 = 2
6 % 3 == 0, yes ---> sum = 2 + 3 = 6
6 % 4 == 0, no
6 % 5 == 0, no
limit was 5
sum=6 == n=6, so its perfect


'''

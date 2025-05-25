n = int(input("Enter number to check : "))
temp = n
rev = 0

while(n>0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if temp == rev:
    print("The number is palindromic")

else:
    print("The number is not palindromic")

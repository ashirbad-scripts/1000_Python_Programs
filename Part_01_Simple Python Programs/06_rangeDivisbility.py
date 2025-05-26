Lower = int(input("Enter starting range : "))
Higher = int(input("Enter Ending range : "))

for i in range(Lower, Higher):
  if (i%5 == 0 and i%7== 0):
    print(f"{i} is divisble by 7 and a multiple of 5")

# take a number n and prin n + nn + nnnn, eg. 23 = 23 + 
n = int(input("Enter a number : "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print(f"{n} = {comp}")

# explanation:-
'''
t1 = 55
t2 = 555
comp = 5 + 55 + 555

'''

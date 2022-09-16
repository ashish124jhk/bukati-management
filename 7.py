n=int(input("Enter a number :"))
i=2
temp = 0
while (i<= n-1):
    if(n%i ==0):
        temp = 1
        break
    else:
        i = i + 1
if (temp ==0):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
    

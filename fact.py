# WAP to print factorial of a given number #
i=int(input("Enter a number:"))
fac=1
while i>0:
    fac=fac*i
    i=i-1
print("Factorial=",fac)

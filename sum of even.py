# WAP to find sum of even number from 1 to n #
n=int(input("Enter a number:"))
i=2
sum=0
while(i<=n):
    if (i%2==0):
     sum=sum+i
    i=i+2
print("sum of even number=",sum)    
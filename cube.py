# WAP to print sum of CUBE from 1 to 10 #
n=int(input("enter a number:"))
i=1
sum=0
while(i<=n):
    sum=sum+i*i*i
    i=i+1
print("sum of cube=",sum)
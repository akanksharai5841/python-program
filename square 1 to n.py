# WAP to print sum of SQUARE from 1 to n #
n=int(input("Enter a number:"))
i=1
sum=0
while(i<=n):
    sum=sum+i*i
    i=i+1
print("sum of square=",sum)
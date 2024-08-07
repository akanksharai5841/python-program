# WAP to print only even numbers between 1 to n #
n=int(input("Enter a number:"))
i=2
while(i<=n):
    if i%2==0:
       print(i)
       i=i+2
       
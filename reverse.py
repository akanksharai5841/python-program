# WAP to reverse a given number #
n=int(input("Enter a number:"))
rev=0
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
print("Reverse number is:",rev)  

# WAP to check whether a given number is palindrome or not #
n=int(input("Enter a number:"))
rev=0
x=n
while(n>0):
    rev=(rev*10)+n%10
    n=n//10
if(x==rev):
    print("palindrome number")
else:
    print("Not Palindrome")
            

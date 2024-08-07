# WAP to check whether a given number is armstrong or not #
i=int(input("Enter a number:"))
orig=i
sum=0
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")        

a=[]
for i in range(5):
    x=input("Enter item to add in the list:")
    a.append(x)
x=input("Enter value whose frequency you want:")
f=a.count(x)
print("frequency of ",x,"=",f)    
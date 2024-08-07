a=[]
size=int(input("Enter size of the list:"))
for i in range(size):
    val=int(input("Enter number:"))
    a.append(val)
a.sort()
print("max number=",a[size-1])
print("sec max number=",a[size-2])    
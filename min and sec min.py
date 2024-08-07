a=[]
size=int(input("Enter size of the list:"))
for i in range(size):
    val=int(input("Enter number:"))
    a.append(val)
minval=min(a)
print("min value in the first list is:",minval) 
a.remove(minval)
secmin=min(a)
print("second min value in the list:",secmin)   

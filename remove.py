a=[]
for i in range(5):
    x=input("Enter value:")
    a.append(x)
print("original list is:",a)
value=input("Enter value to remove:")
a.remove(value)
print("list after deletion:",a)  
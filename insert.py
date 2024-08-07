a=[]
for i in range(5):
    x=input("Enter value:")
    a.append(x)
print("original list is:",a)
index=int(input("Enter index where you want to insert:"))  
value=input("Enter value to insert:")
a.insert(index,value)
print("list after insertion:",a)  
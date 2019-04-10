n=int(input("Enter the number of elements in a list"))
elem=int(input("Enter element to be deleted"))
a=[]
for i in range(0,n):
        x=int(input("Enter the element"))
        a.append(x)
print(a)
try:
    a.remove(21)
except:
    print("Element not found")
print(a)
        
    

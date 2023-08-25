#program to left rotate the array by one position
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a=a+[x]
temp=a[0]
for i in range(n-1):
    a[i]=a[i+1]
a[n-1]=temp
print("The array after left rotate by one position is",a)

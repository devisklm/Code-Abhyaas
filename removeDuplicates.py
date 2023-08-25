#program to remove duplicates from an array
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a=a+[x]
i=0
j=1
while(j<n):
    if(a[i]==a[j]):
        j+=1
    else:
        i+=1
        a[i]=a[j]
        j+=1
print("The array after remove duplicates is",a[0:i+1])
    

#program to find second largest and second smallest element in an array
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a=a+[x]
maxi=max(a[0],a[1])
secmaxi=min(a[0],a[1])
mini=min(a[0],a[1])
secmini=max(a[0],a[1])
for i in range(n):
    if(a[i]>maxi):
        secmaxi=maxi
        maxi=a[i]
    if(a[i]>secmaxi and a[i]!=maxi):
        secmaxi=a[i]
    if(a[i]<mini):
        secmini=mini
        mini=a[i]
    if(a[i]<secmini and a[i]!=mini):
       secmini=a[i]
print("The second largest element is",secmaxi)
print("The second smallest element is",secmini)
        

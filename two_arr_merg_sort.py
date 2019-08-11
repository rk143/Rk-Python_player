r,k=list(map(int,input().split()))
s=list(map(int,input().split()))[:r]
a=list(map(int,input().split()))[:k]
l=s+a
u=sorted(l)
for i in u: 
 print(i, end=" ")

a=[1,2,3]
b=[300,200,100]
b.reverse()
c={}
for i in range(0,len(a)):
    c[a[i]]=b[i]
print(c)

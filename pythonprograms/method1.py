a=[1,2,3,2,3,2,3,4]
c=[]
b={}
for i in range(0,len(a)):
	s=a.count(a[i])
	c.append(s)
for i in range(0,len(a)):
    b[a[i]]=c[i]
print(b)

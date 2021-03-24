a="agsdjoj1234567"
for i in range(len(a)):
    if(a[i].isnumeric()):
        b=int(a[i])
        if(b%2==0):
            print(a[i],end="")

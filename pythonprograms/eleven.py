a=int(input())
b=int(input())
amount=a*b
if(amount>100):
    if(amount>500):
        print("greater than 500")
    else:
        if(amount>=400)and(amount<=500):
            print(amount)
        elif(amount>=300)and(amount<=400):
            print("in between 300 to 400")
        elif(amount>=200)and(amount<=300):
            print("in between 200 to 300")
        elif(amount>=100)and(amount<=200):
            print("in between 100 to 200")
        else:
            print("equals to 100")
else:
    print("lessthan 100")

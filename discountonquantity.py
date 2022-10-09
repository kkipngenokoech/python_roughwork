userquantity=int(input("enter quantity purchased:"))
if userquantity>=1000:
    print(0.9*userquantity*100)
else:
    print(userquantity*100)

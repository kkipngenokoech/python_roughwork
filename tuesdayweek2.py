#assignment one
usergrade=int(input("enter your marks:"))
if usergrade>=70 and usergrade<=100:
    print("A")
elif usergrade>=60 and usergrade<=69:
    print("B")
elif usergrade>=50 and usergrade<=59:
    print("C")
elif usergrade>=40 and usergrade<=49:
    print("D")
elif usergrade>=0 and usergrade<=39:
    print("E")
else:
    print("incorrect value entered please retry again")


#assignment two
userquantity=int(input("enter quantity purchased:"))
if userquantity>=1000:
    print(0.9*userquantity*100)
else:
    print(userquantity*100)

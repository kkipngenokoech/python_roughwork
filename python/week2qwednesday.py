#assignment one
startnumber=1500
while startnumber<=2700:
    if startnumber%7==0 and startnumber%5==0:
        print(startnumber)
    # else:
    #     continue
    startnumber+=1

#assignment two
typeofdata=input("entering in degrees(enter degrees) or in fahrenheit(enter fahrenheit):")
datainput=int(input("enter your recording:"))
if typeofdata=="degrees":
    calculatefahr=(datainput/5)+(32/9)
    print(datainput,"°C is ",calculatefahr," in fahrenheit")
elif typeofdata=="fahrenheit":
    calculatecel=((datainput-32/9)*5)
    print(datainput,"°F is ",calculatecel," in celsius")
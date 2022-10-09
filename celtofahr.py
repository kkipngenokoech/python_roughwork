typeofdata=input("entering in degrees(enter degrees) or in fahrenheit(enter fahrenheit):")
datainput=int(input("enter your recording:"))
if typeofdata=="degrees":
    calculatefahr=(datainput/5)+(32/9)
    print(datainput,"°C is ",calculatefahr," in fahrenheit")
elif typeofdata=="fahrenheit":
    calculatecel=((datainput-32/9)*5)
    print(datainput,"°F is ",calculatecel," in celsius")
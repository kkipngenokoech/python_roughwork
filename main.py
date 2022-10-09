a=[5,10.0]
print(id(a))
b=a
print(id(b))#checks location of the variable stored
print(id(a[0]),id(b[0]))
a[0]=56
print(id(a[0]),id(b[0]))
data_copy=a.copy()
print(data_copy)
print(a[1])#"""
data_1=4.5
data_2=[2,3,4,5]
data=[data_1,data_2,"True",True,23,23.34]
print(data)
print(data[1])
print(data[1][1])
data[1][1]=9
print(data[1][1])
names=["abaraham","john","stanely","wizzard"]
print(names[0][0])
print(names[1][0])
print(names[2][0])
print(names[3][0])
sports=["football","NBA","F1","tennis","badmitton","basketball"]
print("i like to play {}".format(sports[0]))
print("i like to play {}".format(sports[1]))
print("i like to play {}".format(sports[2]))
#assignment one
from random import shuffle
numberlist=[12,34,65,34,23,45]
shuffle(numberlist)
print(numberlist)


#assignment two
listthirty=[]
for index in range(1,31):
    listthirty.append(index*index)
print(listthirty[-5:])
print(listthirty[:5])
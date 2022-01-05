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

#LISTS WITHIN LISTS
data_1=4.5
data_2=[2,3,4,5]
data=[data_1,data_2,"True",True,23,23.34]
print(data)
print(data[1])
print(data[1][1])
data[1][1]=9
print(data[1][1])

#ACCESSING STRINGS WITHIN A LIST
names=["abaraham","john","stanely","wizzard"]
print(names[0][0])
print(names[1][0])
print(names[2][0])
print(names[3][0])
sports=["football","NBA","F1","tennis","badmitton","basketball"]
print("i like to play {}".format(sports[0]))
print("i like to play {}".format(sports[1]))
print("i like to play {}".format(sports[2]))

#USING FOR LOOPS WITH LIST
for Sports in range(len(sports)):
    print("i like to play {}".format(sports[Sports]))

for even_numbers in range(0,100,2):
    print(even_numbers)

for odd_numbers in range(1,101,2):
    # add code to print odd numbers
    pass
for divisible_3 in range(1,100):
    if divisible_3%3==0:
        print(divisible_3)
    else:
        continue

#WHILE LOOPS
health=10
while health>0:
    print("game is still on")
    health=health-1#health-=1
#Input=input("enter a word").lower()
"""while Input!="quit":
    print(Input)
    Input = input("\nenter a word").lower()
"""

#SLICING LISTS
slice_numbers=[1,2,3,4,5,6,7,8,9]
sliced_numbers=slice_numbers[0:2]#outputs from index 0 to index 2-1
print(sliced_numbers)

#ADDING ITEMS TO YOUR LIST
#appends()-adds items to the back of your list
append_list=[1,2,3,4,5,6,78]
append_list.append(23)
print(append_list)
#insert()-adds an item to a specific location
insert_list=[1,2,3,4,5,6,7]
insert_list.insert(3,34)
print(insert_list)

#REMOVING ITEMS FROM YOUR LIST
remove_item=[1,2,3,4,56,7]
remove_copy=remove_item.copy()
#pop()-removes the last item on the list,but you can always add an index
#it returns the removed element as well
remove_item.pop()
print(remove_item)
pop_item=remove_item.pop(0)
print(pop_item)
#remove()-it removes the element given
remove_copy.remove(56)
print(remove_copy)
try:
    print(remove_copy.remove(56))
except:
    print("that number that doesnt exist")
print(remove_copy)

#USING NUMERICAL DATA
numerical_data=[12,43,76,36,59,87,2345]
print(max(numerical_data))
print(min(numerical_data))
print(sum(numerical_data))

#SORTING A LIST
#sorted() function using  numerical or alphethical
#it returns a copy of a list
sort_numbers=[90,65,34,44,98,56,36,12,678]
sorted_numbers=sorted(sort_numbers)
print(sorted_numbers)

#.sort()-this changes the original list
sorted_numbers.sort()
print(sorted_numbers)

#USING CONDITIONAL STATEMENTS
in_names=["john","mary","melanie","edgar"]
if "mary" in in_names:
    print("found")
if "melanie" not in in_names:
    print("not found")

#CHECK AN EMPTY LIST
if in_names==[]:
    print("empty")
if not in_names:
    print("empty")


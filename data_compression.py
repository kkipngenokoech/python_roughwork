#LIST COMPRESSION
"""
used to reduce the iteration lines into one line
syntax-variable_name=[item_to_append for item in item_list if condition]
        variable_name=[item_to_append if condition else item_to_append for item in item_list]
"""
numbers_compression=[number for number in range(100)]#number here stands for index
print(numbers_compression)
#the former way is:
numbers_append=[]
for index in range(100):
    numbers_append.append(index)
print(numbers_append)

#list compression using if condition
numbers_condition=[number_condition for number_condition in range(100) if number_condition%2==0]
print(numbers_condition)
#the former way is :
numbers_append_condition=[]
for index in range(100):
    if index%2==0:
        numbers_append_condition.append(index)
print(numbers_append_condition)

#list compression using if else condition
number_if_else=["even" if index %2==0 else "odd" for index in range(100)]
print(number_if_else)
#the former way is:
number_append_else=[]
for index in range(10):
    if index%2==0:
        number_append_else.append("even")
    else:
        number_append_else.append("odd")
print(number_append_else)

#LIST COMPRESSION WITH VARIABLES
var_number=[2,3,4,5]
squared_numbers=[index**2 for index in var_number]
print(squared_numbers)
#the former way is:
square_number=[]
for index in var_number:
    square_number.append(index**2)
print(square_number)

#DICTIONARY COMPRESSION
"""
for dictionary you just have to add two  variables instead of one
"""
dict_number=[index for index in range(10)]
dict_compress={index:index**2 for index in dict_number if index%2==0}
print(dict_compress)
#excersice
degree_list=[12,21,15,32]#[53.6,69.8,59,89.6]
fahrenheit=[index*(9/5)+32 for index in degree_list]
print(fahrenheit)

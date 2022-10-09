#FUNCTION SYNTAX
"""
def function_name(parameter passed):
"""
#FUNCTION DEFINITION-user defined function
def print_info():#non parametized function
    print("NAME:newlyne")#in built function
    print("age:20")
#FUNCTION CALL
print_info()
print_info()

#FN WITH PARAMETERS
def print_Info(name,age):#name and age are parameters
    print("NAME:{}".format(name))
    print("age:{}".format(age))
print_Info("newlyne",20)#newlyne and 20 are arguements

#passing a list as a parameter
numbers_1=[2,3,4,5,12]
numbers_2=[9,8,7,6,10,56]
def square_list(numbers_square):
    for index in numbers_square:
        print(index**2)
square_list(numbers_1)
square_list(numbers_2)

#using defaults parameters-they always come after the non-default parameters
def calculate_area(radius,PIE=3.14):
    print("AREA:{}".format(PIE*radius*radius))
calculate_area(4)

#optional parameters
def enter_name(first,last,middle=" "):
    if middle:
        print("{} {} {}".format(first, middle, last))
    else:
        print("{} {}".format(first, last))
enter_name("Newlyn","koech","cherono")
enter_name("newlyne",last="cherono")#you can assign specific arguements to specific parameters

#PASSING ANY NUMBER OF ARGUEMENTS YOU WANT IN THE FUNCTION
def multiple_varied(*data):
    print(type(data))#tupple type
    for index in data:
        print(index)
multiple_varied("newlyne","cherono",20,"nurse")

#pasing many arguements during call ,but allows us to define it as a dictionary
def dictionary_varied(**data_1):
    print(type(data_1))
    print(data_1["NAME"])
    print(data_1["AGE"])
dictionary_varied(NAME="Newylne",AGE=20,cute=True)
first_name="newylene"
last_name="cherono"
print(first_name,last_name,20)

#USING RETURN KEYWORD INSTEAD OF PRINT WITHIN A FUNCTION
def adding_numbers(a,b):
    return a+b
sum_of_numbers=adding_numbers(20,19)
print(sum_of_numbers)

#USING TERNARY OPERATOR
def search_list(the_list,element):
    return True if element in the_list else False
end_result=search_list([12,"john",34,23.0,True],23.0)
print(end_result)

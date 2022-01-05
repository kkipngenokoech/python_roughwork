"""
lambda arguements:expression-always begins with key word lambda
lambda arguements:value_to_return if condition else value_to_return
"""
print((lambda index:index**2)(4))
#the former way is:
def square_num(index):
    return index**2
print(square_num(4))
#passing multiple arguements to a lambda function
print((lambda x,y:x*y)(2,3))

#using conditional statements in labda functions must contain both  if and else statements
greater=lambda x,y:x if x>y else y
result=greater(10,19)
print(result)
#we can returna lambda function
def my_function(index):
    return lambda x:index*x
doubler=my_function(2)
print(doubler(5))
#exercise
convert_fahrenheit=lambda degree_value:degree_value*(9/5)+32
print(convert_fahrenheit(12))

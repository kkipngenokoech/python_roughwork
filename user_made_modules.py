"""
you create two seperate files and the same directory or same project then if you want to use functins already defined in the other oython file
you just import it
there are several files in ths project and we are going to import one of them below
"""
import data_compression as data_compress#we imported the data_compression py and allocated it a new name data_compress
#from workingwithfunctions import
from test_file import get_formatted_name
print("enter q to quit")
while True:
    first_name=input("\nplease give me a first name:").title()
    if first_name=='Q':
        break;
    last_name=input("please give me a last name:").title()
    if last_name=='Q':
        break;
    formatted_name=get_formatted_name(first_name,last_name)
    print("your name is {}".format(formatted_name))

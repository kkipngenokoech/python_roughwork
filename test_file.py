from IPython.display import clear_output
def get_formatted_name(first, last,middle=""):
    full_name = f"{first} {middle} {last}"
    return full_name.title()


"""
first_name=input("enter your first name:")
clear_output()
last_name=input("enter your last name:")
clear_output()
print("hi my name is ",get_formatted_name(first_name,last_name))
"""
# PASSING TEST
"""
a passing test=import the unitest module,then create a class that inherits from the unittest.Testcase
and write a series of methods that tests your code functionality
"""
#"""
from test_file import get_formatted_name
import unittest
class name_test(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("jane", "doe", "kurt")
        self.assertEqual(formatted_name, 'Jane Kurt Doe')
if __name__ == '__main__':
    unittest.main()
#"""
# FAILING TEST
"""
in a failing test ,we do the opposite,we expect the test code to fail
"""
def get_full_name(first,middle,last):
    full_name = f"{first} {middle} {last}"
    return full_name.title()
#print(get_full_name("newylne","cherono"))
#print(get_full_name("newylne","cherono","koech"))
from test_file import get_full_name
class name_test(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_full_name("jane", "doe")
        self.assertEqual(formatted_name, 'Jane  Doe')
if __name__ == '__main__':
    unittest.main()

#TEST FOR CLASSES
class anonymous_survey:
    def __init__(self,question):
        self.question=question
        self.responses=[]
    def show_question(self):
        print(self.question)
    def store_response(self,new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("show results:")
        for response in self.responses:
            print(response)
"""
question=input("what language did you learn first?")
clear_output()
my_survey=anonymous_survey(question)
my_survey.show_question()
print("\nenter q to quit at any time to quit")
clear_output()
while True:
    response=input("language:")
    clear_output()
    if response=='q':
        break;
    my_survey.responses.append(response)
print("thank you for everyone who participated in the survey")
my_survey.show_results()
"""
from test_file import anonymous_survey
class test_anonymous_survey(unittest.TestCase):
    def test_store_response(self):
        question=input("which language did you learn first:").title()
        my_survey=anonymous_survey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
if __name__ =="__main__":
    unittest.main()
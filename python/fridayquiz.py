#bitwise operators
interger1=2
interger2=3
#print(interger1+interger2)
while interger2!=0:
    carry=interger2&interger1
    interger1=interger1^interger2
    interger2=carry<<1
print(interger1)


#priority in python
from collections import deque
import re
operators="+-/*"
parenthesis="()"
priority={
    '+':0,
    '-':0,
    '*':1,
    '/':1
}
def testpriority(operatorone,operatortwo):
    return priority[operatorone]>=priority[operatortwo]

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
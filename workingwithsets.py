#sets are unordered -they cannot be accessed with indexes but with key values
#DECLARING A SET
#USING CURLY BRACKETS AND SQUARE BRACKETS
set_1=set([1,2,3,4,5])
#using curly bracketd like in dictionaries
set_2={1,2,3,4,5}
print(type(set_1),type(set_2))

#adding elements to sets
set_1.add(6)
print(set_1)
#removing element for set
set_1.remove(6)
print(set_1)

#FROZENSETS-COMBINATION OF SETS AND TUPLES
#immutable unordered and unique
frozen_set=frozenset([1,2,3,4,5])
print(type(frozen_set))
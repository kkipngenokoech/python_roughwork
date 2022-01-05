#dictionaries are ordered and mutable
#DECLARING DICTIONARIES
empty_dict={}
print(type(empty_dict))
name_dict={"NAME":"newylne","AGE":20}
print(name_dict)
empty_dictfn=dict()
print(empty_dictfn)

#ACCESSING DICTIONARY INFORMATION
person_dict={"NAME":"newylne","age":20}
print(person_dict["NAME"])
print(person_dict.get("NAME"))#if key is not found it return none
print(person_dict.get("AGE","AGE IS AVAILABLE"))

#COMBINING DICTIONARIES WITH LISTS
data_dictlist={"sports":["baseball","basketball","lawn tennis","skating"],"games":["GTA","NFS","PES"]}
print(data_dictlist["sports"][0])
list_course=["BSE","BCS","BIT","BCT"]
course_dict=dict({"faculty":list_course})
print(course_dict)

#LIST WITH DICTIONARIES
data_listdict=[23,"new hamsphere",{"NAME":"rich.com","AGE":20}]
print(data_listdict[0])
print(data_listdict[2])
print(data_listdict[2]["NAME"])

#DICTONARIES WITHIN DICTIONARIES
dict_dict={"TEAM":"OLANDO PIRATES","TEAM_POS":4,"COMPETITIONs":{"FA":"QUARTER_FINAL","EPL":2}}
print(dict_dict)

#adding new information to a dictionary
addto_dict={"NAME":"CHELSEA","COMPETITON":"EPL"}
addto_dict["COLOR"]="BLUE"
print(addto_dict)
print(addto_dict["COLOR"])
print(addto_dict.get("color","color present"))

#changing the value of the infromation in the dictionary
addto_dict["COLOR"]="WHITE"
print(addto_dict["COLOR"])#it overwrites the data if the key is present else creates a new one
addto_dictcopy=addto_dict.copy()
#deleting an element in the dictionary
try:
    del addto_dict["COLOR"]
    print(addto_dict)
except:
    print("the key doesnt exist")
#ITERATING OVER A DICTIONARY
#using both keys and values together
for key,value in addto_dictcopy.items():
    print("{}:{}".format(key,value))
#using keys only
for key in addto_dictcopy.keys():
    print("{}:-{}".format(key,addto_dictcopy[key]))
#looping only values
for value in addto_dictcopy.values():
    print(value)
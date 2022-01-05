"""
values={4:4,8:8,"o":10,"ace":11}
cards=("o","hearts")
print("{}".format(values[cards[0]]))
"""
#CREATING YOUR FIRST CLASS
class car():
    pass#this means we shall code later
#all data types are classes at their base

#CREATING AN OBJECT-THATS INSTATINIATING A CLASS
ford=car()
subaru=car()
hillux=car()
volkswagen=car()
print(ford)
print(subaru)

#PASSING ATTRIBUTES TO CLASS
class car_1():
    sound="beep"
    color="blue"
ford_1=car_1()
print(ford_1)#gives you the type and its location of the object
print(ford_1.color)#helps you access the attribute of the car

#CHANGING THE ATTRIBUTE OF THE OBJECT
ford_1.sound="honk"
print(ford_1.sound)

#using init__() method
#it means initialization method-it helps personalize the attributes
class car_2():
    sound="beep"#global attribute
    def __init__(self,color,model):
        self.color=color#class/instance attribute-due to use of the self parameter
        self.model=model
ford_2=car_2("blue","SUV")
print(ford_2.color,ford_2.model)


#ADDING METHODS TO A FUNCTION
class dog():
    def make_sound(self):
        print("bark")
jimmy=dog()
jimmy.make_sound()
#passing parameters to a method
class dog():
    def make_sound(self,action_sound):#it has a self parameter hence on;y accessible by the instances only
        print(" a dog ",action_sound)#use self.attribute to access attributes created within a class
    def print_information():#without the self parameter ,it vannot be accessed by the objects of this class
        print("i am an animal")
jimmy=dog()
jimmy.make_sound("barks")
#jimmy.print_information()
#dog.print_information()

#USING SETTERS AND GETTERS
class person():
    name=""
    def set_name(self,new_name):
        self.name=new_name
    def getName(self):
        return self.name
person_1=person()
person_1.set_name("edwin odegard")
print(person_1.getName())

#CALLING METHODS WITHIN METHODS
class person_1():
    def __init__(self,name,age):#this is a magic method-it has two underscores
        self.name=name
        self.age=age
    def get_age(self):
        return self.age
    def judge_age(self):
        if self.get_age()<18:
            print("you are under age and not allowed in")
        else:
            print("enjoy your stay here,and welcome")
kiptoo=person_1("kevin",17)
kiptoo.judge_age()

#INHERITANCE
"""
it allows users to have code reusability
"""
class Animal():
    def make_sound(self):
        print("roar")
class dog(Animal):
    species="canine"
    print("hello i am a dog and i ")
sam=dog()
sam.make_sound()

#USING SUPER()-USING THIS METHOD ALLOWS US TO PASS ARGUEMENTS OF THE SUB CLASS INTO THE SUPER CLASS
class animal_1():
    def __init__(self,species):
        self.species=species
class dog_1(animal_1):
    def __init__(self,species,name):
        self.name=name
        super().__init__(species)
jimmy_1=dog_1("canine","jimmy")
print(jimmy_1.species)

#METHOD OVERRIDING
"""
python always checks for the method found in the sub class first,if not found it then checks the superclass
"""
class animal_2():
    def make_sound(self):
        print("roar")
class dog_2(animal_2):
    def species(self,species):
       # self.species=species
        #print("i am a {} and i ".format(species))
        return self.species
    def make_sound(self,sound_made):
        print("i am a{} and i{}".format(self.species,sound_made))
ricky=dog_2()
ricky.species("canine")
ricky.make_sound("bark")

#INHERITING MULTIPLE CLASSES
class physics():
    gravity=9.8
class automobile():
    def __init__(self,make,model,year):
        self.make,self.model,self.year=make,model,year
class ford(physics,automobile):#it accesses both the physics and aoutomobile car attributes
    def __init__(self,model,year):
        automobile.__init__(self,"ford",model,year)#the super method doesnt work on the multiple inhetiance
truck=ford("f-150",2008)
print(truck.gravity,truck.model)

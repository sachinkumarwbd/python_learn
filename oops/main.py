# types of programing

# 1 imperative
# 2 functional
# 3 object oreinted


# for pillers of oops

# 1 Encaplsulation?
# ==Encapsulation is a way to restrict the direct access to some components of an object, so users cannot access state values for all of the variables of a particular object. Encapsulation can be used to hide both data members and data functions or methods associated with an instantiated class or object.


# 2 Abstraction?
# ==Abstraction is a process of hiding the implementation details from the user. It provides a way to focus on what the object does instead of how


# 3 Inheritance?
# ==Inheritance is a way to reuse the code from another class without copying the code or creating new code. It is a mechanism in which one




# 4 Polymorphism?
# ==Polymorphism is a way to perform a single action in different forms. It is a feature that allows one interface to be used for a polemorphism behavior and multiple task


# what is classes?
# === class is a blueprint for creating objects
# === class is a template for creating objects
# === class is a collection of data and functions


# what is objects?
# === objects are instances of classes
# === objects are created from classes


class Obj:  # create a varaiables thats is attribute in a class
    __a = 12  # private variables using encapsiultion and dont be access
    b = 13  # publice variables
    def __hello():  # create a function thats is method in a class
        print("hello")
    __hello() 

Obj()
print(Obj.b)


# Objects

class cars:
    a= 12
    b= 13

obj = cars()
obj2 = cars()
print(obj2.b)
print(obj.a)



# constructor

class cars:   # super class
    def __init__(self,a,b):  # initilization
        self.a = a
        self.b = b

    def hello(self):       # object method
        print(f"hello\n{self.a},{self.b}") 

class newcars:   #multiple inheritance
    def __init__(self):
    
        print("hello world")


class honda(newcars,cars):   # this is inheritance all propertice other class to inherite
    # def __init__(self, a, b):     # sub class
    #     super().__init__(a, b) 
  pass         
       
       
Allcars = cars(12,13)
Allcars2 = cars(14,16)
print(Allcars.a)
print(Allcars.b)
print(Allcars2.a) 
print(Allcars2.b)

allcars = honda()

allcars.hello()


# Polymorphism?

class person:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)   
      

class animal(person):    # method overrinding
    # def __init__(self,name):
    #     self.name = name
    def show(self):
        print(self.name)    

person1 = person('sachin') 
animal1 = animal('lion')    # firts peroitry

person1.show()
animal1.show()



# abstraction

from abc import ABC , abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perieter(self):
        pass

class Circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        pass

    def perieter(self):
        pass    

circle1 = Circle(12)          

        
    

  
        
        
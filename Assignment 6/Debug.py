class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor=flavor
        self.frosting = frosting


class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    def oldCar(self):
        if self.year <= 2005:
            return "your car is old"
        else:
            return "your car not old"
    
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog( "pepper", 4)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("sydney", 102404950, "kitchen")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name)
    print(newEmployee.idNumber)
    print(newEmployee.department)

    print()
    
    #now create and print out a cake you make
    bdayCake= Cake("banana", "cream cheese")
    print(bdayCake.flavor , "with", bdayCake.frosting, "icing")
    
    #and now create another cake and print it out
    cakee= Cake("chocolate", "chocolate")
    print(cakee.flavor , "with", cakee.frosting, "icing")

    
    
    #create a cat!
    cat1 = Cat("Baloo", "9", "short")
    #create another cat!
    cat2= Cat("Soup", "3", "Long")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    carr= Car("Prius", 2014, "red")
    #Now print out the function you made for car :)
    print(carr.oldCar())

main()

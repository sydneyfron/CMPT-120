#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random
class student:
    def __init__(self, name, id, year, major, gpa):
        self.name=name
        self.id=id
        self.year=year
        self.major=major
        self.gpa=gpa

    def inHonors(self):
        if self.gpa> 3.5:
            return True
        else:
            return False

    def freeFood(self):
        num= random.randint(1,100)
        if num== self.id:
            print("winner! student (name) gets free lunch!")
        else:
            print("loser")
    
    
    
    
    
    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    stu1= student("sam", 23, "f", "edu", 3.8)
    stu2= student("leaf", 4, "s", "psyc", 3)
    stu3= student("branch", 55, "j", "comp sci", 3.3)

    print(stu1.inHonors())
    print(stu1.freeFood())
    print(stu2.inHonors())
    print(stu2.freeFood())

    print(stu3.inHonors())
    print(stu3.freeFood())
    
main()

def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isnumeric():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
    smt=input("Enter asterisk or ampersand: ")
    if smt=="*":
        print("star")
    else:
        print("and")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    cake=input("Enter integer: ")
    if cake.isnumeric():
        cake=int(cake)
    else:
        print("not int")

    # last challenge: find out how to check if the string input has the substring "marist"
    words=input("Enter stuff: ")
    if words.find("marist") >-1:
        print("marist present")
    else:
        print("not present")
    #google this one ;) substring is the key google term
    
main()

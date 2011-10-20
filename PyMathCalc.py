
## This is covered by the Creative Commons
## BY - NC - SA
## http://creativecommons.org/licenses/by-nc-sa/3.0/au/
## Original Creator William Pemberton
## Version 0.1 - Alpha PyMathCalc

#Imports
import math,sys,os

#initiation of global varibles
working = True

#Functions
def menu():
    global working
    print("""
______________
|----MENU----|
|____________|
z.square
x.rectangle
c.circle
v.triab(a,b)
b.triac(a,c)
n.tribc(b,c)
m.tri(a,b)
a.Hexagon
o.Working out (Toggle) = """ + str(working) + """
q.exit""")
    input = raw_input("> ")
    if input == "z" :
        square()
    elif input == "x":
        rectangle()
    elif input == "c":
        circle()
    elif input == "v":
        triab()
    elif input == "b":
        triac()
    elif input == "n":
        tribc()
    elif input == "m":
        tri()
    elif input == "a":
        hex()
    elif input == "o":
        working = True if working== False else False
    elif input == "q" :
        sys.exit(0)
    raw_input("Press enter to continue...")
    os.system("cls")
    menu()
    
    
#def input(): #Original input methord
#    input = raw_input("> ")
#    if input == "q":
#        sys.exit(0)
#    elif input == "m":
#        menu()
#    else:
#        return input

def square():
    global working
    #print("What is the length of the sides?")
    #side = int(input())
    side = int(what("length of the sides"))
    p = str(side*4.0)
    a = str(side*side)
    side = str(side)
    if working:
        print("Side length: "+side+" Units")
        print("Perimeter:   "+side+" x 4 = "+p+" Units")
        print("Area:        "+side+" x "+side+" = "+a+" Square Units")
    else:
        print("Side length: "+side+" Units")
        print("Perimeter:   "+p+" Units")
        print("Area:        "+a+" Square Units")

def rectangle():
    global working
    #print("What is the length?")
    #length = int(input())
    #print("What is the height?")
    #height = int(input())
    length = int(what("length"))
    height = int(what("height"))
    p = str((length*2.0)+(height*2.0))
    a = str(length*height)
    length,height = (str(length),str(height))
    if working:
        print("Length:     "+length+" Units")
        print("Height:     "+height+" Units")
        print("Perimeter:  ("+length+" x 2) + (" + height + " x 2) = "+p+" Units")
        print("Area:       "+a+" Squared Units")
    else:
        print("Length:    "+length+" Units")
        print("Height:    "+height+" Units")
        print("Perimeter: "+p+" Units")
        print("Area:      "+a+" Squared Units")

def circle():
    global working
    #print("What is the Diameter?")
    #diam = int(input())
    diam = int(what("diameter"))
    cir = str(diam*math.pi)
    radius = diam/2.0
    area = math.pi*(radius*radius)
    radius = str(radius)
    diam = str(diam)
    if working:
        print("Circumference:   " + "Pi x " + diam + " = " + cir + " Units")
        print("Diameter:        " + diam + " Units")
        print("Radius:          " + diam + " \ 2 = " + radius + " Units")
        print("Area:            " + "Pi x (" + radius + " x " + radius + ") = " + str(area) + " Squared Units")
        print("(The rest is divided by their respective amounts.)")

    else:
        print("Circumference:   " + cir + " Units")
        print("Diameter:        " + diam + " Units")
        print("Radius:          " + radius + " Units")
        print("Area:            " + str(area) + " Squared Units")
    print("Semi area:       " + str(area/2.0) + " Squared Units")
    print("quater:          " + str(area/4.0) + " Squared Units")
    print("Area per degree: " + str(area/360.0) + " Squared Units")

def triab():
    global working
    #print("What is the base?")
    #a = int(input())
    #print("What is the height?")
    #b = int(input())
    a = int(what("base"))
    b = int(what("height"))
    c = math.sqrt((a*a)+(b*b))
    if working:
        print("Hypotenuse: sqrt(("+str(a)+"x "+str(a)+") + ("+str(b)+" x "+str(b)+"))")
    #print str(c)
    tri(a,b,c)

def triac():
    global working
    #print("What is the base?")
    #a = int(input())
    #print("What is the hypo?") #Get full word for "c"
    #c = int(input())
    a = int(what("base"))
    c = int(what("Hypotenuse"))
    b = math.sqrt((c*c)-(a*a))
    if working:
        print("Height: sqrt(("+str(c)+" x "+str(c)+") + ("+str(a)+" * "+str(a)+"))")
    #print str(b)
    tri(a,b,c)
	
def tribc():
    global working
    #print("What is the height?")
    #b = int(input())
    #print("What is the hypo?") #Get full word for "c"
    #c = int(input())
    b = int(what("height"))
    c = int(what("Hypotenuse"))
    a = math.sqrt((c*c)-(b*b))
    if working:
        print("Base: sqrt(("+str(c)+" x "+str(c)+") + ("+str(b)+" * "+str(b)+")) = "+a+" Units")
    #print str(a)
    tri(a,b,c)
	
def tri(a,b,c):
    global working
    if working:
        print("Permieter: "+str(a)+" + "+str(b)+" + "+str(c)+" = "+str(a+b+c)+" Units")
        print("Area:      "+"0.5 x ("+str(a)+" x "+str(b)+" = "+str(0.5*(a*b))+" Square Units")
    else:
        print("Perimeter:  " + str(a+b+c) + " Units")
        area = 0.5*(a*b)
        print("Area:      " + str(area) + " Square Units")
    print("Base:       " + str(a) + " Units")
    print("Height:     " + str(b) + " Units")
    print("Hypotenuse: " + str(c) + " Units")

def hex():
    length = int(what("legth of a side"))
    if working:
        print("Perimeter: "+str(length)+" x 6 = "+ str(length*6) +" Units")
        
    
#(length of 1 side)2 x 2.6

#def what(after): #Original
#    print("What is the " + after + "?")
#    return raw_input("> ")

def what(after): #Second one
    print("What is the " + after + "?")
    #return a = raw_input("> ") if a != "q" else sys.exit(0)
    input = raw_input("> ")
    if input != "q":
        return input
    else:
        sys.exit(0)

def rounder2(input):
    input *= 100
    if input-int(input) < 0.5:
        return (math.floor(input))/100
    else:
        return (math.ceil(input))/100
        
#if __name__ == '__main__':
#    input = what("day today")
#    print("The day is apparently " + input + " :D")
#    print what("problem")
    
menu()

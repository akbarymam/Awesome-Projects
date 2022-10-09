#purpose: to frind the distance betwen two points on a graph
#updates:
    #1. 2022-10-04 08:58:28 : Started this project
    #2. 


# the distance formula on a x and y (2d graph) axis is 
#       distance = ((x2 - x1)wholeSq + (y2 - y1)wholeSq)WholeRoot 

#to get the coordinates of x1 and y1
from math import sqrt

print("----------------")
print("created by: ")
print("https://github.com/ChefYeshpal")
print("for: hacktober")
print("----------------")

print("welcome to my attempt to create a program that would find the distance between two points on a graph which contains x and y axis")
print("----------------")
x1 = int(input("please enter the coordinates of x1: "))
y1 = int(input("please enter the coordinates of y1: "))
print("----------------")

#to get the coordinates of x2 and y2
x2 = int(input("please enter the coordinates of x2: "))
y2 = int(input("please enter the coordinates of y2: "))
print("----------------")
#applying distance formula
c = (((x2 - x1)**2) + ((y2 - y1)**2)) 
d = sqrt(c)

print("the distance between the two points is ", d)
print("----------------")
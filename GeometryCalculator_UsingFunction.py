# Name:                      Geometry Calculaytor
# Author:                    Yunfeng Lin   
# Date Created:              Janurary 31, 2023
# Date Last Modified:        February 6, 2023

'''
1. Receive user's input for each Circle, Rectangle and Triangel.
2. Prompt user to input the Radius, width and length of each shape.
3. Calculate the area and perimeter of each shape by using function.
4. Display the result on the terminal/consol.
5. Whenever completing one of the calculation, ask the initial question again.
6. If the user enters [4. Quit], stop loop and no more asking the initial question.

'''

import math # To calculate the triangle area and perimeter.

def circle(radiUs):
    circleArea = radiUs * radiUs * 3.14 
    circlPerimeter = radiUs * 2 * 3.14
    print("The area of the circle is " + str(circleArea) + " square cm","Perimeter of the circle is " + str(circlPerimeter) + " cm",sep="\n")

def rectangle(rectangleWidth , rectangleLength):
    rectangleArea = rectangleWidth * rectangleLength
    rectanglePerimeter = 2 * (rectangleWidth + rectangleLength)
    print("The area of the Rectangle is " + str(rectangleArea) + " square cm","Perimeter of the Rectangle is " + str(rectanglePerimeter) + " cm",sep="\n")

def Triangle(triangle_Side):
    triangle_Area = (math.sqrt(3)/4) * (triangle_Side * triangle_Side)
    triangle_Perimeter = 3 * triangle_Side
    print("The area of the Equilateral Triangle is " + str(triangle_Area) + " square cm","Perimeter of the Triangle is " + str(triangle_Perimeter) + " cm",sep="\n")

while True:

    print("\n\tGeomatric calculator","\n\n1. Calculate the area and perimeter of a Circle.","2. Calculate the area and perimeter of a Rectangle.","3. Calculate the area and perimeter of a Triangle.","4. Quit.",sep="\n")
    num = int(input("Enter your choice (1-4):")) # Receive input of the user from the option 1 - 4. 
    if num == 1: # if the user choses number 1, then do the following.
        print("Enter radius of the Circle(cm):")
        radiUs = float(input()) # Convert the input value into float and store it to the variable [radiUs].
        circle(radiUs) # Calling the function and pass the input value to the function.


    elif num == 2:
        print("Enter width of Rectangle(cm):")
        rectangleWidth = float(input()) # Convert the input value into float and store it to the variable [rectangleWidth].
        print("Enter length of Rectangle(cm):")
        rectangleLength = float(input()) # Convert the input value into float and store it to the variable [rectangleLength].
        rectangle(rectangleWidth , rectangleLength) # Calling the function and pass the input value to the function.

    
    elif num == 3:
        print("Enter the length of the side:")
        triangle_Side = float(input()) # Convert the input value into float and store it to the variable [triangle_Side].
        Triangle(triangle_Side) # Calling the function and pass the input value to the function.


    elif num == 4:
        print("Quit")
        break # If the user enters number 4, stop loop and no more asking the initial question.
   
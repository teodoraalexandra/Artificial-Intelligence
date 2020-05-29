#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:19:14 2020

@author: teodoradan
"""
import numpy as np
import random
import math
import copy

"""
START SUDOKU
"""

def getEmpty(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == 0:
                return [i, j]
    return [-1,-1]

def checkSquare(A, iStart, jStart, iStop, jStop):
    #function that verifies if the values in the given square are unique
    found = []
    for i in range(iStart, iStop):
        for j in range(jStart, jStop):
            if A[i][j] != 0 and A[i][j] in found:
                return False
            found.append(A[i][j])
    return True

def getSquare(A):

    n = len(A) #first example: 4
    sqn = int(math.sqrt(n)) #first example: 2
    for i in range (0, n, sqn):
        for j in range (0, n, sqn):
            #first example: generate squares of size 2x2
            if checkSquare(A, i, j, i + sqn-1, j + sqn -1) == False:
                return False
    return True

def validate(A):
    #check each row
    for row in A:
        appear = []
        for i in range(len(row)):
            if row[i] != 0 and row[i] in appear:
                return False
            if row[i] != 0:
                appear.append(row[i])
    
    #check each column
    for i in range (len(A)):
        appear2 = []
        for j in range (len(A)):
            if A[j][i] in appear2:
                return False
            if A[j][i] != 0:
                appear2.append(A[j][i])
                
    return getSquare(A)

def sudoku(A):
    #take input from the user:
    n = int(input("Insert the maximum number of trials: "))
    
    B = copy.deepcopy(A)
    
    print("The input matrix:\n")
    print(A, "\n")
    
    print(validate(A))
    i = 1
    found = False
    
    while i <= n:
        a = np.random.randint(low = 1, high = 5, size = 1)
        [row, col] = getEmpty(B)
        
        
        if row == -1: #all the positions have been occupied
            print("Solution found!: ")
            print(B)
            print("Total attempts: ", i)
            found = True
            break
        else:
            #if the solution is incorrect, reset B to the initial matrix and start generating random numbers again
            B[row][col] = a
            if validate(B) == False:
                B = copy.deepcopy(A)
                i += 1
    
    if found == False:            
        print("Sorry, no solution could be found!")
       
    
def main_sudoku():
    A = np.loadtxt("sudoku4x4.txt")
    B = np.loadtxt("sudoku9x9.txt")
    
    option = input("Press A for a 4x4 sudoku or B for a 9x9 sudoku: ");
    if (option == "A"):
        print(A)
        sudoku(A)
    elif (option == "B"):
        print(B)
        sudoku(B)
    else:
        print("Invalid option.")
        
"""
END SUDOKU
"""
    
"""
START CRYPTO
"""  
def genericSolution(equation, solution):
    split1 = equation.split("=")
    rhs = split1[1] #here we have the right hand side
    if (solution[rhs[0]] == 0):
        return False
    rhs_crypto = ""
    for letter in rhs:
        for key in solution:
            if(letter == key):
                rhs_crypto += str(solution[key])
                
    lhs = split1[0] #A+B+C
    if (lhs.find("-")):
        data = lhs.split("-")
        operator = "-"
        eq = ""
        for item in data:
            if (solution[item[0]] == 0):
                return False
            for letter in item:
                for key in solution:
                    if (letter == key):
                        eq += str(solution[key]) 
            eq += operator
        eq = eq[:-1]
        print(eq, "=", rhs_crypto)
        return (eq == rhs_crypto)
    
def isCryptSolution(equation, solution, operator):
    #{"S": 9, "E": 5, "N": 6, "D": 7, "M": 1, "O": 0, "R": 8, "Y": 2}
    #{'E': 8, 'A': 1, 'T': 9, 'H': 2, 'P': 0, 'L': 3} 
    #{'N': 9, 'E': 3, 'V': 5, 'R': 6, 'D': 8, 'I': 7} 
    
    split1 = equation.split(operator)
    first = split1[0] #first <- SEND
    
    if (solution[first[0]] == 0):
        return False
    
    split2 = split1[1].split("=")
    second = split2[0] #second <- MORE
    if (solution[second[0]] == 0):
        return False
    third = split2[1] #third <- MONEY
    if (solution[third[0]] == 0):
        return False
    
    #we should have number_1 as SEND decrypted: 9567
    number_1 = ""
    for letter in first:
        for key in solution:
            if (letter == key):
                number_1 += str(solution[key])
                
    #we should have number_2 as MORE decrypted: 1085
    number_2 = ""
    for letter in second:
        for key in solution:
            if(letter == key):
                number_2 += str(solution[key])
    
    #we should have number_3 as MONEY decrypted: 10652
    number_3 = ""
    for letter in third:
        for key in solution:
            if(letter == key):
                number_3 += str(solution[key])
    
    if (operator == "+" and int(number_1) + int(number_2) == int(number_3)):
        return True
    if (operator == "-" and int(number_1) - int(number_2) == int(number_3)):
        return True
    return False

def generate_solution(letters):
    dict = {}
    digits = [0,1,2,3,4,5,6,7,8,9]
    for letter in letters:
        random_digit = random.choice(digits)
        dict[letter] = random_digit
        digits.remove(random_digit)
    return dict

def generate_letters(equation):
    letters = []
    operators = ["+", "-", "="]
    i = 0
    while i < len(equation):
        if equation[i] in letters or equation[i] in operators:
            i += 1
        else:
            letters.append(equation[i])
            i +=1
    return letters
        
def main_crypto():
    print("1. SEND+MORE=MONEY")
    print("2. EAT+THAT=APPLE")
    print("3. NEVER-DRIVE=RIDE")
    f = open("crypto.txt", "r")
    equations = f.read().splitlines()
    f.close()

    option = int(input("What puzzle do you want? "))
    if (option == 1):
        #we read from file the actual equation
        equation = equations[option - 1]
        #we generate a random solution
        solution = generate_solution(generate_letters(equation))
        #we create an operator
        operator = "+"
    
    elif (option == 2):
        #we read from file the actual equation
        equation = equations[option - 1]
        #we generate a random solution
        solution = generate_solution(generate_letters(equation))
        #we create an operator
        operator = "+"
        
    elif (option == 3):
        #we read from file the actual equation
        equation = equations[option - 1]
        #we generate a random solution
        solution = generate_solution(generate_letters(equation))
        #we create an operator
        operator = "-"
    else:
        print("Invalid option.")
        
    
    n = int(input("Insert maximum number of trials: "))
    i = 1
    found = False
    while i <= n:
    #while (found == False):
        copy_equation = equation
        if(isCryptSolution(copy_equation, solution, operator)): 
            print("This is a solution: ", solution)
            found = True
            break
        else:
            solution = generate_solution(generate_letters(equation))
            i += 1
    if (found == False):
        print("No solution could be found.")
    
"""
END CRYPTO
"""
    
"""
START GEOMETRIC
"""
def insertShape(table, shape, i, j):
    #insert the shape to the table
    for i_shape in range(len(shape)):
        for j_shape in range(len(shape[i_shape])):
            table[i + i_shape][j + j_shape] += shape[i_shape][j_shape]
            
def fits(table, shape, i, j):
    #We want to check if the shape fits into the table, starting table[i,j] position
    
    #return false if the row position + the length of shape exceed the table
    if i + len(shape) > 5:
        return False
    
    
    if len(shape) == 1:
        #check the liniar shape (arrays of size 1)
        if i > 5 or j + len(shape[0]) >= 6:
            return False
        else:
            for j_shape in range(len(shape[0])):
                #it is suficient for one position from the table to be non-empty 
                #non-empty = a non-zero number 
                #so, as the shape is valid (number), and one position from table is non-empty,
                #their multiplication will lead to a result different than 0 -> return False. 
                if shape[0][j_shape] * table[i][j + j_shape] != 0:
                    return False
            return True
    else:
        #check the nonlinear shapes
        for row in shape:
            if j + len(row) > 6:
                return False
            
    #check for any overlaps
    for i_shape in range(len(shape)):
        for j_shape in range (len(shape[i_shape])):
            #this approach is similar with the one explained above
            if shape[i_shape][j_shape] * table[i + i_shape][j + j_shape] != 0:
                return False
    return True

def compatiblePos(table, shape):
    positions = []
    for i in range(len(table)):
        for j in range (len(table[i])):
            if fits(table, shape, i, j):
                positions.append((i,j))
    return positions

def getShapes():
    sh1 = np.array([[1,1,1,1]], dtype = int)
    sh2 = np.array([[2,2,2]],  dtype = int)
    sh3 = np.loadtxt("shape3.txt", dtype = int)
    sh4 = np.loadtxt("shape4.txt", dtype = int)
    sh5 = np.loadtxt("shape5.txt", dtype = int)
    sh6 = np.loadtxt("shape6.txt", dtype = int)
    sh7 = np.loadtxt("shape7.txt", dtype = int)
    sh8 = np.array([[8],[8]], dtype = int)
    
    shp = []
    shp.append(sh1)
    shp.append(sh2)
    shp.append(sh3)
    shp.append(sh4)
    shp.append(sh5)
    shp.append(sh6)
    shp.append(sh7)
    shp.append(sh8)
    
    return shp

def main_geometric():
    table = np.zeros((5,6),  dtype = int)
    n = int(input("Insert maximum number of trials: "))
    i = 1 
    while i <= n:
        #create the 5x6 board
        table = np.zeros((5,6),  dtype = int)
        #get the geometric forms from Figure 5
        shapes = getShapes()
        
        while(len(shapes) != 0):
            found = False
            #generate a random index from 0 to len(shapes) -> basically get one random shape
            currentShapeIndex = np.random.randint(0, len(shapes))
            currentShape = shapes.pop(currentShapeIndex)
            
            positions = compatiblePos(table, currentShape)
            
            if len(positions) == 0:
                #we don't find a position in table in i-th aproach, so we go on
                i += 1
                break
            else: 
                #we find at least one valid position -> generate one random position from list
                positionIndex = np.random.randint(0, len(positions))
                currentPosition = positions.pop(positionIndex)
                
                #in currentPosition we have pair of (i, j)
                insertShape(table, currentShape, currentPosition[0], currentPosition[1])
                found = True
                
            
        if len(shapes) == 0 and found == True:
            print("Solution found: ")
            print(table)
            print("Number of trials: ", i)
            return
    
    print("No solution could be found!")
    print("Last attempt resulted in: ")
    print(table)
    return
"""
END GEOMETRIC
"""

def run():
    print("Menu:\n")
    print("1. Sudoku game")
    print("2. Cryptarithmetic game")
    print("3. Geometric forms")
    print("0. Exit\n")
    option = int(input("What game would you like? "))
    
    while (option != 0):
        if option == 1:
            main_sudoku()
            option = int(input("What game would you like? "))
        elif option == 2:
            main_crypto()
            option = int(input("What game would you like? "))
        elif option == 3:
            main_geometric()
            option = int(input("What game would you like? "))
        else:
            option = int(input("Wrong number. Enter again: "))
            
run()
        
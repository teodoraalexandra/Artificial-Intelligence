#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:05:55 2020

@author: teodoradan
"""


import random
from itertools import permutations
import numpy as np


class Ant:
    def __init__(self, problem):
        self.__problem = problem
        self.__sizeOfPath = self.__problem.getPathLength()
        
        #path of each ant is of size nxn and is full of zeros, initially
        self.__path = []
        for i in range(self.__problem.getPathLength()):
            self.__path.append(0)
            
        self.__moves = []

    def __len__(self):
        return len(self.__path)
    
    def getPath(self):
        return self.__path

    def fitness(self, individual):
        vmax = self.__problem.getSizeOfMatrix()
        
        # start from 1 to avoid making a division by 0
        f = 1
        suma = (vmax * (vmax + 1)) / 2

        first_row = []
        second_row = []
        for row in range(vmax):
            for column in range(vmax):
                element = individual[row][column]
                first_row.append(element[0])
                second_row.append(element[1])
            if sum(first_row) == suma:
                f += 1
            if sum(second_row) == suma:
                f += 1
            first_row = []
            second_row = []

        first_column = []
        second_column = []
        for column in range(vmax):
            for row in range(vmax):
                element = individual[row][column]
                first_column.append(element[0])
                second_column.append(element[1])
            if sum(first_column) == suma:
                f += 1
            if sum(second_column) == suma:
                f += 1
            first_column = []
            second_column = []

        return f

    def calculateDistance(self, next):
        # (after we add next in path)
        # return an empiric distance given by the number of the possible correct moves
        
        ant = Ant(self.__problem)
        ant.__path = self.__path.copy()
        
        for i in range(len(ant.__path) - 1):
            if (i == 0):
                ant.__path[i] = next
              
        res = 0
        for i in ant.__path:
            if (i == 0):
                res += 1
                
        return res
    
    def computePermutations(self):
        """
        The list of permutation we will shuffle later in the individual

        :return: the list of all possible permutations
        """
        
        vmin = 1
        vmax = self.__problem.getSizeOfMatrix()

        listOfPossibleNumbers = []
        for i in range(vmin, vmax + 1):
            listOfPossibleNumbers.append(i)

        perm = permutations(listOfPossibleNumbers, 2)
        allPermutations = []

        # Compute the arrangements
        for i in list(perm):
            allPermutations.append(i)

        # Add to allPermutations list, the duplicate tuples
        for i in listOfPossibleNumbers:
            miniList = (i, i)
            allPermutations.append(miniList)
        return allPermutations

    def nextMoves(self):
        moves = self.computePermutations()
        return moves

    def update(self, traceMatrix, alpha, beta, q0):
        p = [0 for i in range(self.__problem.getPathLength())]

        nextMoves = self.nextMoves()
    
        index = 0
        for i in nextMoves:
            p[index] = self.calculateDistance(i)
            index += 1
            
        r = [ (p[i] ** beta) for i in range(len(p))]
        while len(nextMoves) > 0:
            rnd1 = random.random()
            if rnd1 < q0:
                r = [[i, self.calculateDistance(i)] for i in nextMoves]
                r = max(r, key=lambda a: a[1])
                index = -1
                for i in self.__path:
                    index += 1
                    if (i == 0):
                        self.__path[index] = r[0]
                        
                nextMoves.remove(r[0])
            else:
                s = sum(p)
                if s == 0:
                    return random.choice(nextMoves)
                p = [p[i] / s for i in range(len(p))]
                p = [sum(p[0: i + 1]) for i in range(len(p))]
                rnd2 = random.random()
                i = 0
                while rnd2 > p[i]:
                    i += 1
                    
                index = -1
                for elem in self.__path:
                    index += 1
                    if (elem == 0) and (len(nextMoves) > 0):
                        aleatoriu = random.choice(nextMoves)
                        self.__path[index] = aleatoriu
                        nextMoves.remove(aleatoriu)
                
        return self.__path
    
    def chunkIt(self, path, size):
        #split the path of size nxn in n smallest lists ->  create a matrix
        
        avg = len(path) / float(size)
        out = []
        last = 0.0
    
        while last < len(path):
            out.append(path[int(last):int(last + avg)])
            last += avg
    
        return out

    def prettyPrint(self):
        matrix = self.chunkIt(self.__path, self.__problem.getSizeOfMatrix())
        for row in matrix:
            for item in row:
                print (item, " ", end='')
            print ("\n")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:54:55 2020

@author: teodoradan
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from chromozomePopulation import ChromozomePopulation
from chromozome import Chromozome
from particlePopulation import ParticlePopulation
from particle import Particle
from problem import Problem
from prettytable import *
import time


class Controller:
    def __init__(self, problem):
        self.__n = problem.getSize()

    def ParticleSwarmOptimization(self, noIteratii, dimPopulation, vmin, vmax, w, c1, c2, sizeOfNeighborhood):
        P = ParticlePopulation(dimPopulation, vmin, vmax)

        # we establish the particles' neighbors
        neighborhoods = P.selectNeighbors(sizeOfNeighborhood)

        for i in range(noIteratii):
            P.iteration(neighborhoods, c1, c2, w / (i + 1))

        # get the best individual
        graded = [(x.fitness(x), x) for x in P.getPopulation()]
        graded = sorted(graded, key=lambda x: x[0])
        # in graded we keep pairs of fitness and individual -> result store the best individual
        # we take the last individual, because it has the greatest fitness score
        result = graded[len(graded) - 1]
        fitnessOptim = result[0]
        individualOptim = result[1]

        return individualOptim, fitnessOptim

    def EvolutionaryAlgorithm(self, noIteratii, dimPopulation, vmin, vmax, pM):
        P = ChromozomePopulation(dimPopulation, vmin, vmax)
        c = Chromozome(vmin, vmax)
        print ("I am going to print the best solutions found: \n")
        for i in range(noIteratii):
            c = P.iteration(pM)
            print (c.outputFormat())
            print ("\n")
            time.sleep(0.5)
            
        # get the best individual
        graded = [(P.fitness(x, vmax), x) for x in P.getPopulation()]
        graded = sorted(graded, key=lambda x: x[0])
        # in graded we keep pairs of fitness and individual -> result store the best individual
        # we take the last individual, because it has the greatest fitness score
        result = graded[len(graded) - 1]
        fitnessOptim = result[0]
        individualOptim = result[1]

        return individualOptim.outputFormat(), fitnessOptim
    
    

    def HillClimbing(self, n):
        p = Problem(n)
        queue = p.getMatrix()
        listOfPermutations = p.getListOfPermutations()
        print ("I am going to print the best solution found: ")

        possible_solution = []
        row = 1
        while queue:
            row_state = queue.pop()

            next_state, listOfPermutations = p.expand(row_state, listOfPermutations, row)
            possible_solution.append(next_state)
            
            print (possible_solution)
            time.sleep(0.5)
        
            row += 1

        fitnessOptim = p.fitness(possible_solution, n)
        p = PrettyTable()
        for row in possible_solution:
            p.add_row(row)
        pretty = p.get_string(header=False, border=False)

        return pretty, fitnessOptim

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:55:49 2020

@author: teodoradan
"""


from problem import Problem
from controller import Controller
from chromozomePopulation import ChromozomePopulation
from particlePopulation import ParticlePopulation
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count
import pandas as pd
import statistics

        
def printMainMenu():
    s = ''
    s += "0 - exit \n"
    s += "1 - find solution using Evolutionary algorithm \n"
    s += "2 - find solution using Hill Climbing\n"
    s += "3 - find solution using Particle Swarm Optimization"
    print(s)


class UI:
    def __init__(self, n):
        self.__problem = Problem(n)
        self.__controller = Controller(self.__problem)
        self.__eaAverage = []
        self.__psoAverage = []

    def particleSwarmOptimization(self):
        startClock = time()
        noIteratii = int(input("Enter the number of iterations = "))
        dimPopulation = int(input("Enter the dimension of the population = "))

        # numbers for permutations will be in interval [1, n]
        vmin = 1
        vmax = n
        # maximum fitness possible
        maximumFitness = 4 * vmax

        # specific parameters for PSO
        w = 1.0
        c1 = 1.
        c2 = 2.5
        sizeOfNeighborhood = 20

        optimIndividual, fitnessOptim = self.__controller.ParticleSwarmOptimization(noIteratii, dimPopulation, vmin, vmax, w, c1, c2, sizeOfNeighborhood)
        print ('Result: The detected matrix after ', noIteratii, ' iterations is: ')
        print(optimIndividual)
        print (' with fitness optim = ', fitnessOptim, '/', maximumFitness)
        print('execution time = ', time() - startClock, " seconds")

    def animate_EA(self, x_vals, y_vals, index, r):
        population = 40
        P = ChromozomePopulation(population, 1, n) #population = 40
        pop = P.getPopulation()
         
        r = random.randrange(1, 40)
        x_vals.append(next(index))
        y_vals.append(P.fitness(pop[r], n))
        self.__eaAverage.append(P.fitness(pop[r], n))
        
        plt.cla()
        plt.plot(x_vals, y_vals)
        plt.show()
        
    def animate_PSO(self, x_vals, y_vals, index, r):
        population = 40
        P = ParticlePopulation(population, 1, n) #population = 40
        pop = P.getPopulation()
         
        r = random.randrange(1, 40)
        particle = pop[r]
        x_vals.append(next(index))
        y_vals.append(particle.fitness(particle))
        self.__psoAverage.append(particle.fitness(particle))
        
        plt.cla()
        plt.plot(x_vals, y_vals)
        plt.show()
            
    def statisticsEvolutionaryAlgorithm(self, n):
        plt.style.use('fivethirtyeight')
        
        x_vals = []
        y_vals = []
        
        index = count()
        
        for run in range(30): #run = 30
            r = random.randrange(1, 40)
            #evaluation = 1000 (interval)
            FuncAnimation(plt.gcf(), self.animate_EA(x_vals, y_vals, index, r), interval = 1000)
        
        plt.tight_layout()
        
        #average display for best solution
        sum_num = 0
        for t in self.__eaAverage:
            sum_num = sum_num + t           

        avg = sum_num / len(self.__eaAverage)
        print ("Average of fitness score is: ", avg)
        
        #standard deviation display for best solution
        deviation = statistics.stdev(self.__eaAverage)
        print ("Standard deviation of fitness score is: ", deviation)
        
    def statisticsParticleSwarmOptimization(self, n):
        plt.style.use('fivethirtyeight')
        
        x_vals = []
        y_vals = []
        
        index = count()
        
        for run in range(30): #run = 30
            r = random.randrange(1, 40)
            #evaluation = 1000 (interval)
            FuncAnimation(plt.gcf(), self.animate_PSO(x_vals, y_vals, index, r), interval = 1000)
        
        plt.tight_layout()
        
        #average display for best solution
        sum_num = 0
        for t in self.__psoAverage:
            sum_num = sum_num + t           

        avg = sum_num / len(self.__psoAverage)
        print ("Average of fitness score is: ", avg)
        
        #standard deviation display for best solution
        deviation = statistics.stdev(self.__psoAverage)
        print ("Standard deviation of fitness score is: ", deviation)
        
    def evolutionaryAlgorithm(self):
        startClock = time()
        noIteratii = int(input("Enter the number of iterations = "))
        dimPopulation = int(input("Enter the dimension of the population = "))

        # numbers for permutations will be in interval [1, n]
        vmin = 1
        vmax = n

        # the mutation probability
        pM = float(input("Enter the mutation probability = "))
        # maximum fitness possible
        maximumFitness = 4 * vmax

        optimIndividual, fitnessOptim = self.__controller.EvolutionaryAlgorithm(noIteratii, dimPopulation, vmin, vmax, pM)
        print ('Result: The detected matrix after ', noIteratii, ' iterations is: ')
        print(optimIndividual)
        print (' with fitness optim = ', fitnessOptim, '/', maximumFitness)
        print('execution time = ', time() - startClock, " seconds")

    def hillClimbing(self):
        startClock = time()
        # maximum fitness possible
        maximumFitness = 4 * n

        optimIndividual, fitnessOptim = self.__controller.HillClimbing(n)
        print ('Result: The detected matrix is: ')
        print(optimIndividual)
        print (' with fitness optim = ', fitnessOptim, '/', maximumFitness)
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        runM = True
        printMainMenu()
        while runM:
            command = int(input(">>"))
            if command == 0:
                runM = False
            elif command == 1:
                self.statisticsEvolutionaryAlgorithm(n)
                #self.evolutionaryAlgorithm()
            elif command == 2:
                self.hillClimbing()
            elif command == 3:
                self.statisticsParticleSwarmOptimization(n)
                #self.particleSwarmOptimization()
            else:
                print ("Invalid command")


n = int(input("Enter the size of the matrix >> "))
ui = UI(n)
ui.run()


# TO DO:
# GUI 
# integrate statistics nicely :)

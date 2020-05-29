#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:06:54 2020

@author: teodoradan
"""


from controller import Controller
from problem import Problem
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
import random
import statistics

acoAverage = []

def animate_ACO(x_vals, y_vals, index, r):
        #statistics are made on a 3x3 matrix -> path is of size 9
        pheromoneMatrix = [[1 for i in range(9)] for j in range(9)]
        
        for i in range(30): 
            solution, fitness = controller.epoch(pheromoneMatrix)
            x_vals.append(next(index))
            y_vals.append(fitness)
            
            acoAverage.append(fitness)
        
            plt.cla()
            plt.plot(x_vals, y_vals)
            plt.show()

def statisticsAntColonyOptimization(n):
        plt.style.use('fivethirtyeight')
        
        x_vals = []
        y_vals = []
        
        index = count()
        
        r = random.randrange(1, 40)
        FuncAnimation(plt.gcf(), animate_ACO(x_vals, y_vals, index, r), interval = 1000)
        
        plt.tight_layout()
        
        #average display for best solution
        sum_num = 0
        for t in acoAverage:
            sum_num = sum_num + t           

        avg = sum_num / len(acoAverage)
        print ("Average of fitness score is: ", avg)
        
        #standard deviation display for best solution
        deviation = statistics.stdev(acoAverage)
        print ("Standard deviation of fitness score is: ", deviation)

if __name__ == '__main__':
    problem = Problem("size.txt")
    controller = Controller("parameters.txt", problem)
    
    #STATISTICS ARE FOR A 3x3 MATRIX
    option = input("Wanna see some statistics first? [y/n] >> ")
    if (option == "y"):
        statisticsAntColonyOptimization(3)
    elif (option == "n"):
        pheromoneMatrix = [[1 for i in range(problem.getPathLength())] for j in range(problem.getPathLength())]
        #print(pheromoneMatrix) 
        
        print("Computing solution ... ")
        print("\n")
        
        solution = []
        best_ant = None
        fitness = 0
        bestFitness = 0
        for i in range(controller.getNoEpoch()): 
            solution, fitness = controller.epoch(pheromoneMatrix)
            
            if best_ant == None and bestFitness == 0:
                best_ant = solution
                bestFitness = fitness
            if bestFitness < fitness:
                best_ant = solution
                bestFitness = fitness
        
        best_ant.prettyPrint()
        print("Having fitness: ", bestFitness - 1)
    else:
        print("Invalid option.")

    
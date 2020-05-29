#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:44:41 2020

@author: teodoradan
"""


from chromosome import Chromosome
from population import Population
from random import choice

f = open("input.in", "r")
EPSILON = int(f.readline())
f.close()
with open("training.in", "r") as f:
    HEADER = f.readline().split(',')


class Controller:
    def __init__(self, nrInd, input_data, output_data, inputTrain, outputTrain, inputTest, outputTest):
        self.n = 0
        self.input = input_data
        self.output = output_data
        self.inputTest = inputTest
        self.outputTest = outputTest
        self.inputTrain = inputTrain
        self.outputTrain = outputTrain
        self.nrInd = nrInd
        self.population = Population(nrInd, inputTrain, outputTrain)
        self.probability_mutate = 0.2
        self.probability_crossover = 0.8

    def run(self):
        self.population.evaluate(self.inputTrain, self.outputTrain)
        
        best_fitness = 999999
        i = 1
        f = open("output.out", "w")

        while (best_fitness > EPSILON):
            print("\n")
            f.write("\n")
            print("Iteration: " + str(i))
            f.write("Iteration: " + str(i) + "\n")
            self.iteration()
            self.population.evaluate(self.inputTrain, self.outputTrain)
            self.population.selection(self.nrInd)
            best = self.population.best(1)[0]
            best_fitness = float(best.fitness)
            print( "Best: " + str(best.root) + "\n" + "fitness: " + str(best_fitness) + "\n" )
            f.write("Best: " + str(best.root) + "\n" + "fitness: " + str(best_fitness) + "\n")
            i += 1
        
        f.close()

    def iteration(self):
        parents = range(self.nrInd)
        nrChildren = len(parents) // 2
        offspring = Population(nrChildren, self.inputTrain, self.outputTrain)

        # __str__ of population return the chromosomes fitness
        for i in range(nrChildren):
            offspring.individuals[i] = Chromosome.crossover(choice(self.population.individuals),
                                                            choice(self.population.individuals),
                                                            self.inputTrain,
                                                            self.outputTrain)
            offspring.individuals[i].mutate(self.probability_mutate)
        offspring.evaluate(self.inputTrain, self.outputTrain)
        self.population.reunion(offspring)
        self.population.selection(self.nrInd)

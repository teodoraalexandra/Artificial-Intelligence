#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:53:08 2020

@author: teodoradan
"""

from random import randint, random, choice
from chromozome import Chromozome
import time

class ChromozomePopulation:
    """
    Create a number of individuals (i.e. a population).

    dimPopulation: the number of individuals in the population
    vmin: the minimum possible value
    vmax: the maximum possible value
    """

    def __init__(self, dimPopulation, vmin, vmax):
        self.__population = [Chromozome(vmin, vmax) for x in range(dimPopulation)]
        self.__dimPopulation = dimPopulation
        self.__vmin = vmin
        self.__vmax = vmax

    def getPopulation(self):
        return self.__population

    def fitness(self, individual, vmax):
        """
        Determine the fitness of an individual. Higher is better.
        For each individual, which is a matrix, we compute its fitness score
        Fitness score is initially 0.
        As we parse the rows, if numbers are correctly placed, we increase fitness with 1. Maximum here is 2 * vmax
        As we parse the columns, if numbers are correctly placed, we increase fitness with 1. Maximum here is 2 * vmax.
        The optimal solution should have a fitness score of 4 * vmax

        individual: the individual to evaluate
        """
        f = 0
        suma = (vmax * (vmax + 1)) / 2

        first_row = []
        second_row = []
        for row in range(vmax):
            for column in range(vmax):
                element = individual.getElement(row, column)
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
                element = individual.getElement(row, column)
                first_column.append(element[0])
                second_column.append(element[1])
            if sum(first_column) == suma:
                f += 1
            if sum(second_column) == suma:
                f += 1
            first_column = []
            second_column = []

        return f

    def mutate(self, individual, pM, vmin, vmax):
        """
        Performs a mutation on an individual with the probability of pM.
        If the event will take place, we swap two positions from the individual, all randomly

        individual:the individual to be mutated
        pM: the probability the mutation to occure
        vmin: the minimum possible value
        vmax: the maximum possible value
        """

        auxiliary = Chromozome(self.__vmin, self.__vmax)
        auxiliary.deleteMaterial()

        if pM > random():
            noOfMutationPerIndividual = randint(1, vmax * vmax)
            while noOfMutationPerIndividual != 0:
                row = randint(vmin - 1, vmax - 1)
                column = randint(vmin - 1, vmax - 1)
                row_mutated = randint(vmin - 1, vmax - 1)
                column_mutated = randint(vmin - 1, vmax - 1)
                # algorithm of swapping
                auxiliary.setElement(row, column, individual.getElement(row, column))
                individual.setElement(row_mutated, column_mutated, individual.getElement(row, column))
                individual.setElement(row, column, auxiliary.getElement(row, column))
                noOfMutationPerIndividual -= 1

        return individual

    def crossover(self, parent1, parent2):
        """
        crossover between 2 parents
        child will inherit (randomly), step by step, each of the parents elements
        """
        child = []
        rows_of_child = []

        for i in range(len(parent1)):
            for j in range(len(parent1)):
                # take every element by each parent, and offer the opportunity for child to choose (randomly, ofc) :)
                element_1 = parent1.getElement(i, j)
                element_2 = parent2.getElement(i, j)
                inheritance = choice([element_1, element_2])
                rows_of_child.append(inheritance)
            child.append(rows_of_child)
            rows_of_child = []

        c = Chromozome(self.__vmin, self.__vmax)
        c.addMaterial(child)
        return c

    def iteration(self, pM):
        """
        an iteration

        pop: the current population
        pM: the probability the mutation to occure
        vmin: the minimum possible value
        vmax: the maximum possible value
        """
        i1 = randint(0, len(self.__population) - 1)
        i2 = randint(0, len(self.__population) - 1)
        c = Chromozome(self.__vmin, self.__vmax)
        if i1 != i2:
            c = self.crossover(self.__population[i1], self.__population[i2])
            c = self.mutate(c, pM, self.__vmin, self.__vmax)
            f1 = self.fitness(self.__population[i1], self.__vmax)
            f2 = self.fitness(self.__population[i2], self.__vmax)
            '''
            the repeated evaluation of the parents can be avoided
            if  next to the values stored in the individuals we 
            keep also their fitnesses 
            '''
            fc = self.fitness(c, self.__vmax)
            if (f1 < f2) and (f1 < fc):
                self.__population[i1] = c
            if (f2 < f1) and (f2 < fc):
                self.__population[i2] = c
        return c

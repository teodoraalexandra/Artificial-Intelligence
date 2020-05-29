#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:55:20 2020

@author: teodoradan
"""


from particle import Particle
from random import randint, random


class ParticlePopulation:
    """
    Create a number of individuals (i.e. a population).

    dimPopulation: the number of individuals in the population
    vmin: the minimum possible value
    vmax: the maximum possible value
    """

    def __init__(self, dimPopulation, vmin, vmax):
        self.__population = [Particle(vmin, vmax) for x in range(dimPopulation)]
        self.__dimPopulation = dimPopulation
        self.__vmin = vmin
        self.__vmax = vmax

    def __len__(self):
        return len(self.__population)

    def getElement(self, i):
        return self.__population[i]

    def getPopulation(self):
        return self.__population

    def selectNeighbors(self, sizeOfNeighborhood):
        """  the selection of the neighbours for each particle

        input --
           pop: current population
           sizeOfNeighborhood: the number of neighbours of a particle

        output--
           ln: list of neighbours for each particle
        """

        if sizeOfNeighborhood > len(self.__population):
            sizeOfNeighborhood = len(self.__population)

        neighbors = []
        for i in range(len(self.__population)):
            localNeighbor = []
            for j in range(sizeOfNeighborhood):
                nr = randint(0, len(self.__population) - 1)
                x = self.__population[nr]
                while x in localNeighbor:
                    nr = randint(0, len(self.__population) - 1)
                    x = self.__population[nr]
                localNeighbor.append(x)
            neighbors.append(localNeighbor)
        return neighbors

    def iteration(self, neighbors, c1, c2, w):
        """
        an iteration

        pop: the current state of the population


        for each particle we update the velocity and the position
        according to the particle's memory and the best neighbor's pozition
        """
        bestNeighbors = []

        # determine the best neighbor for each particle

        for i in range(len(self.__population)):
            bestNeighbors = neighbors[i][0]
            for j in range(1, len(neighbors[i])):
                bnFitness = bestNeighbors.fitness(bestNeighbors)
                nFitness = neighbors[i][j].fitness(neighbors[i][j])
                if bnFitness > nFitness:
                    bestNeighbors = neighbors[i][j]

        # update the velocity for each particle
        for i in range(len(self.__population)):
            for j in range(len(self.__population[0].getVelocity())):
                newVelocity = w * self.__population[i].getVelocityByPosition(j)
                newVelocity = newVelocity + c1 * random() * (bestNeighbors.getPositionByPosition(j) - self.__population[i].getPositionByPosition(j))
                newVelocity = newVelocity + c2 * random() * (self.__population[i].getBestPositionByPosition(j) - self.__population[i].getPositionByPosition(j))
                self.__population[i].setVelocityAtPosition(j, newVelocity)

        # update the position for each particle
        for i in range(len(self.__population)):
            for j in range(len(self.__population[0].getVelocity())):
                newPosition = self.__population[i].getPositionByPosition(j) + self.__population[i].getVelocityByPosition(j)
                self.__population[i].setPositionAtPosition(j, newPosition)

        return self.__population

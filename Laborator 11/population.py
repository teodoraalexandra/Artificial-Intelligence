#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:44:27 2020

@author: teodoradan
"""


from chromosome import Chromosome


class Population:
    def __init__(self, nrIndividuals, inputTrain, outputTrain):
        self.nrIndividuals = nrIndividuals
        self.individuals = [Chromosome(inputTrain, outputTrain) for _ in range(nrIndividuals)]
        self.inputTrain = inputTrain
        self.outputTrain = outputTrain

    def __str__(self):
        result = []
        for elem in self.individuals:
            result.append(str(elem.fitness))
        return str(result)

    def evaluate(self, inputTrain, outputTrain):
        for chromosome in self.individuals:
            chromosome.evaluate(inputTrain, outputTrain)

    def selection(self, nrInd):
        if nrInd < self.nrIndividuals:
            self.nrIndividuals = nrInd
            self.individuals = sorted(self.individuals, key=lambda x: x.fitness)
            self.individuals = self.individuals[:nrInd]

    def best(self, maxInd):
        self.individuals = sorted(self.individuals, key=lambda x: x.fitness)
        return self.individuals[:maxInd]

    def reunion(self, other):
        self.nrIndividuals += other.nrIndividuals
        self.individuals = self.individuals + other.individuals

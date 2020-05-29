#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:43:58 2020

@author: teodoradan
"""


from random import randint
from numpy.random.mtrand import choice
from node import Node
from math import *

f = open("input.in", "r")
f.readline()
DEPTH_MAX = int(f.readline())
f.close()


class Chromosome:
    def __init__(self, inputTrain, outputTrain, d=DEPTH_MAX):
        self.inputTrain = inputTrain
        self.outputTrain = outputTrain
        self.root = Node()
        self.root.init(d)
        self.maxDepth = d
        self.fitness = self.evaluate(self.inputTrain, self.outputTrain)

    def __str__(self):
        return str(self.root)

    def evaluate(self, inputTrain, outputTrain):
        self.fitness = 0
        nr = 0
        exp = str(self.root)
        for (x, y) in zip(inputTrain, outputTrain):
            for i in range(len(x)):
                from controller import HEADER
                HEADER[i] = str(x[i])
 
            res = eval(exp)

            new_res = abs(float(res) - float(y))

            self.fitness += new_res
            nr += 1
        self.fitness = self.fitness / nr
        return self.fitness
 
    @staticmethod
    def crossover(ch1, ch2, inputTrain, outputTrain):
        node1 = choice(ch1.root.getNodes())
        node2 = choice(ch2.root.getNodes())
        c = Chromosome(inputTrain, outputTrain)
        if ch1.root == node1:  # if we must change the whole tree
            c.root = node2.deepcopy()
        else:
            c.root = Node()
            c.root.change(ch1.root, node1, node2)
        return c

    def mutate(self, prob):
        pos = randint(1, self.root.size)
        self.root.mutate(pos, prob)

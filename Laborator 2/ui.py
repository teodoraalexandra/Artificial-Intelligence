#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:44:01 2020

@author: teodoradan
"""

from state import State
from problem import Problem
from controller import Controller
from time import time


def printMainMenu():
    s = ''
    s += "0 - exit \n"
    s += "1 - find a path with DFS \n"
    s += "2 - find a path with Greedy\n"
    print(s)


class UI:
    def __init__(self, n):
        self.__problem = Problem(n)
        self.__controller = Controller(self.__problem)

    def findPathDFS(self):
        startClock = time()
        solutions = self.__controller.DFS(0)
        solutions.prettyPrint()
        print('execution time = ', time() - startClock, " seconds")

    def findPathGreedy(self):
        startClock = time()
        solutions = self.__controller.Greedy()
        print(solutions)
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        runM = True
        printMainMenu()
        while runM:
            command = int(input(">>"))
            if command == 0:
                runM = False
            elif command == 1:
                self.findPathDFS()
            elif command == 2:
                self.findPathGreedy()
            else:
                print ("Invalid command")


n = int(input("Enter the size of the matrix >> "))
ui = UI(n)
ui.run()

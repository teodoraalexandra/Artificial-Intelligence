#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:54:02 2020

@author: teodoradan
"""

from collections import deque


class Controller:
    def __init__(self, problem):
        self.__problem = problem
        self.__stateList = problem.getState()

    def DFS(self, row):
        # row - integer - the row number we are considering
        # (initially we call DFS(0))
        if row == self.__problem.getSize():
            self.__stateList.addState(self.__problem.outputFormat())
            return
        for col in range(self.__problem.getSize()):
            if self.__problem.isValidMove(row, col):
                self.__problem.addInMatrix(row, col)
                self.DFS(row + 1)
                self.__problem.removeFromMatrix(row, col)

        return self.__stateList

    def Greedy(self):
        queue = self.__problem.getMatrix()
        diagonal = self.__problem.getDiagonizable()

        possible_solution = []
        row = 0
        while queue:
            row_state = queue.pop()
            row_diagonal = diagonal.pop()

            sumRows = 0
            for item in row_state:
                sumRows += int(item)
            if sumRows == 1:
                possible_solution.append(row_state)
                continue

            next_state = self.__problem.expand(row_state, row_diagonal, row)
            possible_solution.append(next_state)
            row += 1

        # check if possible_solution is a solution
        self.__problem.setMatrix(possible_solution)
        if self.__problem.isValidMove(self.__problem.getSize() - 1, self.__problem.getSize() - 1):
            return possible_solution
        else:
            return "I can not find a valid solution, but I get this: ", possible_solution

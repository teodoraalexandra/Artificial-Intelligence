#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:54:20 2020

@author: teodoradan
"""

from state import State


class Problem:

    def __init__(self, n):
        self.__n = n
        self.__state = State()
        self.__matrix = [['0' for x in range(n)] for y in range(n)]
        self.__positionList = []
        self.__diagonalMatrix = [['0' for x in range(n)] for y in range(n)]
        self.generateMatrix()

    def generateMatrix(self):
        position = 0
        for i in range(0, self.getSize()):
            self.__diagonalMatrix[i][position] = '1'
            position += 1

    def getSize(self):
        return self.__n

    def getState(self):
        return self.__state

    def getMatrix(self):
        return self.__matrix

    def getDiagonizable(self):
        return self.__diagonalMatrix

    def setMatrix(self, newMatrix):
        self.__matrix = newMatrix

    def getPosition(self):
        return self.__positionList

    def addPositionList(self, x):
        self.__positionList.append(x)

    def heuristic(self, row_state):
        self.__positionList.sort(reverse=True)

        if len(self.__positionList) > 1 and len(self.__positionList) != self.getSize():
            col = self.__positionList[-1] - self.__positionList[0]
            col = abs(col)
            row_state[col] = '1'
            return row_state
        elif len(self.__positionList) == self.getSize():
            row_state[0] = '1'
            return row_state
        else:
            col = self.__positionList[-1]
            row_state[col] = '1'
            return row_state

    def expand(self, row_state, row_diagonal, row):
        for i in range(0, self.getSize()):
            if row_diagonal[i] == '1':
                position = i
                self.__positionList.append(position)
                row_state = self.heuristic(row_state)
        return row_state

    def isValidMove(self, row, col):
        col_j = col
        left_diag_j = col
        right_diag_j = col
        for i in range(row, -1, -1):
            if self.__matrix[i][col_j] == '1':
                return False
            if left_diag_j >= 0 and self.__matrix[i][left_diag_j] == '1':
                return False
            if right_diag_j < self.__n and self.__matrix[i][right_diag_j] == '1':
                return False
            left_diag_j -= 1
            right_diag_j += 1
        return True

    def addInMatrix(self, row, col):
        self.__matrix[row][col] = '1'

    def removeFromMatrix(self, row, col):
        self.__matrix[row][col] = '0'

    def outputFormat(self):
        output = []
        for row in self.__matrix:
            output.append(' '.join(map(str, row)))
        return output

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:03:22 2020

@author: teodoradan
"""


from __future__ import print_function
from problem import Problem
from controller import Controller

if __name__ == '__main__':

    problem = Problem("balance-scale.txt")
    controller = Controller(problem)

    controller.startBuilding()




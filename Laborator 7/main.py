#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:50:52 2020

@author: teodoradan
"""

from problem import Problem
from controller import Controller

if __name__ == '__main__':
    p = Problem("bdate2.txt")
    c = Controller(p)
    c.run()
    

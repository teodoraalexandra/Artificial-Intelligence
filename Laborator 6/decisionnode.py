#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:02:39 2020

@author: teodoradan
"""


class DecisionNode:
    # a Decision Node asks a question.
    # this holds a reference to the question, the child containing true instances, and the one with false instances

    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

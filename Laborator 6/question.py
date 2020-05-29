#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:04:05 2020

@author: teodoradan
"""


class Question:
    # column represent the name of the attributes:
    #       "left-weight", "left-distance", "right-weight", "right-distance", "label"
    # value represent the possible values for these columns (1, 2, 3, 4, 5) -> 5 possible values

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def __str__(self):
        condition = ">="
        header = ["left-weight", "left-distance", "right-weight", "right-distance", "label"]
        s = "Is " + header[self.column] + " " + condition + " " + str(self.value) + "?"
        return s

    # q = Question(0, 1) --> Is left-weight >= 1?
    # example = training_data[0] --> [1, 2, 2, 4, 'R']
    # q.match(example) --> result will be true

    def match(self, instance):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = instance[self.column]
        return val >= self.value

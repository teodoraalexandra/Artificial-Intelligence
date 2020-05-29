#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:03:03 2020

@author: teodoradan
"""


class Leaf:
    # a Leaf node classifies data
    # it calls the class_counts function that returns a dictionary

    def __init__(self, trainingData):
        self.trainingData = trainingData
        self.predictions = self.class_counts()

    def class_counts(self):
        # counts for each class how many elements are there

        counts = {}  # a dictionary of label -> count.
        for row in self.trainingData:
            # in our dataset format, the label is always the first column
            label = row[-1]
            if label not in counts:
                counts[label] = 0
            counts[label] += 1
        return counts

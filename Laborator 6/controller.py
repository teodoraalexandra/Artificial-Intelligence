#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:02:10 2020

@author: teodoradan
"""


from question import Question
from decisionnode import DecisionNode
from leaf import Leaf


# print(class_counts(training_data)) --> {'B': 1, 'R': 2, 'L': 2}
def class_counts(trainingData):
    # counts for each class how many elements are there

    counts = {}  # a dictionary of label -> count.
    for row in trainingData:
        # in our dataset format, the label is always the first column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


# trueRows, falseRows = partition(training_data, Question(0, 4))
# print(trueRows) --> [4, 4, 2, 5, 'L']
# print(falseRows) --> [1, 2, 2, 4, 'R'], [1, 1, 5, 5, 'R'], [1, 1, 1, 1, 'B'], [1, 5, 2, 1, 'L']
def partition(trainingData, question):
    true_rows = []
    false_rows = []
    for row in trainingData:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


# no_mixing = [['R'], ['R']]
# print(gini(no_mixing)) --> best giniIndex because there is no mixing --> 0

# some_mixing = [['R'], ['B']]
# print(gini(some_mixing)) --> not great, not terrible --> 0.5

# lots_of_mixing = [['R'], ['B'], ['L']]
# print(gini(lots_of_mixing)) --> in this case there is much mixing, so gini index is higher --> approximately 0.6
def gini(rows):
    # compute the gini index for a list formed of classes
    # gini index is a metric to measure how often a randomly chosen element would be incorrectly identified
    # an attribute with lower gini index should be preferred
    # the formula used for computing gini index:
    #           1 - SUM(p ** 2)
    counts = class_counts(rows)  # here we keep track of how many different elements are (in dictionary)
    giniIndex = 1
    for element in counts:
        probability_of_element = counts[element] / float(len(rows))
        giniIndex -= probability_of_element ** 2
    return giniIndex


# giniIndex = gini(training_data)
# true_rows, false_rows = partition(training_data, Question(0, 4))
# print (info_gain(true_rows, false_rows, giniIndex)) --> 0.14

# giniIndex = gini(training_data)
# true_rows, false_rows = partition(training_data, Question(1, 3))
# print (info_gain(true_rows, false_rows, giniIndex)) --> 0.37
def info_gain(trueRows, falseRows, gini_index):
    # return the information gain --> the higher, the better
    # the partition will be more accurate if the information gain will be higher
    p = float(len(trueRows)) / (len(trueRows) + len(falseRows))
    return gini_index - p * gini(trueRows) - (1 - p) * gini(falseRows)


# bestGain, bestQuestion = find_best_split(training_data)
# print(bestGain) --> 0.37
# print(bestQuestion) --> Is left-distance >= 4?
def find_best_split(trainingData):
    # we compute the information gain for every possible question
    # the greatest information gain wins -> this question will be asked

    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_gini_index = gini(trainingData)
    nr_of_features = len(trainingData[0]) - 1  # this should be 4

    for feature in range(nr_of_features):

        values = set([row[feature] for row in trainingData])

        for val in values:

            # create a question for every feature and for every value
            question = Question(feature, val)

            true_rows, false_rows = partition(trainingData, question)
            if len(true_rows) == 0 or len(false_rows) == 0:
                # prevent the algorithm to crash if the data is not partitioned
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_gini_index)

            # update the best_gain and best_question if there is the case
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


# my_tree = build_tree(training_data)
# print(print_leaf(classify(training_data[0], my_tree)))
# print(print_leaf(classify(training_data[1], my_tree)))
def print_leaf(counts):
    # compute the probability for every prediction made in the leaf
    total = sum(counts.values()) * 1.0
    print("counts: ", counts)
    probabilities = {}
    for label in counts.keys():
        probabilities[label] = str(int(counts[label] / total * 100)) + "%"
    return probabilities


class Controller:
    def __init__(self, problem):
        self.__testingData = problem.getTestingData()
        self.__trainingData = problem.getTrainingData()

    def build_tree(self, trainingData):
        # calculate the information gain and return the question that produces the highest gain
        gain, question = find_best_split(trainingData)

        # if the information gain is 0 --> return a leaf
        if gain == 0:
            return Leaf(trainingData)

        true_rows, false_rows = partition(trainingData, question)

        # Recursively build the true and false branch
        true_branch = self.build_tree(true_rows)
        false_branch = self.build_tree(false_rows)

        # in the decision node we will keep:
        #   the best question so far
        #   the true branch we need to follow
        #   the false branch we need to follow
        return DecisionNode(question, true_branch, false_branch)

    def print_tree(self, node, spacing=""):
        if isinstance(node, Leaf):
            print (spacing + "Predict", node.predictions)
            return

        print(spacing + str(node.question))  # print the question
        print(spacing + "--> True:")
        self.print_tree(node.true_branch, spacing + " ")  # print the true branch (recursively)

        print(spacing + "--> False:")
        self.print_tree(node.false_branch, spacing + " ")  # print the false branch (recursively)

    def classify(self, element, node):
        if isinstance(node, Leaf):
            return node.predictions

        # decide what path to follow
        if node.question.match(element):
            return self.classify(element, node.true_branch)
        else:
            return self.classify(element, node.false_branch)

    # my_tree = build_tree(training_data)
    # classify(training_data[0], my_tree)

    def startBuilding(self):
        my_tree = self.build_tree(self.__trainingData)

        self.print_tree(my_tree)

        average = 0
        number_of_iterations = 0

        for row in self.__testingData:
            actual = row[-1]
            predicted = self.classify(row, my_tree).keys()
            prediction = ""
            for elem in predicted:
                prediction += elem
            print("Actual: " + str(actual) + " Predicted: " + str(prediction))
            if actual == prediction:
                score = 100
                average += score
                number_of_iterations += 1
            else:
                score = 0
                number_of_iterations += 1

        print("\n")
        print("Average score after all: " + str(average // number_of_iterations))

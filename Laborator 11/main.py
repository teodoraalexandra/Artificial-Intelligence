#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:34:48 2020

@author: teodoradan
"""


from controller import Controller
from random import shuffle
import time


input_data = []
output_data = []
inputTest = []
outputTest = []
inputTrain = []
outputTrain = []

TrainSIZE = 0.75  # percentage of training size
TestSIZE = 0.25  # percentage of testing size


def loadData():
    nr = 0
    global TrainSIZE
    print("Loading training data from file training.in")
    time.sleep(2)
    with open("training.in", "r") as f:
        # for using whole db (might take a lot of time), we should remove the [:x]
        for line in f.readlines()[:100]:
            values = list(line.split(','))
            input_data.append(values[0:-1])

            for element in input_data:
                for i in range(len(element)):
                    element[i] = float(element[i])

            output_data.append(values[-1])

            i = 0
            for element in output_data:
                if element == "Sharp-Right-Turn\n":
                    element = 3
                if element == "Slight-Right-Turn\n":
                    element = 2
                if element == "Move-Forward\n":
                    element = 1
                if element == "Slight-Left-Turn\n":
                    element = 0
                output_data[i] = element
                i += 1

            nr += 1

    shuffle(input_data)
    shuffle(output_data)

    inputTrain = input_data[:int(nr * TrainSIZE)]
    outputTrain = output_data[:int(nr * TrainSIZE)]
    inputTest = input_data[int(nr * TrainSIZE):]
    outputTest = output_data[int(nr * TrainSIZE):]

    print("Training size: " + str(len(inputTrain)))
    print("Testing size: " + str(len(outputTest)))
    print("\n")

    return input_data, output_data, inputTrain, outputTrain, inputTest, outputTest


if __name__ == '__main__':
    f = open("input.in", "r")
    epsilon = f.readline()
    depth = f.readline()
    print("From input.in we've read 2 parameters.\n")
    print("-----Epsilon: ", epsilon)
    print("-----Depth max: ", depth)
    time.sleep(2)
    
    input_data, output_data, inputTrain, outputTrain, inputTest, outputTest = loadData()
    controller = Controller(10, input_data, output_data, inputTrain, outputTrain, inputTest, outputTest)
    controller.run()


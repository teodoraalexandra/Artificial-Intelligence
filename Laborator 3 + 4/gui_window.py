# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from problem import Problem
from controller import Controller
from chromozomePopulation import ChromozomePopulation
from particlePopulation import ParticlePopulation
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count
import pandas as pd
import statistics
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count
import pandas as pd
import statistics

from threading import Thread as process
import requests
import threading 
import time 

class Ui_MainWindow(object):
    def __init__(self):
        self.__eaAverage = []
        self.__psoAverage = []
        
    def animate_EA(self, x_vals, y_vals, index, r):
        population = 40
        n = 3 #Statistics are for a 3x3 matrix
        P = ChromozomePopulation(population, 1, n) #population = 40
        pop = P.getPopulation()
         
        r = random.randrange(1, 40)
        x_vals.append(next(index))
        y_vals.append(P.fitness(pop[r], n))
        self.__eaAverage.append(P.fitness(pop[r], n))
        
        plt.cla()
        plt.plot(x_vals, y_vals)
        plt.show()
        
    def animate_PSO(self, x_vals, y_vals, index, r):
        population = 40
        n = 3 #Statistics are for a 3x3 matrix
        P = ParticlePopulation(population, 1, n) #population = 40
        pop = P.getPopulation()
         
        r = random.randrange(1, 40)
        particle = pop[r]
        x_vals.append(next(index))
        y_vals.append(particle.fitness(particle))
        self.__psoAverage.append(particle.fitness(particle))
        
        plt.cla()
        plt.plot(x_vals, y_vals)
        plt.show()
        
    def statisticsEvolutionaryAlgorithm(self, n):
        plt.style.use('fivethirtyeight')
        
        x_vals = []
        y_vals = []
        
        index = count()
        
        for run in range(30): #run = 30
            r = random.randrange(1, 40)
            #evaluation = 1000 (interval)
            FuncAnimation(plt.gcf(), self.animate_EA(x_vals, y_vals, index, r), interval = 1000)
        
        plt.tight_layout()
        
        #average display for best solution
        sum_num = 0
        for t in self.__eaAverage:
            sum_num = sum_num + t           

        avg = sum_num / len(self.__eaAverage)
        print ("Average of fitness score is: ", avg)
        
        #standard deviation display for best solution
        deviation = statistics.stdev(self.__eaAverage)
        print ("Standard deviation of fitness score is: ", deviation)
        
    def statisticsParticleSwarmOptimization(self, n):
        plt.style.use('fivethirtyeight')
        
        x_vals = []
        y_vals = []
        
        index = count()
        
        for run in range(30): #run = 30
            r = random.randrange(1, 40)
            #evaluation = 1000 (interval)
            FuncAnimation(plt.gcf(), self.animate_PSO(x_vals, y_vals, index, r), interval = 1000)
        
        plt.tight_layout()
        
        #average display for best solution
        sum_num = 0
        for t in self.__psoAverage:
            sum_num = sum_num + t           

        avg = sum_num / len(self.__psoAverage)
        print ("Average of fitness score is: ", avg)
        
        #standard deviation display for best solution
        deviation = statistics.stdev(self.__psoAverage)
        print ("Standard deviation of fitness score is: ", deviation)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 70, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 130, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 160, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 131, 31))
        self.label.setStyleSheet("font: 18pt \".SF NS Text\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 151, 16))
        self.label_4.setObjectName("label_4")
        """
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 240, 181, 41))
        self.label_5.setStyleSheet("font: 18pt \".SF NS Text\";")
        self.label_5.setObjectName("label_5")
        """
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 160, 101, 16))
        self.label_8.setObjectName("label_6")
        """
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(60, 290, 221, 151))
        self.textEdit_1.setObjectName("textEdit_1")
        """
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 180, 181, 71))
        self.pushButton.setStyleSheet("font: 18pt \".SF NS Text\";")
        self.pushButton.setObjectName("pushButton")
        """
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(460, 310, 211, 131))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 270, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 460, 60, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 500, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        """
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 70, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 70, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 120, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
        self.pushButton_2.clicked.connect(self.startEA)
        self.pushButton_3.clicked.connect(self.startHC)
        self.pushButton_4.clicked.connect(self.startPSO)
        self.pushButton.clicked.connect(self.stopAlgo)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def stopAlgo(self):
        app.quit()
            
    def startEA(self):
        def callbackEA(a, b, c, d):
            self.__n = d
            self.__problem = Problem(self.__n)
            self.__controller = Controller(self.__problem)
            
            #startClock = time()
            noIteratii = c
            dimPopulation = b
            
            # numbers for permutations will be in interval [1, n]
            vmin = 1
            vmax = self.__n
            
            # the mutation probability
            pM = a
            # maximum fitness possible
            maximumFitness = 4 * vmax
            
            optimIndividual, fitnessOptim = self.__controller.EvolutionaryAlgorithm(noIteratii, dimPopulation, vmin, vmax, pM)
            # output of the optim individual
            print ("This is the best individual I could find: \n")
            print (optimIndividual)
            
            # output of the fitness of the individuali
            ratio = str(fitnessOptim) + '/' + str(maximumFitness)
            print (ratio)
            #print('execution time = ', time() - startClock, " seconds")
            
        lineEdit1 = float(self.lineEdit.text())
        lineEdit2 = int(self.lineEdit_2.text())
        lineEdit3 = int(self.lineEdit_3.text())
        lineEdit4 = int(self.lineEdit_4.text())
        t = threading.Thread(target = callbackEA, args =(lineEdit1, lineEdit2, lineEdit3, lineEdit4, )) 
        t.start()
        
    def startHC(self):
        def callbackHC(d):
            self.__n = d
            self.__problem = Problem(self.__n)
            self.__controller = Controller(self.__problem)
            
            #startClock = time()
            # maximum fitness possible
            maximumFitness = 4 * self.__n
    
            optimIndividual, fitnessOptim = self.__controller.HillClimbing(self.__n)
            # output of the optim individual
            print ("This is the best individual I could find: \n")
            print (optimIndividual)
            
            # output of the fitness of the individual
            ratio = str(fitnessOptim) + '/' + str(maximumFitness)
            print (ratio)
            #print('execution time = ', time() - startClock, " seconds")
        
        lineEdit4 = int(self.lineEdit_4.text())
        t = threading.Thread(target = callbackHC, args =(lineEdit4, )) 
        t.start()
        
    def startPSO(self):
        def callbackPSO(b, c, d):
            self.__n = d
            self.__problem = Problem(self.__n)
            self.__controller = Controller(self.__problem)
            
            #startClock = time()
            noIteratii = c
            dimPopulation = b
    
            # numbers for permutations will be in interval [1, n]
            vmin = 1
            vmax = self.__n
            # maximum fitness possible
            maximumFitness = 4 * vmax
    
            # specific parameters for PSO
            w = 1.0
            c1 = 1.
            c2 = 2.5
            sizeOfNeighborhood = 20
    
            optimIndividual, fitnessOptim = self.__controller.ParticleSwarmOptimization(noIteratii, dimPopulation, vmin, vmax, w, c1, c2, sizeOfNeighborhood)
            # output of the optim individual
            print ("This is the best individual I could find: \n")
            print (str(optimIndividual))
            
            # output of the fitness of the individuali
            ratio = str(fitnessOptim) + '/' + str(maximumFitness)
            print (ratio)
            #print('execution time = ', time() - startClock, " seconds")
        
        lineEdit2 = int(self.lineEdit_2.text())
        lineEdit3 = int(self.lineEdit_3.text())
        lineEdit4 = int(self.lineEdit_4.text())
        t = threading.Thread(target = callbackPSO, args =(lineEdit2, lineEdit3, lineEdit4, )) 
        t.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User input:"))
        self.label_2.setText(_translate("MainWindow", "Probability of mutation"))
        self.label_3.setText(_translate("MainWindow", "Population size"))
        self.label_4.setText(_translate("MainWindow", "Numbers of generations"))
        #self.label_5.setText(_translate("MainWindow", "Best found until now:"))
        self.pushButton.setText(_translate("MainWindow", "Stop algorithm"))
        #self.label_6.setText(_translate("MainWindow", "Final found solution:"))
        #self.label_7.setText(_translate("MainWindow", "Fitness:"))
        self.label_8.setText(_translate("MainWindor", "Size of matrix:"))
        self.pushButton_2.setText(_translate("MainWindow", "Start EA"))
        self.pushButton_3.setText(_translate("MainWindow", "Start HC"))
        self.pushButton_4.setText(_translate("MainWindow", "Start PSO"))


if __name__ == "__main__":
    ui = Ui_MainWindow()
    #STATISTICS ARE FOR A 3x3 MATRIX
    option = input("Wanna see some statistics first? [y/n] >> ")
    if (option == "y"):
        second_option = int(input("EA or PSO? [1/2] >> "))
        if (second_option == 1):
            ui.statisticsEvolutionaryAlgorithm(3)
        elif (second_option == 2):
            ui.statisticsParticleSwarmOptimization(3)
        else:
            print("Invalid option.")
    elif (option == "n"):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        print("Invalid option.")
    


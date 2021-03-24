import project1 as p1
from project1 import perceptron, average_perceptron, pegasos
import utils
import numpy as np
import numpy.testing as npt
import re


toy_features, toy_labels = toy_data = utils.load_toy_data('toy_data.tsv')
T = 10
L = 0.2

thetas = perceptron(toy_features, toy_labels, T)
print(thetas)
utils.plot_toy_data("Perceptron", toy_features, toy_labels, thetas)

thetas = average_perceptron(toy_features, toy_labels, T)
print(thetas)
utils.plot_toy_data("Average Perceptron", toy_features, toy_labels, thetas)

thetas = pegasos(toy_features, toy_labels, T, L)
print(thetas)
utils.plot_toy_data("Pegasos", toy_features, toy_labels, thetas)
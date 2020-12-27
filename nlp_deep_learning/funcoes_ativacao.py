# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:06:06 2020

@author: TOP Artes
"""

import numpy as np
# transfer function

def stepFunction(soma):
    """
    Linearmente separáveis
    """
    if (soma >= 1):
        return 1
    return 0

step_teste = stepFunction(-0.358)

def sigmoidFunction(soma):
    """
    Classificação binária
    """
    return 1 / (1 + np.exp(-soma))

sig_teste = sigmoidFunction(-0.358)

def tanhFunction(soma):
    """
    Classificação entre 0 e 1
    """
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

tan_teste = tanhFunction(-0.358)

def reluFunction(soma):
    """
    Redes neurais convolucionais
    """
    if soma >= 0:
        return soma
    return 0

relu_teste = reluFunction(0.358)

def linearFunction(soma):
    return soma

linear_teste = linearFunction(0.358)

def softmaxFunction(x):
    """
    Classificação mais de 2 classes
    """
    ex = np.exp(x)
    return ex / ex.sum()

soft_teste = softmaxFunction([5.0,2.0,1.3])
print(soft_teste)
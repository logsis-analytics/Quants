# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:27:50 2021

@author: danielpazing

logsis: logística - proceso -simulación - analitycs
www.logsis.com.ar

MOVIMIENTO BROWNIANO
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt


ejex = np.arange(1000)
ejey = np.zeros(shape=1000, dtype=float)
ejez = np.zeros(shape=1000, dtype=float)

vals = np.random.standard_normal(1000)


for t in range(1,1000):
        
    ejez[t]= ejez[t-1] + vals[t]
    

plt.plot(ejex,ejez)

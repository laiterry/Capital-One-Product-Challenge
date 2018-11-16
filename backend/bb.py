#!/usr/bin/env python

# -*- Coding: UTF-8 -*-
# @Time    : 11/15/18 9:07 PM
# @Author  : Terry LAI
# @Email   : terry.lai@hotmail.com
# @File    : bb.py
import pandas as pd
import numpy as np
import time
from datetime import datetime
import statsmodels.formula.api as sm
#from fbprophet import Prophet
import matplotlib.pylab as plt

def Happymodel(input1):
    data = pd.read_csv('hourlyrate_with_skills_web-mobile-software-dev_2018_11_15_16_04_31.txt',header=None)
    list=[]
    for i in range(4,14):
        for value in data[i]:
            if value not in list:
                list.append(value)
    df= pd.DataFrame(index=data.index, columns=list)
    for j in range(4,14):
        for i in range(0,584):
            skills=data[j][i]
            #print (skills)
            df[skills][i]=1
    datadroped=data.drop(columns=[4,5,6,7,8,9,10,11,12,13])
    df2=datadroped.join(df,how='outer')
    df2=df2.fillna(0)
    observation=[]
    for i in range (0,584):
        if df2[input1][i] == 1:
            observation.append(i)
    df3 = df2.loc[observation,list]
    df3 = df3.join(df2[3],how='outer')
    df3 = df3.fillna(0)
    y = df3[3]
    X = df3[list]
    model1 = sm.OLS(y, X).fit()
    result=model1.summary(alpha=0.05)
    #print (result)
    modeloutput1=model1.params.sort_values(ascending=True)[-4:-1]
    return (modeloutput1.index),(sum(modeloutput1))
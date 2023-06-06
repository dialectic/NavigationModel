# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:27:06 2023

@author: ai598
"""
import tensorflow as tf
from keras.datasets import imdb  # import imdb data 
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import RepeatedKFold
from tensorflow.keras.utils import to_categorical
import numpy as np
import pandas as pd
from keras.utils.np_utils import to_categorical
from keras import layers
from keras import models
import random as random
import pickle
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import warnings
warnings.filterwarnings("ignore")
import command as command
import compare as compare



filename ='NewTuneMoveTrain2.sav'
trained_model = pickle.load(open(filename,'rb'))


df = pd.read_csv('PROCESSED DATA\MoveTestData20.csv') 

# *****************FOR 24 INPUT *******************************
Input = pd.DataFrame(df[['VIX1', 'VIX2', 'VIX3', 'VIX4', 'VIX5', 'VIX6', 'VGX1', 'VGX2', 'VGX3', 'VGX4', 'VGX5', 'VGX6',
       'OIX1', 'OIX2', 'OIX3', 'OIX4', 'OIX5', 'OIX6', 'OGX1', 'OGX2', 'OGX3', 'OGX4', 'OGX5', 'OGX6']])


InputArray = np.asarray(Input)

# Make prediction from model
new_predict = trained_model.predict(InputArray)


# Create Vehicle Input Array

Vdata = np.zeros([new_predict.shape[0],24])

i=0
while(i<6):
  Vdata[:,i] = InputArray[:,i] # VIX1 - VIX6
  i=i+1
j=0
while(j<12):
  Vdata[:,6+j] = new_predict[:,j] # VM1X1 - VM1X6 & VM2X1 - VM2X6 
  j=j+1
k=0
while(k<6):
  Vdata[:,18+k] = InputArray[:,6+k] # VGX1 - VGX6
  k=k+1
  
  
  
# Obstacle Data Frame

OdataFrame = pd.DataFrame(df[['OIX1', 'OIX2', 'OIX3', 'OIX4', 'OIX5', 'OIX6', 'OM1X1', 'OM1X2',
       'OM1X3', 'OM1X4', 'OM1X5', 'OM1X6', 'OM2X1', 'OM2X2', 'OM2X3', 'OM2X4',
       'OM2X5', 'OM2X6', 'OGX1', 'OGX2', 'OGX3', 'OGX4', 'OGX5', 'OGX6']])  
  
Odata = np.asarray(OdataFrame) 
 

Observation = Odata.shape[0]
Vdata=Vdata.reshape(Observation,4,6)
Odata=Odata.reshape(Observation,4,6)
  

i = 0

Vmove = np.zeros([Observation,2,10])
Omove = np.zeros([Observation,2,10])
while(i<Observation):
  VI_state  = Vdata[i,0,:]
  VM1_state = Vdata[i,1,:]
  VM2_state = Vdata[i,2,:]
  VG_state  = Vdata[i,3,:] 

  OI_state  = Odata[i,0,:]
  OM1_state = Odata[i,1,:]
  OM2_state = Odata[i,2,:]
  OG_state  = Odata[i,3,:]

  Vmove[i] = command.Cmove( VI_state, VG_state,VM1_state,VM2_state)
  Omove[i] = command.Cmove( OI_state, OG_state,OM1_state,OM2_state)

  i=i+1
  
  
count,index = compare.CheckBad(Vmove,Omove)
  
  
print(count)  


  
#%%

Learned_count = count

Random_count = 10805 # from data process module

# creating the dataset
data = {'Trained':Learned_count, 'Random':Random_count}
comp_models = list(data.keys())
values = list(data.values())
# creating the bar plot
plt.bar(comp_models, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Models")
plt.ylabel("Bad Count")
plt.title("Bad Move Comparison")
plt.show()
  
  
  
  
  
  
  
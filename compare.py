# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:32:00 2023

@author: ai598
"""
import numpy as np


def IsClose(A,B):
    C = [A[0]-B[0],A[1]-B[1]]
    dist = np.linalg.norm(C)
    if(dist<(10/100) ):
      return True
    else:
      return False
  
def CheckBad(Vmove,Omove):
    
    observation = len(Vmove)
    m = 0
    n = 0
    count = 0
    index = np.ones([observation])
    while(m<observation):


      while(n<10):
        V_ppoints = Vmove[m,:,n]
        O_points  = Omove[m,:,n]

        if(IsClose(V_ppoints,O_points)):
          count = count+1
          n=10 # get outta loop
          index[m]=0
    
        else:
          count = count
          n=n+1 
      n=0
      m=m+1
    
    return count,index

def GetLabel(Vmove,Omove):
    count,index = CheckBad(Vmove,Omove)
    return index
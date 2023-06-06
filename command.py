# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 17:59:37 2022

@author: Arif
"""
from scipy.interpolate import BarycentricInterpolator as BI
import numpy as np
  
def Lmove(Is,Gs):
    Ix = Is[0]
    Iy = Is[1]
    Gx = Gs[0]
    Gy = Gs[1]

    # Linear move
    xil = np.array([Ix,  Gx ]) #2 , 5.5,
    yil = np.array([Iy,  Gy]) # 8, 7,
    pl  = BI(xil,yil)

    x  = np.linspace(Ix,Gx,10)
    y  = pl(x)

    return x,y

def Pmove(Is,Gs,P1):
            
        Ix  = Is[0]
        Iy  = Is[1]
        Gx  = Gs[0]
        Gy  = Gs[1]
        P1x = P1[0]
        P1y = P1[1]

        # Parabolic move
        xip = np.array([Ix,P1x, Gx ]) 
        yip = np.array([Iy,P1y, Gy])
        pp  = BI(xip,yip)
        
        x  = np.linspace(Ix,Gx,10)
        y  = pp(x)

        return x,y

def Cmove(Is,Gs,P1,P2):
           
       Ix  = Is[0]
       Iy  = Is[1]
       Gx  = Gs[0]
       Gy  = Gs[1]
       P1x = P1[0]
       P1y = P1[1]
       P2x = P2[0]
       P2y = P2[1]

        # Cubic move
       xic = np.array([Ix,P1x,P2x, Gx ]) 
       yic = np.array([Iy,P1y,P2y, Gy])
       pc  = BI(xic,yic)

       x  = np.linspace(Ix,Gx,10)
       y  = pc(x)

       return x,y


    
   
    
    







      







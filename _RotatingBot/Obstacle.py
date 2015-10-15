import numpy as np
import math

class Obstacle:
    
    def __init__(self,x,y):
        self.centerX = x
        self.centerY = y
        self.radius = 1

        self.Theta_to_center = math.atan2(self.centerX, self.centerY)
        self.R_to_center = math.sqrt(self.centerX**2 + self.centerY**2)
    
    def computethetaTraj(self,psiworld):
        self.thetaTraj = psiworld + self.Theta_to_center

    def computexyTraj(self,xworld,yworld):
        self.xtraj = xworld + self.R_to_center*np.cos(self.thetaTraj)
        self.ytraj = yworld + self.R_to_center*np.sin(self.thetaTraj)

    def computeTraj(self,psiworld,xworld,yworld):
        self.computethetaTraj(psiworld)
        self.computexyTraj(xworld,yworld)

    def printCenter(self):
        print self.centerX, self.centerY
        
    def plotLists(self):
        
        t = np.linspace(-math.pi,math.pi,100)
        x = self.radius*np.cos(t) + self.centerX
        y = self.radius*np.sin(t) + self.centerY
        return x, y
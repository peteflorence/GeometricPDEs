import numpy as np
import math

class Obstacle:
    
    def __init__(self,x,y):
        self.centerX = x
        self.centerY = y
        self.radius = 1
        
    def printCenter(self):
        print self.centerX, self.centerY
        
    def plotLists(self):
        
        t = np.linspace(-math.pi,math.pi,100)
        x = self.radius*np.cos(t) + self.centerX
        y = self.radius*np.sin(t) + self.centerY
        return x, y
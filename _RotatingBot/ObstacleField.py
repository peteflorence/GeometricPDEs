import numpy as np
import math

class ObstacleField:

    def __init__(self):
        self.ObstaclesList = []
        
    def addObstacle(self,obstacle):
        self.ObstaclesList.append(obstacle)
    
    def printObstacles(self):
        counter = 1
        for i in self.ObstaclesList:
            print "Obstacle " + str(counter) + " center:"
            i.printCenter()
            counter += 1

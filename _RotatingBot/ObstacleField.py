import numpy as np
import math

from Obstacle import Obstacle

class ObstacleField:

    def __init__(self):
        self.ObstaclesList = []
        
    def addObstacle(self,obstacle):
        self.ObstaclesList.append(obstacle)
    
    def randomField(self, M=5, mindistance = 4, maxdistance = 17):
        # M is number of obstacles 

        randTheta = 2*math.pi * np.random.rand(1,M)[0]
        randR = (maxdistance - mindistance) * np.random.rand(1,M)[0] + mindistance

        for i in range(M):
            x = randR[i]*math.cos(randTheta[i])
            y = randR[i]*math.sin(randTheta[i])
            obs = Obstacle(x,y)
            self.addObstacle(obs)

    def printObstacles(self):
        counter = 1
        for i in self.ObstaclesList:
            print "Obstacle " + str(counter) + " center:"
            i.printCenter()
            counter += 1

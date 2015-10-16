import IPython.html.widgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np

import math

def plotPlane(theta_deg): 
    def plotObs(theta,ax):
        # Plot circle obstacle 2
        an = np.linspace(0,2*math.pi,100)
        r_circ = math.sqrt(5**2 + 12**2)
        print r_circ
        theta_0_circ = math.atan(-5.0/10.0)
        theta_rel_circ = theta + theta_0_circ
        print theta_rel_circ
        ax.plot(1*np.cos(an)+r_circ*math.sin(math.pi + theta_rel_circ), 1*np.sin(an) - r_circ*math.cos(math.pi + theta_rel_circ))

        # Plot circle obstacle 2
        an = np.linspace(0,2*math.pi,100)
        r_circ = math.sqrt(3**2 + 10**2)
        print r_circ
        theta_0_circ = math.atan(3.0/10.0)
        theta_rel_circ = theta + theta_0_circ
        print theta_rel_circ
        ax.plot(1*np.cos(an)+r_circ*math.sin(math.pi + theta_rel_circ), 1*np.sin(an) - r_circ*math.cos(math.pi + theta_rel_circ))

    fig, ax = plt.subplots()

    # Rotate for theta, measured as 0 true north
    theta = theta_deg*math.pi/180
    plotObs(theta,ax)

    def plotFOV(ax):
        FOVangle = 130*math.pi/180
        FOVlength = 10

        theta_neg = -FOVangle/2
        theta_pos = FOVangle/2

        ax.plot((0,FOVlength*math.cos(math.pi/2-theta_pos)),(0,FOVlength*math.sin(math.pi/2-theta_pos)),color='orange')
        ax.plot((0,FOVlength*math.cos(math.pi/2-theta_neg)),(0,FOVlength*math.sin(math.pi/2-theta_neg)),color='orange')



    ax.axis([-15, 15, -5, 20])

    im = plt.imread('tetrazeph.jpg')
    newax = fig.add_axes([0.477, 0.16, 0.07, 0.1], anchor='SW')
    newax.imshow(im)
    newax.axis('off')

    ax.set_aspect('equal', 'datalim')

    plotFOV(ax)

    plt.show()
    return 0
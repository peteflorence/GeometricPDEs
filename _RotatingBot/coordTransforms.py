import math
import numpy as np

def transformStandardPolarTheta_to_PlaneTheta(angle):
    x = np.cos(angle)
    y = np.sin(angle)
    thetatop = np.arcsin(x)
    if y < 0 :
      if x > 0:
        theta = math.pi - thetatop
      else:
        theta = -math.pi - thetatop
    else:
      theta = thetatop
    return theta
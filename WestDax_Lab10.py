import numpy as np
import matplotlib.pyplot as plt


#part 2
def make_initialcond(x, sigma_0, k_0):
    a_x = np.exp(-(x**2)/(2*(sigma_0**2))) * np.cos(k_0*x)
    return a_x

#part 3
def spectral_radius(A):
    #needs to use np.linalg.eig
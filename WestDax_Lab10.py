import numpy as np
import matplotlib.pyplot as plt

#part 1
def make_tridiagonal(N, b, d, a):
    matrix = d*np.identity(N)+b*np.diagflat(np.ones(N-1),1)+a*np.diagflat(np.ones(N-1),-1)
    return matrix
N = 5
b = 3
d = 1
a = 5

A = make_tridiagonal(N, b, d, a)
print(A)

# #part 2
# def make_initialcond(x, sigma_0, k_0):
#     a_x = np.exp(-(x**2)/(2*(sigma_0**2))) * np.cos(k_0*x)
#     return a_x
#
# #part 3
# def spectral_radius(A):
#     #needs to use np.linalg.eig
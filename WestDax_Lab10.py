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

#part 2
def make_initialcond(x, sigma_0, k_0):
    return np.exp(-(x**2)/(2*(sigma_0**2))) * np.cos(k_0*x)

N_space = 300
L = 5
sigma_0 = 0.2
k_0 = 35
x = np.linspace(-L/2, L/2, N_space)

a_x = make_initialcond(x, sigma_0, k_0)
print(a_x)

# #part 3
# def spectral_radius(A):
#     #needs to use np.linalg.eig
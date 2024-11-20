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
# print(A)

#part 2
def make_initialcond(x, sigma_0, k_0):
    return np.exp(-(x**2)/(2*(sigma_0**2))) * np.cos(k_0*x)

N_space = 300
L = 5
sigma_0 = 0.2
k_0 = 35
x = np.linspace(-L/2, L/2, N_space)

a_x = make_initialcond(x, sigma_0, k_0)
# print(a_x)
fig = plt.figure()
plt.plot(x, a_x)
plt.title('Wavepacket vs Position')
plt.ylabel('a(x,0)')
plt.xlabel('x')
plt.show()

# #part 3
def spectral_radius(A):
    #needs to use np.linalg.eig
    eigen = np.linalg.eig(A)
    return eigen[0], np.max(np.abs(eigen[0]))

eigen_vals, mav_abs_val = spectral_radius(A)

print(eigen_vals)
print(mav_abs_val)
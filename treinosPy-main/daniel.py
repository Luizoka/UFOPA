import matplotlib.pyplot as plt
import numpy as np
from scipy.integration import odeinter

a = 10
b = 28
c = 8/3

def lorenz(values, t):
    x,y,z = values
    dx_dt = a*(y-x)
    dy_dt = x*(b-z) - y 
    dz_dt = x*y - c*z
    
    return[dx_dt,dy_dt,dz_dt]

x0 = 1.5
y0 = 20
z0 = 15

t = np.arange(0, 40, 0.01)

result = odeinter(lorenz, [x0, y0, z0],t)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(result[:,0], result[:,1],result[:,2])
plt.show()
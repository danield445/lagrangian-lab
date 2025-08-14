import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pendulum(state, t, L, g):
    theta, omega = state
    dtheta = omega
    domega = -(g / L) * np.sin(theta) 
    return [dtheta, domega]


L, g = 1.0, 9.81
t = np.linspace(0, 10, 1000)
y0 = [np.pi/4, 0]  # Initial angle=45°, angular velocity=0


sol = odeint(pendulum, y0, t, args=(L, g))
plt.plot(t, sol[:, 0])
plt.xlabel('Time (s)'); plt.ylabel('Angle (rad)')
plt.savefig('pendulum_plot.png') 

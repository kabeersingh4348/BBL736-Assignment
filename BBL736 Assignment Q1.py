import numpy as np
import matplotlib.pyplot as plt

def rk4(f, x0, t0, tf, dt):
    
    t = np.arange(t0, tf, dt)
    n = len(t)
    x = np.zeros(n)
    x[0] = x0
    for i in range(n - 1):
        k1 = dt * f(x[i], t[i])
        k2 = dt * f(x[i] + 0.5 * k1, t[i] + 0.5 * dt)
        k3 = dt * f(x[i] + 0.5 * k2, t[i] + 0.5 * dt)
        k4 = dt * f(x[i] + k3, t[i] + dt)
        x[i + 1] = x[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return t, x


def f(p, t):
    
    return (20 * p**2 / (1 + p**2)) - p


initial_conditions = [1, 3, 6]


t0 = 0
tf = 20
dt = 0.01


plt.figure(figsize=(10, 6))
for p0 in initial_conditions:
    
    t, p = rk4(f, p0, t0, tf, dt)
    
    
    plt.plot(t, p, label=f'p(0)={p0}', linestyle='--')


p_values = np.linspace(0, 20, 100)
f_values = f(p_values, t0)  
plt.plot(p_values, f_values, label='f(p)', linestyle='-')

plt.title('Solution of dp/dt = 20p^2 / (1 + p^2) - p using RK4')
plt.xlabel('Time')
plt.ylabel('p(t)')
plt.grid(True)
plt.legend()
plt.show()

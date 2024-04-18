import numpy as np
import matplotlib.pyplot as plt

def simulate_stochastic_system(alpha, n, initial_count, duration):
    time = 0
    count = initial_count
    time_series = [(time, count)]
    
    while time < duration:
        production_rate = (alpha * count**n) / (1 + count**n)
        decay_rate = count
        total_rate = production_rate + decay_rate
        time += np.random.exponential(1 / total_rate)
        
        if np.random.rand() < (production_rate / total_rate):
            count += 1
        else:
            count -= 1
        
        time_series.append((time, count))
        if count <= 0:
            break
    
    return zip(*time_series)

alpha = 20
n = 2
duration = 50
starting_points = [1, 30, 80]

plt.figure(figsize=(10, 6))

for initial in starting_points:
    times, counts = simulate_stochastic_system(alpha, n, initial, duration)
    plt.plot(times, counts, label=f'Initial count = {initial}', linestyle='-', linewidth=1)

plt.title('Gene Expression Dynamics Simulation')
plt.xlabel('Time')
plt.ylabel('Molecule Count')
plt.legend()
plt.grid(True)
plt.show()

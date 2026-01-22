import numpy as np
import matplotlib.pyplot as plt

prey = [100]
pred = [20]

prey_birth_rate = 0.1
pred_death_rate = 0.05
predation_rate = 0.002
pred_efficiency = 0.001

time = [0]

for step in range(500):
    p = prey[-1]
    f = pred[-1]
    
    new_p = p + (prey_birth_rate*p - predation_rate*p*f)*0.1
    new_f = f + (pred_efficiency*p*f - pred_death_rate*f)*0.1
    
    prey.append(max(0, new_p))
    pred.append(max(0, new_f))
    time.append(time[-1]+0.1)

plt.figure(figsize=(10,6))
plt.plot(time, prey, label="Rabbits 🐇", color='green', linewidth=2)
plt.plot(time, pred, label="Foxes 🦊", color='red', linewidth=2)
plt.title("Predator vs Prey: chaos edition")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Rabbits left: {prey[-1]:.1f}")
print(f"Foxes left: {pred[-1]:.1f}")

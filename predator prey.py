import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class PredatorPreySimulation:
    def __init__(self, prey_init=100, pred_init=20):
        """
        Initialize the predator-prey simulation
        
        Parameters:
        - prey_init: initial prey population
        - pred_init: initial predator population
        """
        # Population parameters
        self.prey_birth_rate = 0.1      # Prey reproduction rate
        self.pred_death_rate = 0.05     # Predator death rate
        self.predation_rate = 0.002     # Rate at which predators eat prey
        self.pred_efficiency = 0.001    # Efficiency of converting prey to predators
        
        # Initialize populations
        self.time = [0]
        self.prey_pop = [prey_init]
        self.pred_pop = [pred_init]
        
    def step(self, dt=0.1):
        """Simulate one time step using differential equations"""
        prey = self.prey_pop[-1]
        pred = self.pred_pop[-1]
        
        # Lotka-Volterra equations
        dprey = (self.prey_birth_rate * prey - 
                 self.predation_rate * prey * pred) * dt
        dpred = (self.pred_efficiency * prey * pred - 
                 self.pred_death_rate * pred) * dt
        
        # Update populations (ensure non-negative)
        new_prey = max(0, prey + dprey)
        new_pred = max(0, pred + dpred)
        
        self.prey_pop.append(new_prey)
        self.pred_pop.append(new_pred)
        self.time.append(self.time[-1] + dt)
        
    def run(self, steps=1000):
        """Run simulation for a number of steps"""
        for _ in range(steps):
            self.step()
    
    def plot(self):
        """Plot the population dynamics"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Time series plot
        ax1.plot(self.time, self.prey_pop, label='Prey', color='green', linewidth=2)
        ax1.plot(self.time, self.pred_pop, label='Predators', color='red', linewidth=2)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Population')
        ax1.set_title('Predator-Prey Population Dynamics')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Phase space plot
        ax2.plot(self.prey_pop, self.pred_pop, color='blue', linewidth=1.5, alpha=0.7)
        ax2.scatter(self.prey_pop[0], self.pred_pop[0], color='green', s=100, 
                   label='Start', zorder=5)
        ax2.scatter(self.prey_pop[-1], self.pred_pop[-1], color='red', s=100, 
                   label='End', zorder=5)
        ax2.set_xlabel('Prey Population')
        ax2.set_ylabel('Predator Population')
        ax2.set_title('Phase Space (Predator vs Prey)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

# Run the simulation
if __name__ == "__main__":
    # Create and run simulation
    sim = PredatorPreySimulation(prey_init=100, pred_init=20)
    sim.run(steps=2000)
    sim.plot()
    
    print(f"Final prey population: {sim.prey_pop[-1]:.1f}")
    print(f"Final predator population: {sim.pred_pop[-1]:.1f}")



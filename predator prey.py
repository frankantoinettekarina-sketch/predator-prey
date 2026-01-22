import numpy as np

class PredatorPreySimulation:
    """
    A simple predator-prey ecosystem simulation
    Prey (rabbits) reproduce and get eaten by predators (foxes)
    """
    
    def __init__(self, grid_size=50, num_prey=100, num_predators=20):
        """Set up the simulation grid and populations"""
        self.grid_size = grid_size
        
        # Create lists to store positions
        # Each animal is [x, y, energy]
        self.prey = []
        self.predators = []
        
        # Add prey at random positions
        for _ in range(num_prey):
            x = np.random.randint(0, grid_size)
            y = np.random.randint(0, grid_size)
            self.prey.append([x, y, 10])  # Start with 10 energy
        
        # Add predators at random positions
        for _ in range(num_predators):
            x = np.random.randint(0, grid_size)
            y = np.random.randint(0, grid_size)
            self.predators.append([x, y, 20])  # Start with 20 energy
        
        # Track population over time
        self.prey_history = []
        self.predator_history = []
    
    def move_animal(self, animal):
        """Move an animal one step in a random direction"""
        direction = np.random.randint(0, 4)
        
        if direction == 0:  # Up
            animal[1] = (animal[1] + 1) % self.grid_size
        elif direction == 1:  # Down
            animal[1] = (animal[1] - 1) % self.grid_size
        elif direction == 2:  # Right
            animal[0] = (animal[0] + 1) % self.grid_size
        else:  # Left
            animal[0] = (animal[0] - 1) % self.grid_size
        
        # Moving costs energy
        animal[2] -= 1
    
    def step(self):
        """Run one time step of the simulation"""
        
        # Move all prey
        for prey in self.prey:
            self.move_animal(prey)
        
        # Prey reproduce if they have enough energy
        new_prey = []
        for prey in self.prey:
            if prey[2] > 15 and np.random.random() < 0.1:
                # Create offspring nearby
                new_prey.append([prey[0], prey[1], 10])
                prey[2] -= 5  # Reproduction costs energy
        self.prey.extend(new_prey)
        
        # Move all predators
        for pred in self.predators:
            self.move_animal(pred)
        
        # Predators hunt prey
        prey_to_remove = []
        for pred in self.predators:
            for i, prey in enumerate(self.prey):
                # Check if predator and prey are at same location
                if pred[0] == prey[0] and pred[1] == prey[1]:
                    pred[2] += 15  # Predator gains energy from eating
                    prey_to_remove.append(i)
                    break  # Each predator can only eat once per step
        
        # Remove eaten prey (go backwards to avoid index issues)
        for i in sorted(prey_to_remove, reverse=True):
            del self.prey[i]
        
        # Predators reproduce if they have enough energy
        new_predators = []
        for pred in self.predators:
            if pred[2] > 30 and np.random.random() < 0.05:
                new_predators.append([pred[0], pred[1], 20])
                pred[2] -= 10
        self.predators.extend(new_predators)
        
        # Remove animals that ran out of energy (starved)
        self.prey = [p for p in self.prey if p[2] > 0]
        self.predators = [p for p in self.predators if p[2] > 0]
        
        # Record population sizes
        self.prey_history.append(len(self.prey))
        self.predator_history.append(len(self.predators))
    
    def run(self, num_steps=500):
        """Run the simulation for a number of steps"""
        print("Starting simulation...")
        print(f"Initial: {len(self.prey)} prey, {len(self.predators)} predators")
        
        for step in range(num_steps):
            self.step()
            
            # Print progress every 50 steps
            if (step + 1) % 50 == 0:
                print(f"Step {step + 1}: {len(self.prey)} prey, {len(self.predators)} predators")
            
            # Stop if either population dies out
            if len(self.prey) == 0 or len(self.predators) == 0:
                print(f"Simulation ended at step {step + 1}")
                break
        
        print("\nSimulation complete!")
        self.print_results()
    
    def print_results(self):
        """Print a simple text-based graph of populations"""
        print("\nPopulation History:")
        print("-" * 60)
        
        max_pop = max(max(self.prey_history), max(self.predator_history))
        
        for i in range(0, len(self.prey_history), 10):
            # Scale populations to fit in 30 characters
            prey_bar = int((self.prey_history[i] / max_pop) * 30)
            pred_bar = int((self.predator_history[i] / max_pop) * 30)
            
            print(f"Step {i:3d} | Prey: {'#' * prey_bar} ({self.prey_history[i]})")
            print(f"        | Pred: {'*' * pred_bar} ({self.predator_history[i]})")
            print()

# Run the simulation
sim = PredatorPreySimulation(grid_size=50, num_prey=100, num_predators=20)
sim.run(num_steps=300)

import math
import random
import matplotlib.pyplot as plt

def simulated_annealing_demo():
    # Generate sample values for nodes
    nodes = [random.uniform(0, 100) for _ in range(20)]
    print(f"Nodes: {nodes}")

   
    def acceptance_probability(current_value, next_value, temperature):
        if next_value > current_value:
            return 1.0
        return math.exp((next_value - current_value) / temperature)


    initial_temperature = 100
    cooling_rate = 0.9
    num_iterations = 10

   
    temperatures = []
    probabilities = []

    
    current_node = random.choice(nodes)
    temperature = initial_temperature

    print(f"Initial Node: {current_node}")

    for i in range(num_iterations):
        # Select a random next node
        next_node = random.choice(nodes)
        prob = acceptance_probability(current_node, next_node, temperature)

        
        temperatures.append(temperature)
        probabilities.append(prob)

       
        if prob > random.random():
            current_node = next_node

        
        temperature *= cooling_rate
    plt.figure(figsize=(10, 5))
    plt.plot(temperatures, probabilities, marker='o', label="Acceptance Probability")
    plt.xlabel("Temperature")
    plt.ylabel("Probability of Accepting Inferior Node")
    plt.title("Effect of Temperature on Acceptance Probability")
    plt.gca().invert_xaxis()
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    simulated_annealing_demo()

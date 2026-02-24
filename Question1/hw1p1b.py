import numpy as np


def simulate_7_steps():
    # Initial State
    x1, x2, x3 = 9, 8, 7
    
    # Run exactly 7 reaction steps
    for _ in range(7):
        # Calculate Propensities (a1, a2, a3)
        a1 = 0.5 * x1 * (x1 - 1) * x2
        a2 = x1 * x3 * (x3 - 1)
        a3 = 3 * x2 * x3
        
        a0 = a1 + a2 + a3
        
        # Deadlock check
        if a0 <= 0:
            break
            
        # Randomly select the next reaction
        r = np.random.rand() * a0
        
        # Execute Reaction
        if r < a1:
            # R1: 2X1 + X2 -> 4X3
            x1 -= 2
            x2 -= 1
            x3 += 4
        elif r < a1 + a2:
            # R2: X1 + 2X3 -> 3X2
            x1 -= 1
            x3 -= 2
            x2 += 3
        else:
            # R3: X2 + X3 -> 2X1
            x2 -= 1
            x3 -= 1
            x1 += 2

    return x1, x2, x3

if __name__ == "__main__":
    NUM_RUNS = 5000
    
    # Arrays to store the final states of all 1000 runs
    results_x1 = np.zeros(NUM_RUNS)
    results_x2 = np.zeros(NUM_RUNS)
    results_x3 = np.zeros(NUM_RUNS)
    
    print(f"Running {NUM_RUNS} stochastic simulations (7 steps each)...")
    
    for i in range(NUM_RUNS):
        final_x1, final_x2, final_x3 = simulate_7_steps()
        results_x1[i] = final_x1
        results_x2[i] = final_x2
        results_x3[i] = final_x3

    # Calculate Mean and Variance across the 1000 samples
    mean_x1, var_x1 = np.mean(results_x1), np.var(results_x1)
    mean_x2, var_x2 = np.mean(results_x2), np.var(results_x2)
    mean_x3, var_x3 = np.mean(results_x3), np.var(results_x3)
    

    # Used AI to help me print and save information to a txt file
    print("\n--- Monte Carlo Estimates ---")
    print(f"Initial State: S = [9, 8, 7]\n")
    
    print("Molecule X1:")
    print(f"  Mean:     {mean_x1:.4f}")
    print(f"  Variance: {var_x1:.4f}\n")
    
    print("Molecule X2:")
    print(f"  Mean:     {mean_x2:.4f}")
    print(f"  Variance: {var_x2:.4f}\n")
    
    print("Molecule X3:")
    print(f"  Mean:     {mean_x3:.4f}")
    print(f"  Variance: {var_x3:.4f}")

    filename = "hw1_p1b.txt"
    with open(filename, "w") as file:
        file.write("--- Monte Carlo Estimates ---\n")
        file.write("Initial State: S = [9, 8, 7]\n\n")
        
        file.write("Molecule X1:\n")
        file.write(f"  Mean:     {mean_x1:.4f}\n")
        file.write(f"  Variance: {var_x1:.4f}\n\n")
        
        file.write("Molecule X2:\n")
        file.write(f"  Mean:     {mean_x2:.4f}\n")
        file.write(f"  Variance: {var_x2:.4f}\n\n")
        
        file.write("Molecule X3:\n")
        file.write(f"  Mean:     {mean_x3:.4f}\n")
        file.write(f"  Variance: {var_x3:.4f}\n")
import numpy as np
import matplotlib.pyplot as plt


X0_val = 32    # Input value (e.g., 32 -> log2(32) = 5)
NUM_RUNS = 100 # Number of simulations to run

# Rate constants
# These were chosen by ChatGPT. They worked first try.
k_slow = 0.1
k_medium = 1.0
k_fast = 2.0
k_faster = 50.0 

# Comments from ChatGPT.
def run_simulation(X0):
    # Initialize molecule counts for this run
    X = X0
    Z = 0      # Output
    B = 1      # Clock (Constant)
    A = 0      # Clock Pulse / Catalyst
    C = 0      # Intermediate Pulse
    X_prime = 0 # Recycled X
    
    step_count = 0
    max_steps = 50000 # Safety limit

    while True:
        # Stop if computation is done (X < 2) and no active intermediates remain
        if X < 2 and C == 0 and X_prime == 0:
            break
        if step_count > max_steps:
            break
        step_count += 1

        reactions = []
        rates = []

        # 1. Clock: B -> A + B (slow)
        # B is constant, so this fires indefinitely to drive the system
        if B > 0:
            reactions.append('clock')
            rates.append(k_slow * B)
        
        # 2. Halving: A + 2X -> C + X' + A (faster)
        if A > 0 and X >= 2:
            reactions.append('halve_x')
            rates.append(k_faster * A * X * (X - 1) / 2)
        
        # 3. Consolidate: 2C -> C (faster)
        if C >= 2:
            reactions.append('consolidate_c')
            rates.append(k_faster * C * (C - 1) / 2)
        
        # 4. Decay Catalyst: A -> Null (fast)
        if A > 0:
            reactions.append('decay_a')
            rates.append(k_fast * A)
        
        # 5. Recycle X: X' -> X (medium)
        if X_prime > 0:
            reactions.append('recycle_xp')
            rates.append(k_medium * X_prime)
        
        # 6. Output: C -> Z (medium)
        if C > 0:
            reactions.append('output_z')
            rates.append(k_medium * C)
            
        if not rates:
            break
            
        total_rate = sum(rates)
        r = np.random.rand() * total_rate
        cumulative = 0
        chosen_rxn = None
        
        for i, rate in enumerate(rates):
            cumulative += rate
            if r < cumulative:
                chosen_rxn = reactions[i]
                break
        
        if chosen_rxn == 'clock':
            A += 1
        elif chosen_rxn == 'halve_x':
            X -= 2
            C += 1
            X_prime += 1
        elif chosen_rxn == 'consolidate_c':
            C -= 1
        elif chosen_rxn == 'decay_a':
            A -= 1
        elif chosen_rxn == 'recycle_xp':
            X_prime -= 1
            X += 1
        elif chosen_rxn == 'output_z':
            C -= 1
            Z += 1
            
    return Z


print(f"Running {NUM_RUNS} simulations with X0={X0_val}...")
results = []

for i in range(NUM_RUNS):
    res = run_simulation(X0_val)
    results.append(res)


# I used ChatGPT here to help me plot the results. 
# I don't really trust AI with doing the heavy lifting math, but have used it in the past
# for matplotlib things so I used it again. Changed a few things such as color and file name.

print(f"Unique results: {np.unique(results, return_counts=True)}")

plt.figure(figsize=(10, 6))
bins = np.arange(min(results) - 0.5, max(results) + 1.5, 1)
plt.hist(results, bins=bins, rwidth=0.8, color='skyblue', edgecolor='black')

plt.title(f'Distribution of Output Z over {NUM_RUNS} Runs (Input X0={X0_val})')
plt.xlabel('Final Value of Z')
plt.ylabel('Frequency')
plt.xticks(range(min(results), max(results) + 1))
plt.grid(axis='y', alpha=0.5)


plt.savefig('log_distribution.png')
plt.show()
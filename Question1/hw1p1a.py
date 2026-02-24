import numpy as np


def run_discrete_trajectory(max_steps=5000):
    # Initial State
    x1, x2, x3 = 110, 26, 55
    
    # Flags to track if conditions are met during this run
    hit_c1 = False
    hit_c2 = False
    hit_c3 = False
    
    for step in range(max_steps):
        # Check Conditions
        if x1 >= 150: hit_c1 = True
        if x2 < 10:   hit_c2 = True
        if x3 > 100:  hit_c3 = True
            
        # If all conditions are hit, can break early
        if hit_c1 and hit_c2 and hit_c3:
            break
            
        # Calculate Propensities, equations written here so I don't have to check PDF everytime
        # p1 scales with: 0.5 * x1 * (x1 - 1) * x2
        # p2 scales with: x1 * x3 * (x3 - 1)
        # p3 scales with: 3 * x2 * x3
        a1 = 0.5 * x1 * (x1 - 1) * x2
        a2 = x1 * x3 * (x3 - 1)
        a3 = 3 * x2 * x3
        
        a0 = a1 + a2 + a3
        
        # Deadlock check
        if a0 <= 0:
            break
            
        # Choose the next reaction
        r = np.random.rand() * a0
        
        # Execute Reaction and update state
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

    return hit_c1, hit_c2, hit_c3



NUM_SIMULATIONS = 1000

c1_count = 0
c2_count = 0
c3_count = 0

# I had AI help me with this part, not too familiar with printing strings
print(f"Running {NUM_SIMULATIONS} stochastic simulations...")

for _ in range(NUM_SIMULATIONS):
    c1, c2, c3 = run_discrete_trajectory()
    if c1: c1_count += 1
    if c2: c2_count += 1
    if c3: c3_count += 1

# Calculate Probabilities
pr_c1 = c1_count / float(NUM_SIMULATIONS)
pr_c2 = c2_count / float(NUM_SIMULATIONS)
pr_c3 = c3_count / float(NUM_SIMULATIONS)


# Used AI to help me print and save information to a txt file
print("\n--- Discrete Model (Stochastic) ---")
print(f"Estimated Pr(C1) [X1 >= 150]: {pr_c1:.4f}  ({c1_count}/{NUM_SIMULATIONS} runs)")
print(f"Estimated Pr(C2) [X2 < 10]:   {pr_c2:.4f}  ({c2_count}/{NUM_SIMULATIONS} runs)")
print(f"Estimated Pr(C3) [X3 > 100]:  {pr_c3:.4f}  ({c3_count}/{NUM_SIMULATIONS} runs)")

filename = "hw1_p1a.txt"
with open(filename, "w") as file:
    file.write("--- Discrete Model (Stochastic) ---\n")
    file.write(f"Estimated Pr(C1) [X1 >= 150]: {pr_c1:.4f}  ({c1_count}/{NUM_SIMULATIONS} runs)\n")
    file.write(f"Estimated Pr(C2) [X2 < 10]:   {pr_c2:.4f}  ({c2_count}/{NUM_SIMULATIONS} runs)\n")
    file.write(f"Estimated Pr(C3) [X3 > 100]:  {pr_c3:.4f}  ({c3_count}/{NUM_SIMULATIONS} runs)\n")

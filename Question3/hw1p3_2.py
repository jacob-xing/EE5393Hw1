import numpy as np
import matplotlib.pyplot as plt

X0_val = 64      # Initial Input X0 (Power of 2 makes life easy)
Y0_val = 1       # Initial Output Y0 (Must be 1 for exponentiation: 2^0 = 1)
NUM_RUNS = 100   # Number of runs

# Rate constants 
# Can notice these numbers are different, I chose them ad hoc 
# and played around with them until my output was something I was satisfied with.
k_slow = 0.05
k_medium = 1.0
k_fast = 50.0
k_faster = 10000.0 

# I put this into ChatGPT to add comments so I could track what I was doing. Not the best at naming variables.
def run_simulation(X0, Y0):
    # --- Initialize State ---
    # Logarithm Module Variables (X -> C)
    X = X0              # Input
    B = 1               # Clock Source
    A_log = 0           # Log Catalyst
    X_prime = 0         # Intermediate X
    
    # Temp Variable
    C = 0               # Signal Pulse (Output of Log, Input to Exp)
    
    # Exponentiation Module Variables (C -> Y)
    Y = Y0              # Final Output
    A_exp = 0           # Exp Catalyst
    Y_prime = 0         # Intermediate Y

    step_count = 0
    max_steps = 100000 

    while True:
        # --- TERMINATION CHECK ---
        # Simulation ends when:
        # 1. Log is done (X < 2, cannot halve anymore).
        # 2. All signals (C) have been processed.
        # 3. All catalysts and intermediates have cleared.
        if (X < 2 and C == 0 and A_log == 0 and X_prime == 0 and 
            A_exp == 0 and Y_prime == 0):
            break
        
        if step_count > max_steps:
            break
        step_count += 1

        # --- REACTION PROPENSITIES ---
        reactions = []
        rates = []

        # === LOGARITHM MODULE (X -> C) ===
        # R1: Clock Pulse [B -> A_log + B] (slow)
        if B > 0:
            reactions.append('clock_pulse')
            rates.append(k_slow * B)

        # R2: Halving [A_log + 2X -> C + X' + A_log] (faster)
        # Consumes 2X, produces 1 Signal (C)
        if A_log > 0 and X >= 2:
            reactions.append('halve_x')
            rates.append(k_faster * A_log * X * (X - 1) / 2)

        # R3: Consolidate Pulse [2C -> C] (faster)
        if C >= 2:
            reactions.append('consolidate_c')
            rates.append(k_faster * C * (C - 1) / 2)

        # R4: Decay Log Catalyst [A_log -> Null] (fast)
        if A_log > 0:
            reactions.append('decay_a_log')
            rates.append(k_fast * A_log)

        # R5: Recycle X [X' -> X] (medium)
        if X_prime > 0:
            reactions.append('recycle_xp')
            rates.append(k_medium * X_prime)

        # === EXPONENTIATION MODULE (C -> Y) ===
        # R6: Initiate Doubling [C -> A_exp] (slow/medium)
        # The signal C acts as the input to the Exp module
        if C > 0:
            reactions.append('init_exp')
            rates.append(k_medium * C)

        # R7: Doubling [A_exp + Y -> A_exp + 2Y'] (faster)
        # Consumes Y, produces 2Y' (doubling effect)
        if A_exp > 0 and Y > 0:
            reactions.append('double_y')
            rates.append(k_faster * A_exp * Y)

        # R8: Decay Exp Catalyst [A_exp -> Null] (fast)
        if A_exp > 0:
            reactions.append('decay_a_exp')
            rates.append(k_fast * A_exp)

        # R9: Recycle Y [Y' -> Y] (medium)
        if Y_prime > 0:
            reactions.append('recycle_yp')
            rates.append(k_medium * Y_prime)

        # --- EXECUTE REACTION ---
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
        
        # Log Logic
        if chosen_rxn == 'clock_pulse':
            A_log += 1
        elif chosen_rxn == 'halve_x':
            X -= 2
            C += 1
            X_prime += 1
        elif chosen_rxn == 'consolidate_c':
            C -= 1
        elif chosen_rxn == 'decay_a_log':
            A_log -= 1
        elif chosen_rxn == 'recycle_xp':
            X_prime -= 1
            X += 1
        # Exp Logic
        elif chosen_rxn == 'init_exp':
            C -= 1
            A_exp += 1
        elif chosen_rxn == 'double_y':
            Y -= 1
            Y_prime += 2
        elif chosen_rxn == 'decay_a_exp':
            A_exp -= 1
        elif chosen_rxn == 'recycle_yp':
            Y_prime -= 1
            Y += 1
            
    return Y


print(f"Running {NUM_RUNS} simulations for Y = 2^(log2 X0) with X0={X0_val}...")
results = []

for i in range(NUM_RUNS):
    res = run_simulation(X0_val, Y0_val)
    results.append(res)

# I used ChatGPT here to help me plot the results. 
# I don't really trust AI with doing the heavy lifting math, but have used it in the past
# for matplotlib things so I used it again. Changed a few things such as color and file name.

plt.figure(figsize=(10, 6))
bins = np.arange(min(results) - 2.5, max(results) + 2.5, 1) 

plt.hist(results, bins=bins, rwidth=0.8, color='lightgreen', edgecolor='black')
plt.title(f'Distribution of Final Output Y (Target: {X0_val})')
plt.xlabel('Final Value of Y')
plt.ylabel('Frequency')
plt.axvline(x=X0_val, color='red', linestyle='dashed', linewidth=2, label=f'Ideal Y={X0_val}')
plt.legend()
plt.grid(axis='y', alpha=0.5)

plt.savefig('log_distribution q3p2.png')
plt.show()

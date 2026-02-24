import numpy as np
import matplotlib.pyplot as plt

# I made these strings and then parsed them

lambda_r_text = """
OLRNAP 1 MOI 1 : OLRNAP 1 MOI 1 N 10 : 0.011
RNAP 1 PRE 1 : PRERNAP 1 : 0.01
PRERNAP 1 : RNAP 1 PRE 1 : 1.0
RNAP 1 cI2 1 OR 1 : OR13RNAPcI 1 : 0.02569
OR13RNAPcI 1 : RNAP 1 cI2 1 OR 1 : 1.0
RNAP 1 cI2 1 OR 1 : ORcIRNAP 1 : 0.00967
ORcIRNAP 1 : RNAP 1 cI2 1 OR 1 : 1.0
NUTR4 1 N 1 : NUTRN4 1 : 0.2
NUTRN4 1 : NUTR4 1 N 1 : 1.0
P1 1 cIII 1 : P1cIII 1 : 0.01
P1cIII 1 : P1 1 cIII 1 : 0.01
cI 1 : : 7.0E-4
cI2 1 OR 1 : ORcI 1 : 0.2165
ORcI 1 : cI2 1 OR 1 : 1.0
MOI 1 OR12RNAP 1 NUTRN 1 : MOI 1 OR12RNAP 1 NUTRN 1 cII 10 : 0.014
Basal_error 1 MOI 1 OR3RNAP 1 : Basal_error 1 MOI 1 OR3RNAP 1 cI 10 : 0.0010
ORcIRNAP 1 MOI 1 NUTRN3 1 : ORcIRNAP 1 MOI 1 NUTRN3 1 cII 10 : 0.014
ORCroRNAP 1 NUTRN4 1 MOI 1 : ORCroRNAP 1 NUTRN4 1 MOI 1 cII 10 : 0.014
NUTR 1 N 1 : NUTRN 1 : 0.2
NUTRN 1 : NUTR 1 N 1 : 1.0
Basal_error 1 MOI 1 OR13RNAPcI 1 : Basal_error 1 MOI 1 OR13RNAPcI 1 cI 10 : 0.0010
Cro 2 : Cro2 1 : 0.05
Cro2 1 : Cro 2 : 0.5
Cro2 1 RNAP 1 cI2 1 OR 1 : ORRNAPcICro 1 : 8.0E-5
ORRNAPcICro 1 : Cro2 1 RNAP 1 cI2 1 OR 1 : 1.0
N 1 NUTR3 1 : NUTRN3 1 : 0.2
NUTRN3 1 : N 1 NUTR3 1 : 1.0
OLRNAP 1 MOI 1 NUTL 1 : cIII 10 OLRNAP 1 MOI 1 NUTL 1 : 0.0022
Cro2 2 OL 1 : OL2Cro 1 : 0.0158
OL2Cro 1 : Cro2 2 OL 1 : 1.0
P2cII 1 : P2 1 : 0.6
NUTR 1 MOI 1 OR12RNAP 1 : NUTR 1 MOI 1 OR12RNAP 1 cII 10 : 0.0070
Cro2 2 RNAP 1 OR 1 : ORRNAP2Cro 1 : 2.6E-4
ORRNAP2Cro 1 : Cro2 2 RNAP 1 OR 1 : 1.0
RNAP 1 OR 1 : OR12RNAP 1 : 0.69422
OR12RNAP 1 : RNAP 1 OR 1 : 1.0
P2cIII 1 : P2 1 : 0.0010
cI2 1 OL 1 : OLcI 1 : 0.2025
OLcI 1 : cI2 1 OL 1 : 1.0
P1 1 cII 1 : P1cII 1 : 0.0002
P1cII 1 : P1 1 cII 1 : 0.05
N 1 : : 0.00231
PRE 1 cII 1 : PREcII 1 : 0.00726
PREcII 1 : PRE 1 cII 1 : 1.0
Cro2 1 cI2 1 OR 1 : ORCrocI 1 : 0.1779
ORCrocI 1 : Cro2 1 cI2 1 OR 1 : 1.0
P1cII 1 : P1 1 : 0.6
OR2RNAP 1 MOI 1 NUTR2 1 : OR2RNAP 1 MOI 1 NUTR2 1 cII 10 : 0.0070
MOI 1 PREcIIRNAP 1 : MOI 1 cI 10 PREcIIRNAP 1 : 0.015
ORCroRNAP 1 MOI 1 : Cro 10 ORCroRNAP 1 MOI 1 : 0.014
RNAP 1 cI2 1 OR 1 : ORRNAPcI 1 : 0.0019
ORRNAPcI 1 : RNAP 1 cI2 1 OR 1 : 1.0
cI 2 : cI2 1 : 0.05
cI2 1 : cI 2 : 0.5
ORcIRNAP 1 MOI 1 NUTR3 1 : ORcIRNAP 1 MOI 1 NUTR3 1 cII 10 : 0.0070
ORRNAPcICro 1 MOI 1 Kd 1 : ORRNAPcICro 1 MOI 1 cI 10 Kd 1 : 0.011
cI2 3 OR 1 : OR3cI 1 : 8.1E-4
OR3cI 1 : cI2 3 OR 1 : 1.0
Cro2 2 OR 1 : OR2Cro 1 : 0.03342
OR2Cro 1 : Cro2 2 OR 1 : 1.0
cI2 2 OL 1 : OL2cI 1 : 0.058
OL2cI 1 : cI2 2 OL 1 : 1.0
OLRNAP 1 NUTLN 1 MOI 1 : cIII 10 OLRNAP 1 NUTLN 1 MOI 1 : 0.011
MOI 1 ORRNAP2cI 1 Kd 1 : MOI 1 ORRNAP2cI 1 cI 10 Kd 1 : 0.011
Cro2 1 RNAP 1 OR 1 : ORRNAPCro 1 : 0.01186
ORRNAPCro 1 : Cro2 1 RNAP 1 OR 1 : 1.0
ORcIRNAP 1 MOI 1 : ORcIRNAP 1 Cro 10 MOI 1 : 0.014
Cro2 1 cI2 1 OL 1 : OLcICro 1 : 0.014
OLcICro 1 : Cro2 1 cI2 1 OL 1 : 1.0
MOI 1 PRERNAP 1 : MOI 1 cI 10 PRERNAP 1 : 4.0E-5
N 1 NUTL 1 : NUTLN 1 : 0.2
NUTLN 1 : N 1 NUTL 1 : 1.0
NUTR4 1 ORCroRNAP 1 MOI 1 : NUTR4 1 ORCroRNAP 1 MOI 1 cII 10 : 0.0070
Basal_error 1 MOI 1 ORRNAPCro 1 : Basal_error 1 MOI 1 cI 10 ORRNAPCro 1 : 0.0010
RNAP 1 OR 1 : OR3RNAP 1 : 0.1362
OR3RNAP 1 : RNAP 1 OR 1 : 1.0
Cro2 1 cI2 2 OR 1 : ORCro2cI 1 : 0.02133
ORCro2cI 1 : Cro2 1 cI2 2 OR 1 : 1.0
Cro2 1 RNAP 1 OR 1 : ORCroRNAP 1 : 0.25123
ORCroRNAP 1 : Cro2 1 RNAP 1 OR 1 : 1.0
RNAP 1 PRE 1 cII 1 : PREcIIRNAP 1 : 0.00161
PREcIIRNAP 1 : RNAP 1 PRE 1 cII 1 : 1.0
Cro2 1 PRE 1 : PRECro 1 : 1.0E-5
PRECro 1 : Cro2 1 PRE 1 : 0.1
Basal_error 1 MOI 1 ORRNAP2CrocI 1 : Basal_error 1 MOI 1 ORRNAP2CrocI 1 cI 10 : 0.0010
Cro 1 : : 0.0025
P2 1 cII 1 : P2cII 1 : 2.5E-4
P2cII 1 : P2 1 cII 1 : 0.065
cI2 2 OR 1 : OR2cI 1 : 0.06568
OR2cI 1 : cI2 2 OR 1 : 1.0
P1cIII 1 : P1 1 : 0.001
RNAP 2 OR 1 : OR2RNAP 1 : 0.09455
OR2RNAP 1 : RNAP 2 OR 1 : 1.0
Cro2 2 cI2 1 OR 1 : OR2CrocI 1 : 0.00322
OR2CrocI 1 : Cro2 2 cI2 1 OR 1 : 1.0
OR2RNAP 1 Basal_error 1 MOI 1 : OR2RNAP 1 Basal_error 1 MOI 1 cI 10 : 0.0010
cIII 1 P2 1 : P2cIII 1 : 0.01
P2cIII 1 : cIII 1 P2 1 : 0.01
Cro2 1 OR 1 : ORCro 1 : 0.449
ORCro 1 : Cro2 1 OR 1 : 1.0
Cro2 3 OR 1 : OR3Cro 1 : 6.9E-4
OR3Cro 1 : Cro2 3 OR 1 : 1.0
Cro2 1 OL 1 : OLCro 1 : 0.4132
OLCro 1 : Cro2 1 OL 1 : 1.0
ORRNAP2Cro 1 Basal_error 1 MOI 1 : ORRNAP2Cro 1 Basal_error 1 MOI 1 cI 10 : 0.0010
Cro2 1 RNAP 1 cI2 1 OR 1 : ORRNAP2CrocI 1 : 0.00112
ORRNAP2CrocI 1 : Cro2 1 RNAP 1 cI2 1 OR 1 : 1.0
RNAP 1 cI2 2 OR 1 : ORRNAP2cI 1 : 0.0079
ORRNAP2cI 1 : RNAP 1 cI2 2 OR 1 : 1.0
N 1 NUTR2 1 : NUTRN2 1 : 0.2
NUTRN2 1 : N 1 NUTR2 1 : 1.0
MOI 1 OR12RNAP 1 : Cro 10 MOI 1 OR12RNAP 1 : 0.014
OR2RNAP 1 MOI 1 NUTRN2 1 : OR2RNAP 1 MOI 1 NUTRN2 1 cII 10 : 0.014
OR2RNAP 1 MOI 1 : Cro 10 OR2RNAP 1 MOI 1 : 0.014
MOI 1 ORRNAPcI 1 Kd 1 : ORRNAPcI 1 MOI 1 cI 10 Kd 1 : 0.011
RNAP 1 OL 1 : OLRNAP 1 : 0.6942
OLRNAP 1 : RNAP 1 OL 1 : 1.0
"""

lambda_in_text = """
cI2 0 GE 145
Cro2 0 GE 55
MOI 6 N
P1cIII 0 N
ORCrocI 0 N
NUTRN4 0 N
OR13RNAPcI 0 N
Kd 1 N
ORCro2cI 0 N
N 0 N
ORcI 0 N
PRECro 0 N
OR 1 N
ORCro 0 N
PRE 1 N
ORRNAP2CrocI 0 N
NUTRN2 0 N
OLCro 0 N
P2cIII 0 N
ORRNAPcICro 0 N
OR2RNAP 0 N
P2 100 N
OR2cI 0 N
OR3cI 0 N
PREcIIRNAP 0 N
ORRNAPCro 0 N
NUTR4 1 N
NUTL 1 N
OR12RNAP 0 N
OLcI 0 N
ORCroRNAP 0 N
Cro 0 N
ORRNAP2Cro 0 N
NUTRN3 0 N
Basal_error 1 N
ORcIRNAP 0 N
cIII 0 N
P1cII 0 N
PREcII 0 N
OLcICro 0 N
OL 1 N
OR3RNAP 0 N
OL2Cro 0 N
cI 0 N
OR2Cro 0 N
ORRNAP2cI 0 N
OL2cI 0 N
NUTLN 0 N
OR2CrocI 0 N
P1 40 N
RNAP 30 N
NUTR 1 N
NUTR3 1 N
OLRNAP 0 N
PRERNAP 0 N
cII 0 N
P2cII 0 N
ORRNAPcI 0 N
OR3Cro 0 N
NUTR2 1 N
NUTRN 0 N
"""

def parse_initial_conditions(text_data):
    initial_state = {}
    lines = text_data.strip().split('\n')
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2:
            name = parts[0]
            count = int(parts[1])
            initial_state[name] = count
    return initial_state

def parse_reactions(text_data):
    reactions = []
    lines = text_data.strip().split('\n')
    for line in lines:
        if not line.strip(): continue
        
        segments = line.split(':')
        if len(segments) != 3: continue
        
        reactant_str = segments[0].strip()
        product_str = segments[1].strip()
        rate_str = segments[2].strip()
        
        reactants = {}
        r_parts = reactant_str.split()
        for i in range(0, len(r_parts), 2):
            r_name = r_parts[i]
            r_count = int(r_parts[i+1])
            reactants[r_name] = reactants.get(r_name, 0) + r_count
            
        products = {}
        p_parts = product_str.split()
        for i in range(0, len(p_parts), 2):
            p_name = p_parts[i]
            p_count = int(p_parts[i+1])
            products[p_name] = products.get(p_name, 0) + p_count
            
        net_change = {}
        all_species = set(reactants.keys()) | set(products.keys())
        for s in all_species:
            change = products.get(s, 0) - reactants.get(s, 0)
            if change != 0:
                net_change[s] = change
                
        reactions.append({
            'reactants': reactants,
            'change': net_change,
            'k': float(rate_str)
        })
    return reactions

def run_lambda_gillespie(initial_state, reactions, moi_val):
    state = initial_state.copy()
    state['MOI'] = moi_val 
    
    time = 0.0
    step = 0
    max_steps = 150000 
    
    while step < max_steps:
        cI2 = state.get('cI2', 0)
        Cro2 = state.get('Cro2', 0)
        
        if cI2 > 145:
            return "Stealth"
        if Cro2 > 55:
            return "Hijack"
            
        propensities = []
        total_rate = 0.0
        
        for rxn in reactions:
            h = rxn['k']
            possible = True
            for r_name, r_needed in rxn['reactants'].items():
                available = state.get(r_name, 0)
                if available < r_needed:
                    possible = False
                    break
                
                if r_needed == 1:
                    h *= available
                elif r_needed == 2:
                    h *= available * (available - 1) * 0.5
                elif r_needed == 3:
                    h *= available * (available - 1) * (available - 2) * (1.0/6.0)
            
            if possible and h > 0:
                propensities.append(h)
                total_rate += h
            else:
                propensities.append(0.0)
                
        if total_rate == 0:
            return "Stalled"
            
        dt = -np.log(np.random.random()) / total_rate
        time += dt
        
        r = np.random.random() * total_rate
        cumulative = 0.0
        chosen_idx = -1
        for i, p in enumerate(propensities):
            cumulative += p
            if r < cumulative:
                chosen_idx = i
                break
        
        rxn = reactions[chosen_idx]
        for s_name, s_change in rxn['change'].items():
            state[s_name] = state.get(s_name, 0) + s_change
            
        step += 1
        
    return "Undecided" 


initial_template = parse_initial_conditions(lambda_in_text)
reaction_list = parse_reactions(lambda_r_text)

moi_values = range(1, 11) 
stealth_probs = []
hijack_probs = []
runs_per_moi = 100 

print(f"Running simulation for MOI 1 to 10 ({runs_per_moi} trials each)...")
print("This might take a minute depending on your computer's speed.")

for moi in moi_values:
    outcomes = {'Stealth': 0, 'Hijack': 0, 'Undecided': 0}
    
    for _ in range(runs_per_moi):
        result = run_lambda_gillespie(initial_template, reaction_list, moi)
        outcomes[result] += 1
        

    # Only count the runs that successfully reached a decision to ensure P(S) + P(H) = 1
    total_decided = outcomes['Stealth'] + outcomes['Hijack']
    
    if total_decided > 0:
        p_stealth = outcomes['Stealth'] / total_decided
        p_hijack = outcomes['Hijack'] / total_decided
    else:
        # Failsafe in case all 100 runs stall (highly unlikely)
        p_stealth = 0.5 
        p_hijack = 0.5
    
    stealth_probs.append(p_stealth)
    hijack_probs.append(p_hijack) 
    
    print(f"MOI {moi}: Stealth {outcomes['Stealth']}, Hijack {outcomes['Hijack']}, Undecided {outcomes['Undecided']} | (P(Stealth)={p_stealth:.2f}, P(Hijack)={p_hijack:.2f})")

# Generated from AI
plt.figure(figsize=(9, 6))


plt.plot(moi_values, stealth_probs, marker='o', linestyle='-', color='purple', linewidth=2, label='Stealth (Lysogeny)')
plt.plot(moi_values, hijack_probs, marker='s', linestyle='--', color='red', linewidth=2, label='Hijack (Lysis)')

plt.title('Lambda Phage Decision: Lysogeny vs. Lysis Probability by MOI')
plt.xlabel('Multiplicity of Infection (MOI)')
plt.ylabel('Probability')
plt.ylim(-0.1, 1.1)
plt.grid(True, alpha=0.3)
plt.xticks(moi_values)
plt.legend(loc='best') 
plt.savefig('lambda_phage_decision_curves.png')

plt.show()
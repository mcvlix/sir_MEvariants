# main.py
import matplotlib.pyplot as plt
import numpy as np
import random
import copy

# Import the required functions from your modules
from sir_MEvariants import odeMutations
from simulation import plotMutations, prepareICs, plotAvgBetaAndGamma

# ===================================================
# STEP 1: Create 50 initial conditions (ICs)
# ===================================================

# Original initial conditions (ic2)
ic2 = {
    "string": "This set of ICs is an example of three non-recoverable initial variants with differing mutation chances at each timestep: First is dominant w/ low mutation chances. Second and Third are much less dominant with high mutation chances.",
    "tMax": 200,
    "virV": [0.005, 0.005, 0.0005],
    "Istart": [0.02, 0.01, 0.01],
    "betastart": [0.1, 0.2, 0.1],
    "gammastart": [0.0, 0.0, 0.0],
    "pMutationstart": [0.005, 0.02, 0.02]
}

# Initialize the list of initial conditions with the original one.
ics = [ic2]

# We want a total of 50 ICs; since we already have one, generate 49 additional variants.
n_variants = 49

for i in range(n_variants):
    new_ic = copy.deepcopy(ic2)
    
    # Randomize the scalar 'tMax' by ±5%
    new_ic["tMax"] = int(new_ic["tMax"] * random.uniform(0.95, 1.05))
    
    # Randomize each list-valued parameter by ±5%
    keys_to_randomize = ["virV", "Istart", "betastart", "gammastart", "pMutationstart"]
    for key in keys_to_randomize:
        new_ic[key] = [val * random.uniform(0.95, 1.05) for val in new_ic[key]]
    
    # Optionally update the description string to indicate the variant number.
    new_ic["string"] = f"Variant {len(ics) + 1}: " + new_ic["string"]
    
    # Append the new variant to our list
    ics.append(new_ic)

# Optional: Print all initial conditions for verification
for idx, ic in enumerate(ics, start=1):
    print(f"ic{idx} =", ic, "\n")

# ===================================================
# STEP 2: Run simulations for each initial condition
# ===================================================

# We assume that odeMutations returns three outputs:
#    y, avgBetaOnTime, avgGammaOnTime
# For the purpose of the expected-value plot, we treat:
#    α ≡ avgBetaOnTime, and β ≡ avgGammaOnTime.
#
# (If your model uses a different interpretation, adjust the names accordingly.)

allAlpha = []   # To store the "α" curves (avgBetaOnTime)
allBeta  = []   # To store the "β" curves (avgGammaOnTime)

# Loop over all initial conditions and run the simulation
for i, ic in enumerate(ics):
    # Clean parameters for this simulation
    odeparams = prepareICs(ic, i)
    
    # Run the simulation (odeMutations)
    y, avgBetaOnTime, avgGammaOnTime = odeMutations(*odeparams)
    
    # (Optionally, you might plot the population curves here)
    # plotMutations(y)
    # plotAvgBetaAndGamma(avgBetaOnTime, avgGammaOnTime)
    
    # Convert the returned time-series to NumPy arrays (for averaging)
    allAlpha.append(np.array(avgBetaOnTime, dtype=float))
    allBeta.append(np.array(avgGammaOnTime, dtype=float))

# ===================================================
# STEP 3: Align and average the parameter curves
# ===================================================

# The error you encountered indicates that the curves are of different lengths.
# We find the minimum length among all curves, and truncate each time-series to that length.
min_len_alpha = min(len(alpha) for alpha in allAlpha)
min_len_beta  = min(len(beta) for beta in allBeta)
min_len = min(min_len_alpha, min_len_beta)

# Truncate each curve to the minimum length so they all align
aligned_alpha = np.array([alpha[:min_len] for alpha in allAlpha])
aligned_beta  = np.array([beta[:min_len] for beta in allBeta])

# Compute the expected (average) curves elementwise
expected_alpha = np.mean(aligned_alpha, axis=0)
expected_beta  = np.mean(aligned_beta, axis=0)

# Compute the ratio: expected α divided by expected β at each timestep
expected_ratio = expected_alpha / expected_beta

# ===================================================
# STEP 4: Plot the expected curves and ratio
# ===================================================

plt.figure(figsize=(10, 6))
plt.plot(expected_alpha, label="Expected α (avgBetaOnTime)", linewidth=2)
plt.plot(expected_beta, label="Expected β (avgGammaOnTime)", linewidth=2)
plt.plot(expected_ratio, label="α / β", linewidth=2, linestyle="--")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Expected α, β, and (α/β) Over 50 Iterations")
plt.legend()
plt.grid(True)
plt.show()

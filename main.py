
# ================================================
# WHAT THE FIGURE SHOWS

# the figure shows the expected values of alpha (avgBetaOnTime) and beta (avgGammaOnTime) 
# (yes i know we used alpha and beta in one set and beta gamma in the other.)
# over 50 iterations of the simulation, along with the ratio of alpha to beta at each timestep.
# the expected values are computed by averaging the results from all 50 iterations, 
# and the ratio is calculated by dividing the expected α by the expected β at each timestep. 
# the plot provides insights into how these parameters evolve over time and their relative relationship.
# the fact that the ratio remains constant / slowly decreases forever after a point suggests that 
# we have successfully found a variation pattern that tends towards infectivity rather than lethality.

# ================================================


import matplotlib.pyplot as plt
import numpy as np
import random
import copy

# import the required functions from your modules
from sir_MEvariants import odeMutations
from simulation import plotMutations, prepareICs, plotAvgBetaAndGamma

# STEP 1: Create 50 initial conditions (ICs)

# original initial conditions (ic2)
ic2 = {
    "string": "This set of ICs is an example of three non-recoverable initial variants with differing mutation chances at each timestep: First is dominant w/ low mutation chances. Second and Third are much less dominant with high mutation chances.",
    "tMax": 200,
    "virV": [0.005, 0.005, 0.0005],
    "Istart": [0.02, 0.01, 0.01],
    "betastart": [0.1, 0.2, 0.1],
    "gammastart": [0.0, 0.0, 0.0],
    "pMutationstart": [0.005, 0.02, 0.02]
}

# initialize the list of initial conditions with the original one.
ics = [ic2]

# we want a total of 50 ICs; since we already have one, generate 49 additional variants.
n_variants = 49

for i in range(n_variants):
    new_ic = copy.deepcopy(ic2)
    
    # randomize tMax by 5% up or down
    new_ic["tMax"] = int(new_ic["tMax"] * random.uniform(0.95, 1.05))
    
    # Randomize each list-valued parameter by 5% up or down
    keys_to_randomize = ["virV", "Istart", "betastart", "gammastart", "pMutationstart"]
    for key in keys_to_randomize:
        new_ic[key] = [val * random.uniform(0.95, 1.05) for val in new_ic[key]]
    
    # update the description string to indicate the variant number
    new_ic["string"] = f"Variant {len(ics) + 1}: " + new_ic["string"]
    
    # append the new variant to our list
    ics.append(new_ic)

# STEP 2: run simulations for each initial condition
# we assume that odeMutations returns three outputs:
#    y, avgBetaOnTime, avgGammaOnTime
# for the purpose of the expected-value plot, we treat:
#    α ≡ avgBetaOnTime, and β ≡ avgGammaOnTime.

allAlpha = []   # to store the alpha curves (avgBetaOnTime)
allBeta  = []   # to store the beta curves (avgGammaOnTime)

# loop over all initial conditions and run the simulation
for i, ic in enumerate(ics):
    # clean parameters for this simulation
    odeparams = prepareICs(ic, i)
    
    # run the simulation
    y, avgBetaOnTime, avgGammaOnTime = odeMutations(*odeparams)
    
    # uncomment below if you want to plot the population curves first
    # plotMutations(y)
    # plotAvgBetaAndGamma(avgBetaOnTime, avgGammaOnTime)
    
    # convert the returned time-series to NumPy arrays (for averaging)
    allAlpha.append(np.array(avgBetaOnTime, dtype=float))
    allBeta.append(np.array(avgGammaOnTime, dtype=float))

# STEP 3: align and average the parameter curves

# we find the minimum length among all curves, and truncate each time-series to that length. this makes the code tidy
min_len_alpha = min(len(alpha) for alpha in allAlpha)
min_len_beta  = min(len(beta) for beta in allBeta)
min_len = min(min_len_alpha, min_len_beta)

# truncate each curve to the minimum length so they all align
aligned_alpha = np.array([alpha[:min_len] for alpha in allAlpha])
aligned_beta  = np.array([beta[:min_len] for beta in allBeta])

# compute the expected curves elementwise
expected_alpha = np.mean(aligned_alpha, axis=0)
expected_beta  = np.mean(aligned_beta, axis=0)

# compute the ratio: expected alpha divided by expected beta at each timestep
expected_ratio = expected_alpha / expected_beta

# STEP 4: plot the expected curves and ratio
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
plt.savefig("expected_alpha_beta_ratio.png")

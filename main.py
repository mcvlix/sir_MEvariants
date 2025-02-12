import matplotlib.pyplot as plt
import numpy as numpy


from sir_MEvariants import odeMutations
from simulation import plotMutations, prepareICs, plotAvgBetaAndGamma

# Initial parameters
# tMax                                - no. timesteps
# virV    = [vbeta,vgamma,vpMutation] - variance of each parameter upon mutation (=sd**2)
# betastart                           - transmission rate
# gammastart                          - recovery rate
# pMutationstart                      - probability of mutation on each timestep               

# IMPORTANT: ENSURE Istart, betastart, gammastart, pMutationstart all same length
# (each initial variant is parameterized)

'''
ic1 = {
"string": "This set of ICs is a basic example of one non-recoverable initial variant with 0.02 mutation chances at each timestep.",
"tMax":           100,
"virV":          [0.005, 0.005, 0.0005],
"Istart":        [0.01],
"betastart":     [0.3],
"gammastart":    [0.1],
"pMutationstart":[0.02],
}
'''
import random
import copy

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

# Initialize the list with ic2 as the first element
ics = [ic2]

# Number of new variants to generate
n_variants = 10

for i in range(n_variants):
    # Create a deep copy of ic2 so we don't modify the original
    new_ic = copy.deepcopy(ic2)
    
    # Randomize the scalar 'tMax' within ±5%
    new_ic["tMax"] = int(new_ic["tMax"] * random.uniform(0.95, 1.05))
    
    # Keys whose values are lists that need to be randomized
    keys_to_randomize = ["virV", "Istart", "betastart", "gammastart", "pMutationstart"]
    for key in keys_to_randomize:
        # For each element in the list, multiply by a random factor between 0.95 and 1.05
        new_ic[key] = [val * random.uniform(0.95, 1.05) for val in new_ic[key]]
    
    # Optionally, update the description string to include the variant number.
    # Here, len(ics) + 1 gives the new variant's number.
    new_ic["string"] = f"Variant {len(ics) + 1}: " + new_ic["string"]
    
    # Append the new variant to the list of initial conditions
    ics.append(new_ic)

# Optional: Print out all variants to verify
for idx, ic in enumerate(ics, start=1):
    print(f"ic{idx} =", ic, "\n")

allOdeBeta = []
allOdeGamma = []
for i in range(len(ics)):

    

    # clean parameters
    odeparams = prepareICs(ics[i], i)
    # run odeMutations
    y,avgBetaOnTime,avgGammaOnTime = odeMutations(*odeparams)
    # plot
    #plotMutations(y)
    #plotAvgBetaAndGamma(avgBetaOnTime, avgGammaOnTime)
    allOdeBeta.append(avgBetaOnTime)
    allOdeGamma.append(avgGammaOnTime)
    
for i in range(2):
    odeparams = prepareICs(ics[i], i)
    # run odeMutations
    y,avgBetaOnTime,avgGammaOnTime = odeMutations(*odeparams)
    # plot
    #plotMutations(y)
    #plotAvgBetaAndGamma(avgBetaOnTime, avgGammaOnTime)
    allOdeBeta.append(avgBetaOnTime)
    allOdeGamma.append(avgGammaOnTime)
print(allOdeBeta)
print(allOdeGamma)

#ExpectedBetaPath = numpy.sum(allOdeBeta, axis=1)
#ExpectedGammaPath = numpy.sum(allOdeGamma, axis=1)
#plotAvgBetaAndGamma(ExpectedBetaPath, ExpectedGammaPath)



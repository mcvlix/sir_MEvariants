import matplotlib.pyplot as plt
import numpy as numpy


from sir_MEvariants import odeMutations
from simulation import plotMutations, prepareICs

# Initial parameters
# tMax                                - no. timesteps
# virV    = [vbeta,vgamma,vpMutation] - variance of each parameter upon mutation (=sd**2)
# betastart                           - transmission rate
# gammastart                          - recovery rate
# pMutationstart                      - probability of mutation on each timestep               

# IMPORTANT: ENSURE Istart, betastart, gammastart, pMutationstart all same length
# (each initial variant is parameterized)


ic1 = {
"string": "This set of ICs is a basic example of one non-recoverable initial variant with 0.02 mutation chances at each timestep.",
"tMax":           100,
"virV":          [0.005, 0.005, 0.0005],
"Istart":        [0.01],
"betastart":     [0.2],
"gammastart":    [0.00],
"pMutationstart":[0.02],
}

ic2 = {
"string": "This set of ICs is an example of three non-recoverable initial variants with differing mutation chances at each timestep: First is dominant w/ low mutation chances. Second and Third are much less dominant with high mutation chances.",
"tMax":           100,
"virV":          [0.005, 0.005, 0.0005],
"Istart":        [0.02, 0.01, 0.01],
"betastart":     [0.1, 0.2, 0.1],
"gammastart":    [0.0, 0.0, 0.0],
"pMutationstart":[0.005,0.02, 0.02]
}

ics = [ic1, ic2]

for i in range(len(ics)):

    

    # clean parameters
    odeparams = prepareICs(ics[i], i)
    # run odeMutations
    y = odeMutations(*odeparams)
    # plot
    plotMutations(y)


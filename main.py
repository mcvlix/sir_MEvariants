import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define initial parameters
# Initial A, B, P, POPSHIFT, variances, tmax
#IMPORTANT: 
    #I added POPSHIFT = a walking variable that determines 
    #how much of a virus's population will shift to the new variant 
    #in the event that a new variant is created. this solves the problem
    #of determining the initial population of a new variant
    
    #NOTES: this could be better implemented as a (possibly stochastic) function related to A
    #for tuesday, maybe we just say POPSHIFT = 2A


vir = [ #virus parameters
    [0.3,0.2,0.1,0.2] #init virus has (A,B,P,POPSHIFT) = (0.3,0.2,0.1,0.2)
]
#variances = ?
tmax = 300


#
# Define ICs. aka ystart
ystart = (0.99,0.1,0) # init pop is (0.99,0.1,0) in S,I,R, respectively


# Run Simulation

#what we need is the following:

'''
and then we're done! if we reach t 200 and there is still at least one variant running, then we're good!
'''




# Plot evolution of A,B,P in t
# Plot SIR model itself with total infected
# Plot SIR model with individual infected
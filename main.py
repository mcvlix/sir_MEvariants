import matplotlib.pyplot as plt
import pandas as pd

from sir_MEvariants import odeMutations

# Define initial parameters
# Initial A, B, P, variances, tmax

virP = [[0.3,0.2,0.1],[0.3,0.2,0.1]] # [beta,gamma,pMutation] - initial virus parameters
virV = [0.05, 0.05, 0.05] # = [vbeta,vgamma,vpMutation]
tMax = 20

# Define ICs. aka ystart
ystart = [0.98,[0.01, 0.01],0] # init pop is (0.99,0.1,0) in S,I,R, respectively

# Run Simulation

y = odeMutations(virP, virV, tMax, ystart)

# variants = []
# for t in range(y.shape[0]):
#     variants.append(y[t][1:-1])

# print(variants)

#what we need is the following:

# Plot evolution of A,B,P in t
# Plot SIR model itself with total infected
# Plot SIR model with individual infecte

print(y)

S = [t[0] for t in y]
R = [t[2] for t in y]

plt.plot(S, label="Susceptible")
plt.plot(R, label="Recovered")

# for i in range(0,len(y[-1][1])):
#     V = [t[1][i] for t in y]
#     print(V)
#     plt.plot(V, label= f"Variant {i}")

plt.legend()
plt.show()
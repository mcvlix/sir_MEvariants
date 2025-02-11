# code to run entire simulation
import numpy as np

'''
each timestep
for all viruses (vir(n)):
    walk a,b,p
        IMPORTANT: this walking is not modifying vir(n). 
            it is only used as input data for the formation of vir(n+1) if vir(n+1) is indeed created. (see next line)
    if p hits
        insert new virus at n+1
        use the walked a,b,p to create a new variant at vir(n+1)
        determine % of population present in I(n+1), subtract that from I(n)
     use whatever our method is to favor more infectious & less deadly diseases 
        IMPORTANT: we must figure how to do this in a way that is NOT just a hardcode
'''

'discreteMutation - iterates over current I and uses probability to simulate probabilistic mutations'
def discreteMutation(virP, virV, Inew, t):

    nV = len(Inew) # number of Variants = length of I 
    pM = np.random.rand(nV)

    vbeta      = virV[0]
    vgamma     = virV[1]
    vpMutation = virV[2]
    
    newMutations = 0
    newVariants  = []

    # loop over all variants
    for i in range(0, nV):

        # Simulate mutation each time probability is met
        pMutation = virP[i][2]
        if pM[i] <= pMutation:         

            # population transfer
            nMutation = pMutation * Inew[i]
            Inew[i] -= nMutation

            newVariants.append(nMutation) # add to newVariants

            # carry new parameters in virP (TODO: APPLY VARIANCE TO PARAMETERS)
            prevP = virP[i]
            # apply variances using normal distribution
            newvirP = [np.random.normal(virP[i][j], (virV[j]**0.5)) for j in range(len(virP[0]))] 

            # ensure 
            for j in range(len(newvirP)):
                if newvirP[j] < 0:
                    newvirP[j] = 0
        
            virP.append(newvirP) # append new parameters 
            
            newMutationIndex = len(virP) - 1  # access index for printing
            print(f'Timestep {t}: variant {i} has mutated to variant {newMutationIndex}.\n prevP = {prevP}\n newvirP = {newvirP}')

        # print(f'Timestep {t}: total Mutations: {nV + newMutations + 1}')
    Inew.extend(newVariants)
        

# Built off SIR model ODE solver
def odeMutations(virP, virV, tmax, ystart):

    y = [ystart]

    for t in range(0, tmax):

        # Run mutation before integrating 

        # S,I,R values and parameters
        # I is instead compartmentalized into an array where p(Variant v) = I[v]
        S = y[t][0]
        I = y[t][1].copy()
        R = y[t][2]   

        # Initialize accumulators for the changes
        delta_S = 0
        delta_I = [0] * len(I)  # one delta for each variant
        delta_R = 0

        # Compute the change for each variant based on the original S
        for v in range(len(I)):

            beta = virP[v][0]  # transmission v
            gamma = virP[v][1]  # recovery v
            pMutation = virP[v][2]  # mutation probability v 

            dS = - beta * S * I[v]
            dI = (beta * S * I[v]) - (gamma * I[v])
            dR = gamma * I[v]

            delta_S += dS
            delta_I[v] = dI
            delta_R += dR
            
        # Update the state after all variant contributions are computed
        Snew = S + delta_S
        Inew = [I[v] + delta_I[v] for v in range(len(I))]
        Rnew = R + delta_R

        # apply mutation after iterating
        discreteMutation(virP,virV,Inew,t) 
        y.append([Snew, Inew, Rnew])

    return y
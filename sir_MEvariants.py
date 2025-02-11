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

def discreteMutation(virP, virV, y, t):

    nV = y.shape[1]-2
    pM = np.random.rand(nV)
    
    # loop over all I
    for i in range(0, nV):
        # run classical probability
        if pM[i] <= virP[i-1][2]:

            mutationIndex = len(y[1]) - 2

            print(f'Timestep {t}: variant {i} has mutated to variant {mutationIndex}.')

            # UPON CREATION OF NEW VIRUS: create new parameters virP
                # modify current virP based off of virus
                # add new virP to existing matrix

            # create new I at y[t][i-2]
        



def odeMutations(virP, virV, tmax, ystart):

    # simple SIR model ODE solver
    y = [ystart]

    for t in range(tmax):
        
        # Run mutation before integrating
        # discreteMutation(virP,virV,y,t)   

        # S,I,R values and parameters
        # S and R stay as individual values
        # I is instead compartmentalized into an array where p(Variant v) = I[v]
        S = y[t][0]
        I = y[t][1]
        R = y[t][2]   

        # iterate over each disease
        for v in range(len(I)):

            # I[v]= y[t][v]

            beta = virP[v][0] # transmission
            gamma = virP[v][1] # recovery
            pMutation = virP[v][2] # mutation probab ility 

            S += - beta * S * I[v]
            I[v] += (beta * S * I[v]) - (gamma * I[v])
            R += gamma * I[v]
            
        y.append([S,I,R])

    return y
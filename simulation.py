import matplotlib.pyplot as plt
import numpy as np

# for the sake of cleanliness - groups ICs properly
def prepareICs(ic, i):

    # MY ROOMMATE SHOWED ME TO USE .GET BECAUSE IT IS "SAFER"
    string = ic.get("string")
    tMax = ic.get("tMax")
    virV = ic.get("virV")
    Istart = ic.get("Istart")
    betastart = ic.get("betastart")
    gammastart = ic.get("gammastart")
    pMutationstart = ic.get("pMutationstart")

    # map parameters to usable arrays for ODE 
    virP   =[[betastart[i], gammastart[i], pMutationstart[i]]for i in range(len(Istart))]
    ystart = [1 - sum(Istart),Istart,0]
    odeparams = [virP,virV,tMax,ystart]

    print(f'SIMULATION {i+1}\n', string)

    return odeparams

# plotting function
def plotMutations(y):

    S = [t[0] for t in y]
    R = [t[2] for t in y]

    plt.plot(S, label="Susceptible")
    plt.plot(R, label="Recovered")

    # for length of I at tmax
    for i in range(0,len(y[-1][1])):

        # fill in 0 for all timesteps where I (t[1]) is shorter
        V = [t[1][i] if i < len(t[1]) else 0 for t in y]

        plt.plot(V, label= f"Variant {i}")

    plt.legend()
    plt.show(block=True)

def plotAvgBetaAndGamma(avgBetaOnTime, avgGammaOnTime):

    plt.plot(avgBetaOnTime, label="Average of Beta, Unweighted For Population")
    plt.plot(avgGammaOnTime, label="Average of Gamma, Unweighted For Population")
    plt.plot(np.divide(avgBetaOnTime,avgGammaOnTime), label="Average of Beta/Gamma")
    plt.legend()
    plt.show(block=True)

# sir_MEvariants

The SIR model only assumes a singular variant, while in reality diseases have the chance to mutate.




# ================================================
# WHAT THE FIRST FIGURE SHOWS

# the figure shows the expected values of alpha (avgBetaOnTime) and beta (avgGammaOnTime) 
# (yes i know we used alpha and beta in one set and beta gamma in the other.)
# over 50 iterations of the simulation, along with the ratio of alpha to beta at each timestep.
# the expected values are computed by averaging the results from all 50 iterations, 
# and the ratio is calculated by dividing the expected α by the expected β at each timestep. 
# the plot provides insights into how these parameters evolve over time and their relative relationship.
# the fact that the ratio remains constant / slowly decreases forever after a point suggests that 
# we have successfully found a variation pattern that tends towards infectivity rather than lethality.

# ================================================
#WHAT THE SECOND FIGURE SHOWS

# the second figure shows a sample SIR graph for the last set of initial conditions passed to the simulation.
# it displays the populations of susceptible, infected, and recovered individuals over time.
# there are separate curves for each variant of the infected population,
# illustrating how the infection spreads and evolves over time.
# our current model shows that the first variant is dominant,
# which we would like to fix in the future. This is likely due to our prolific assumptions
# rather than the 'true' behavior of the virus.

# ================================================
# code to run entire simulation
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
def ros_mendel(k,m,n):
    tot_pop=k+m+n
    dom=k/tot_pop
    hetdom=(m/tot_pop)*(k/(tot_pop-1))
    het1het2=(m/tot_pop)*((m-1)/(tot_pop-1))*0.75
    hetrec=(m/tot_pop)*(n/(tot_pop-1))*0.5
    het=hetdom+hetrec+het1het2

    recdom=(n/tot_pop)*(k/(tot_pop-1))
    rechet=(n/tot_pop)*(m/(tot_pop-1))*0.5

    rec=recdom+rechet
    
    print(rec+het+dom)


ros_mendel(15,28,15)
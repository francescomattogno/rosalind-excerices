def mortal_rabbits(n, m):
    
    rab_alive=[]
    rab_alive.append(0)
    rab_alive.append(1)
    for i in range(1, n+1, 1):
        if i < m:
            rab_alive.append(rab_alive[i] + rab_alive[i-1])
        if i == m:
            rab_alive.append(rab_alive[i] + rab_alive[i-1] - rab_alive[i-m+1])
        if i > m:
            rab_alive.append(rab_alive[i] + rab_alive[i-1] - rab_alive[i-m])
    
    return rab_alive[n]

print(mortal_rabbits(85, 16))
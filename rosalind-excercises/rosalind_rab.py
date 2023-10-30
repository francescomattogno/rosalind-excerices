def rab_fib(n, k):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return rab_fib(n-1, k) + k*rab_fib(n-2, k)

    
   

print(rab_fib(32, 4))
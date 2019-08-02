import math  
def prime_number(n):
     a=[p for p in range(2,n) if 0 not in [p%d for d in range (2,int(math.sqrt(p))+1)]]
     return a
a=prime_number(100000)
print(a)

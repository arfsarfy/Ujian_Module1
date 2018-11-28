#Number 1
def nbYear(p0,perecent,aug,p):
    n=0
    while True:
        p0 += p0 * (perecent/100) + aug
        n  += 1 
        if p0>=p:
            return n

print(nbYear(1500000,2.5,10000,2000000))
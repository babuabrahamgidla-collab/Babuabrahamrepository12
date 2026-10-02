print("Hello, world!, 30 September afternoon session")
serires = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def febonacci1(n):
    seriesn0 = 0
    seriesn1 = 1
    if n >= 2:
        
        febn1=0
        febn2=1
        for i in range (1, n):
            febn = febn1 + febn2
            febn1= febn2
            febn2 = febn
            
    elif n==1:
        febn = 1
    elif n==0:
        febn =0
            
    return febn
        
febonacci_nbumber = febonacci1(10) 
print(febonacci_nbumber)       
        
    
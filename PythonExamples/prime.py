def main():
    
    for i in range(2,500):
        isprime=1
        for j in range(2,i):
            if i%j==0:
                isprime=0
                break
            
        if(isprime):
            print i,
        
    
main();

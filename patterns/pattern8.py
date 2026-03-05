class Pattern:
    
    def sol(_self,n):
        
        for i in range(0,n,1):
            
            for j in range(0,i,1):
                print(" ",end="")
                
            for j in range(0, 2*n-(2*i + 1),1): # 
                print("*",end="")   
            
            for j in range(0,i,1):
                print(" ",end="")
                
            print()
                
        
pattern = Pattern()

pattern.sol(5)
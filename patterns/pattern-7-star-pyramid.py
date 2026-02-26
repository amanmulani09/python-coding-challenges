"""
    *    
   ***   
  *****  
 ******* 
*********

"""

class Solution:
    
    def pattern(self,n):
        for i in range(0,n,1): #range(start, stop, step)
            
            # spaces at the start
            for j in range(n -i -1):
                print("-",end="")
                
            # print stars 
            for j in range(2*i+1):
                print("*",end="")
            
            # spaces at the end
            for j in range(n - i - 1):
                print("-",end="")
                
            # move to next row     
            print()
           
sol = Solution()
sol.pattern(5)
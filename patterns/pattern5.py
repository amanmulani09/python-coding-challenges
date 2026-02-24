class Solution:
    
    def pattern(_self,n):
        
        for i in range(n,0,-1):
            line=''
            for j in range(i,0,-1):
                line += '* '
            print(line)
            
sol = Solution()
sol.pattern(5)
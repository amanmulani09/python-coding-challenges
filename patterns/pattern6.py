class Solution:
    
    def pattern(_self,n):
        
        for i in range(n,0,-1):
            line=''
            for j in range(i):
                line += f'{j+1} '
            print(line)
            
sol = Solution()
sol.pattern(5)
class Solution:
    
    def pattern(self,n):
        
        for i in range(n):
            
            line = ''
            for j in range(0,i+1):
                line += f'{i +1}'
            print(line)
            
sol = Solution()
sol.pattern(5)
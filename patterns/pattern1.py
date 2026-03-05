class Pattern:
    
    def pattern(self,n):
        
        for i in range(n):
            line = ''
            for j in range(n):
                line += '* '
            print(line)
            
patrn = Pattern()

patrn.pattern(3)
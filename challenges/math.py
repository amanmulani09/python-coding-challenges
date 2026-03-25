

class Math:
    
    def count_digit(_self,n):
        count = 0
        
        while n > 0:
            count += 1 # increase the count on every iteration till n keep in positive
            
            n = n // 10 # divide the n by 10 to shrink it by 1 digit
            
            print('i am N', n)
            
        return count
    

    def reverse_digit(_self,n):
        
        revNum = 0
        
        while n > 0:
            
            lastDigit  = n % 10
            
            revNum = revNum * 10 + lastDigit
            
            n = n // 10
        
        return revNum
            
            

# sol= Math()
# res = sol.count_digit(7842)
# print(res)

print(Math().reverse_digit(1234))
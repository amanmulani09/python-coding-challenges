

class Math:
    
    def count_digit(_self,n):
        count = 0
        while n > 0:
            
            count+=1 # increase the count in every iteration
            # print(n, "before")
            n = n // 10 # remove the last digit till makes it less than or equal to zero
            # print(n, "after")
        return count
            
            

sol= Math()
res = sol.count_digit(1234)
print(res)

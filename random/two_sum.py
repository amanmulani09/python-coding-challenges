
def two_sum(nums:list[int],target:int) -> list[int]:
    
    seen = {}
    
    for index, num in enumerate(nums):
        
        remaining = target - num
        
        if remaining in seen:
            return [seen[remaining],index]
        
        seen[num] = index
        
    return []


print(two_sum([2, 7, 11, 15],9))

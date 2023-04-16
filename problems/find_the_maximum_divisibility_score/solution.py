class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_divisor_score = 0
        max_divisor = divisors[0]
        
        for d in divisors: # iterate over divisors
            divisor_score = 0
            for n in nums: # iterate over numbers dividing
                if n % d == 0: # count how many nums are divided by a given divisor
                    divisor_score += 1
                    
            # if found divisor with greater divisor score
            if divisor_score > max_divisor_score:
                max_divisor_score = divisor_score
                max_divisor = d
                
            # if found divisor with equal divisor score, take min
            if divisor_score == max_divisor_score:
                max_divisor = min(max_divisor, d)
                
        return max_divisor
            
                    
            
        
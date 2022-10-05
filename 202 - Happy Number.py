class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumSquare(n): 
            r = n
            s = 0 
            while r != 0: 
                last = r % 10 
                s += last**2 
                r = r // 10 
            return s 
        
        d = dict()
        
        while True: 
            if sumSquare(n) == 1: 
                return True 
            
            elif n in d: 
                return False 
            
            d[n] = True 
            n = sumSquare(n)
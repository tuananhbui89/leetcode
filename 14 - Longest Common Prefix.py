class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check_char(c, cindex): 
            for s in strs: 
                if s[cindex] != c: 
                    return False 
            return True 
        
        output = ""
        
        len_min = len(strs[0])
        for sindex, s in enumerate(strs):
            if len(s) <= len_min: 
                imin = sindex 
                len_min = len(s)
            
        for cindex, c in enumerate(strs[imin]): 
            if check_char(c, cindex): 
                output += c 
            else: 
                return output 
        
        return output 
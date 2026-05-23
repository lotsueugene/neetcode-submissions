class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        str_map = {}
        
        for string in s:
            str_map[string] = str_map.get(string, 0) + 1
        
        for char in t:
            if char in str_map and str_map[char] > 0:
                str_map[char] -= 1
            else:
                return False
        return True

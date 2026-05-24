class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1 

        while l < r:
            while l< r and not self.isalphanum(s[l]): #while not an alphanum, move left pointer forward 
                l += 1
            while r > l and not self.isalphanum(s[r]):  #while not an alphanum, move right pointer down 
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l, r = l + 1, r - 1 #moving to the next position to do the next comparison
        return True #if everything on top runs then it is True
        


    def isalphanum(self, c): #isalnum helper function
            return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z')  or 
                ord('0') <= ord(c) <= ord('9') 
                )

class Solution:
    def isAnagram(self, s: str, t: str) :
        dup = {}
        flag = False

        if len(s) != len(t):
            return False

        for i in s:
            if dup.get(i):
                dup[i] += 1
            else:
                dup[i] =1 
    
        
        for j in t:
            if dup.get(j):
                dup[j] -=1
                flag = True

                
            else:
                return False
      


                    
        return flag
            
        
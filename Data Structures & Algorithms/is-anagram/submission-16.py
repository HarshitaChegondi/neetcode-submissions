class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def ana(str):
            dictionary = {}
            for key in str:
                if key not in dictionary:
                    dictionary[key] = 1
                else:
                    dictionary[key] += 1
            return dictionary

        if ana(s) == ana(t):
            return True
        else:
            return False



            


            
                

        
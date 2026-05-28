class Solution:
    def isPalindrome(self, s: str) -> bool:

        modifiedStr = ''.join(filter(str.isalnum, s))

        reverseStr = modifiedStr[::-1]

        if modifiedStr.lower() == reverseStr.lower():
            return True
        else:
            return False



        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sclean = "".join(i for i in s if i.isalnum())
        sRev = sclean[::-1]
        slow = sclean.lower()
        sRevLow = sRev.lower()
        if slow == sRevLow:
            return True
        else:
            return False
        
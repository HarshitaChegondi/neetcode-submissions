class Solution:
    def isPalindrome(self, s: str) -> bool:

        text = ""
        for i in s:
            if i.isalnum():
                text+=i.lower()

        if text == text[::-1]:
            return True
        else:
            return False

        
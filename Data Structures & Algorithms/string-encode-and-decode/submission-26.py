class Solution:

    def encode(self, strs: List[str]) -> str:

        modifiedStrs = [str(len(word)) + word for word in strs]

        if strs:
            newStr = '-'.join(strs) + '-'
            return newStr
        else:
            return ''

        

    def decode(self, s: str) -> List[str]:
        if s != '':
            currentWord = ''
            words = []
            for n in s:
                if n == '-':
                    words.append(currentWord)
                    currentWord = ''
                else:
                    currentWord+=n
            
            if currentWord:
                words.append(currentWord)

            return words
        else:
            return []


        

        

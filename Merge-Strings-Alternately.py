class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = 0
        result = ''
        print('"', end='')
        while x < len(word1) and x < len(word2):
            result += word1[x] + word2[x]
            x += 1

        if x < len(word1):
            while x < len(word1):
                result += word1[x]
                x += 1

        elif x < len(word2):
            while x < len(word2):
                result += word2[x]
                x += 1

        return result


        
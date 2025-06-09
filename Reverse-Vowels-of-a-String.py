class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        str_vowels = []

        for letter in s:
            if letter.lower() in vowels:
                str_vowels += letter

        i = len(str_vowels) - 1

        for j in range(len(s)):
            if s[j].lower() in vowels:
                s[j] = str_vowels[i]
                i -= 1
        s = \\.join(s)
        return s
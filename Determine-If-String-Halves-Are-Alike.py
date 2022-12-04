class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a', 'e', 'i', 'o', 'u']
        countOne = 0
        countTwo = 0
        s = s.lower()

        for i in range(len(s) // 2):
            if s[i] in vowel:
                countOne += 1

        for j in range(len(s)//2, len(s)):
            if s[j] in vowel:
                countTwo += 1
        
        if countOne == countTwo:
            return True
        else:
            return False
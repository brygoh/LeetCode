class Solution:
    def reverseWords(self, s: str) -> str:
        index = len(s) - 1
        wordCount = len(s.split(' '))
        temp = ''
        res = ''

        while True:
            if s[0] == ' ':
                s = s[1:]
                index -= 1
            else:
                break

        while index > 0:
            if s[index] == ' ':
                res += (self.reverseString(temp))
                if wordCount != 1 and temp != '':
                    res += ' '
                    wordCount -= 1
                temp = ''
            else:
                temp += s[index]
            index-=1
        temp += s[0]
        res += self.reverseString(temp)

        return res
    
    def reverseString(self, s: str) -> str:
        return s[::-1]

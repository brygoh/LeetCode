# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 1, n
        while upper >= lower:
            tracker = (upper + lower) // 2
            if guess(tracker) == 1:
                lower = tracker + 1
            if guess(tracker) == -1:
                upper = tracker - 1
            if guess(tracker) == 0:
                return tracker
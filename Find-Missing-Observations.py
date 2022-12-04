class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n)
        totalMissing = total - sum(rolls)
        if totalMissing < n or totalMissing > 6 * n: return []
        quotient, remainder = divmod(totalMissing, n)
        res = [quotient] * n
        for i in range(remainder):
            res[i] += 1
        return res
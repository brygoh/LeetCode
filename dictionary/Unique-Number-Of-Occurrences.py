class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        unique = {}
        for i in count.values():
            if i not in unique:
                unique[i] = 1
            else:
                return False
        return True

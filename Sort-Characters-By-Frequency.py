class Solution:
    def frequencySort(self, s: str) -> str:
        dick = {}
        res = []
        for i in s:
            dick[i] = 1 + dick.get(i, 0)
        
        dick = dict(sorted(dick.items(), key=lambda item: item[1], reverse=True))
        for j, k in dick.items():
            for i in range(k):
                res.append(j)
        return res
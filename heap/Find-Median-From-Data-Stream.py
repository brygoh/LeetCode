from heapq import *

class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heappush(self.maxheap, -heappushpop(self.minheap, -num))
        else:
            heappush(self.minheap, -heappushpop(self.maxheap, num))

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return float(self.maxheap[0] - self.minheap[0]) / 2.0
        else:
            return float(self.maxheap[0])
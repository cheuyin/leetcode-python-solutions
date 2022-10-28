class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(0, n + 1):
            res.push(onesCount(i))
        
        return res


    def onesCount(self, n: int) -> int:
        res = 0

        while n: 
            res += n % 2
            n = n >> 1
        
        return res
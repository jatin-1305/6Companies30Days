class Solution:
    def trailingZeroes(self, n: int) -> int:
        f=1
        for i in range(1,n+1):
            f*=i
        f=str(f)
        count=0
        for i in f[::-1]:
            if i=='0':
                count+=1
            else:
                break
        return count

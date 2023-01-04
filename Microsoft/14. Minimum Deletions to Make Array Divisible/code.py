def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        if len(numsDivide)>1:
            num1,num2=numsDivide[0],numsDivide[1]
            gcd=find_gcd(num1,num2)
            for i in range(2,len(numsDivide)):
                gcd=find_gcd(gcd,numsDivide[i])
        else:
            gcd = numsDivide[0]
        d,count={},0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                a=d[i]
                d[i]=a+1
        d1 = {i: d[i] for i in sorted(list(d.keys()))}
        for key in d1.keys():
            if gcd%key!=0:
                a=d[key]
                count+=a
            else:
                return count
        return -1

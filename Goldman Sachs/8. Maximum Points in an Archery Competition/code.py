class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bobArrows = []
        for i in range(12):
            bobArrows.append(aliceArrows[i] + 1)
        maxScore, maxBinNum = 0, None
        for binNum in range(2 ** 12):
            tempScore, tempArrows = 0, 0
            tempBinNum = binNum
            k = 0
            while tempBinNum > 0:
                if tempBinNum % 2 == 1:
                    tempScore += k
                    tempArrows += bobArrows[k]
                tempBinNum //= 2
                k += 1
            if tempArrows <= numArrows and tempScore > maxScore:
                maxScore = tempScore
                maxBinNum = binNum
        output = [0] * 12
        k = 0
        while maxBinNum > 0:
            if maxBinNum % 2 == 1:
                output[k] = bobArrows[k]
            maxBinNum //= 2
            k += 1
        if sum(output) < numArrows:
            output[0] += numArrows - sum(output)
        return output

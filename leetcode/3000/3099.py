class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        xs = str(x)
        sum = 0
        for c in xs:
            sum += int(c)
        return sum if x%sum == 0 else -1
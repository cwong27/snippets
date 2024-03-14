class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        def factors(n):    
            return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        f = sorted(factors(area))
        if len(f) % 2 == 1:
            return [f[len(f)//2],f[len(f)//2]]
        return [f[len(f)//2],f[(len(f)//2)-1]]
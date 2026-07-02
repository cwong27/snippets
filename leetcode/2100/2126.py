class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sorted_a = sorted(asteroids)
        total_m = mass
        for n in sorted_a:
            if n <= total_m:
                total_m += n
            else:
                return False
        return True
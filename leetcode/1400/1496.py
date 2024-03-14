class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x = y = 0
        visited.add(f"{x},{y}")
        for p in path:
            if p == 'N':
                y += 1
            if p == 'S':
                y -= 1
            if p == 'E':
                x += 1
            if p == 'W':
                x -= 1
            current = f"{x},{y}"
            if current in visited:
                return True
            visited.add(f"{x},{y}")
        return False

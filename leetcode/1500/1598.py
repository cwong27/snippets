class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for l in logs:
            if l == "./":
                continue
            elif l == "../":
                depth = max(0, depth-1)
            else:
                depth += 1
        return depth
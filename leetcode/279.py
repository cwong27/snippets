def numSquares(n: int) -> int:
    squares = [i**2 for i in range(1, int(n**0.5) + 1)]
    rest, count = n, 0
    while rest > 0:
        for s in squares[::-1]:
            if rest >= s:
                rest -= s
                count += 1
                break
    return count
numSquares(12)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(0)
        n = int(''.join(map(str, num))) 
        total = n + k 
        return [int(digit) for digit in str(total)] 
        
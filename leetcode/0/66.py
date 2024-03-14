class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        done = False
        i = len(digits) - 1
        while not done:
            if digits[i] != 9:
                digits[i] += 1
                done = True
            else:
                if i == 0:
                    digits[i] = 0
                    new_digits = [1]
                    new_digits += digits
                    digits = new_digits
                    done = True
                else:
                    digits[i] = 0
                    i -= 1
        return digits
        
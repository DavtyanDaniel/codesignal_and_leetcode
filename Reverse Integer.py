# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:

    def reverse(self, x: int) -> int:
        i = len(str(x)) - 1
        reversed = 0
        b = False
        if x < 0:
            x = -1 * x
            i = len(str(x)) - 1
            b = True
        while i >= 0:
            current_num = x % 10
            reversed = reversed + current_num * pow(10, i)
            x = x // 10
            i = i - 1
        if pow(2, 31) * -1 <= reversed <= pow(2, 31) - 1:
            if b:
                return reversed * -1
            else:
                return reversed
        else:
            return 0
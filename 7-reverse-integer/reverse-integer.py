class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        revnum = 0
        while x > 0:
            ld = x % 10
            revnum = revnum * 10 + ld
            x //= 10

        revnum *= sign

        if revnum < - (2**31) or revnum > (2**31):
            return 0

        return revnum
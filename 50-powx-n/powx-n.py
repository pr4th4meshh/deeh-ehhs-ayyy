class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1.0

        half = self.myPow(x, n // 2)
        return half * half * (x if n % 2 else 1)

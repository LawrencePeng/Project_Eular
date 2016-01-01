def power(x, exp):
    def power(x, exp, nowX):
        if exp is 0:
            return nowX
        if exp % 2 is 0:
            return power(x * x, exp / 2, nowX)
        return power(x, exp - 1, nowX * x)
    return power(x, exp, 1)
sum = 0
for x in range(1, 1001):
    sum += power(x, x)
print sum


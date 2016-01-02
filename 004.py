def isPalin(num):
    return str(num) == str(num)[::-1]

max = 0
for x in range(100,1000):
    for y in range(100,1000):
        if isPalin(x * y) and max < x * y:
            max = x * y

print max

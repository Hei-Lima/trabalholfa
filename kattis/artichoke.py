import math

l = input().split()
p = int(l[0])
a = int(l[1])
b = int(l[2])
c = int(l[3])
d = int(l[4])
n = int(l[5])
biggest_drop = 0.0

def price(k):
    return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)

if n <= 1:
    print(f"{0.0:.7f}")
else:
    max_so_far = price(1)
    for k in range(2, n + 1):
        pk = price(k)
        drop = max_so_far - pk
        if drop > biggest_drop:
            biggest_drop = drop
        if pk > max_so_far:
            max_so_far = pk

    print(f"{biggest_drop:.7f}")
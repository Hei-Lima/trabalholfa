n = int(input())
l = list(map(int, input().split()[:n]))
m = min(l)
idx = l.index(m)

print(idx)
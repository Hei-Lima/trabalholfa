l = input().split()

n = int(l[3])
total = 0
f = True

for i in range(0, 3):
    if int(l[i]) == 0:
        f = False
    total += int(l[i])

if total < n or n < 3:
    f = False
    
print("YES" if f == True else "NO")
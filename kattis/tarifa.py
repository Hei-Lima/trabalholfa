x = int(input())
n = int(input())
avaliable = 0

for i in range(n):
    avaliable += x - int(input())
    
print(avaliable + x)
n = int(input())
l = input().split()

result = [0] * (n + 1)  
result[1] = 1  


for i, val in enumerate(l):
    position = int(val) + 2 
    result[position] = i + 2  

print(" ".join(str(result[i]) for i in range(1, n + 1)))
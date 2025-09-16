n = int(input())

for i in range(n):
    x = int(input())
    string = "even" if x % 2 == 0 else "odd"
    print(str(x) + " is " + string)
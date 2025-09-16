def formate(l, i):
    mini = min(l)
    maxi = max(l)
    rang = maxi - mini
    print("Case: " + str(i) + " " + str(mini) + " " + str(maxi) + " " + str(rang))

for i in range(10):
    try:
        l = input()
    except EOFError:
        break
    l = l.split()[1:]
    formate(l, i)
l = input().split()

power = int(l[0]) * 3 + int(l[1]) * 2 + int(l[2]) * 1
v = "Estate"
t = "Copper"

dv = {"Province":8, "Duchy":5, "Estate":1}
dt = {"Gold":6, "Silver":3, "Copper":0}

if power >= 2:
    for key in dv:
        if power >= dv[key]:
            if dv[key] > dv[v]:
                v = key

for key in dt:
    if power >= dt[key]:
        if dt[key] > dt[t]:
            t = key

if power >= 2:
    print(v + " or " + t)
else:
    print(t)

l = list(map(int, input().strip("[]").split())) if input else []

if not l:
    print(-1)
else:
    p1 = p2 = None

    for i in l:
        if p1 is None or i > p1:
            if p1 != i:
                p2 = p1
            p1 = i
        elif i < p1 and (p2 is None or i > p2):
            p2 = i

    print(p2 if p2 is not None else -1)

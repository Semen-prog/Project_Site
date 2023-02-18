def paint(mod):
    res = [[0 for _ in range(mod)] for _ in range(mod)]
    for a in range(mod):
        for b in range(mod):
            if res[a][b] > 0:
                continue
            x, y = a, b
            q = []
            res[x][y] = -1
            len = 0
            while True:
                len += 1
                x, y = y, x * y % mod
                if res[x][y] > 0:
                    res[a][b] = res[x][y]
                    break
                if res[x][y] < 0:
                    ind = -res[x][y] - 1
                    res[a][b] = len - ind
                    break
                res[x][y] = -len - 1
                q.append((x, y))
            for x, y in q:
                res[x][y] = res[a][b]
    return res
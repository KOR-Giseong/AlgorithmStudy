n = int(input("숫자 입력 : "))

for y in range(0, n):
    for x in range(0, n):
        p = min(x, y, n - x - 1, n - y - 1)
        if x >= y:
            q = x + y - 2 * p
        else:
            q = (n - 1 - 2 * p) * 4 - (x + y - 2 * p)
        q += 4 * (p * n - (p * p))
        print("{:3d}".format(q), end="")
    print()
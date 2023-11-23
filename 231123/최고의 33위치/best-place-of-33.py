field = []

def getValue(x, y) -> int:
    global field
    ret = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            ret += field[i][j]
    return ret


N = int(input())

for i in range(N):
    field.append(list(map(int, input().split())))

ret = 0
for i in range(N-2):
    for j in range(N-2):
        ret = max(ret, getValue(i, j))

print(ret)
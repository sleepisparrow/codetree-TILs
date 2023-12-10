N = int(input())
arr = list(map(int, input().split()))

def printAll(arr):
    for i in arr:
        print(i, end=" ")
    print()

def makeNum(past, tmp):
    if len(tmp) == 6:
        printAll(tmp)
        return
    elif len(tmp) > 6:
        return
    # if past >=  len(arr):
    #     return

    for i in range(past+1, len(arr)):
        tmp.append(arr[i])
        makeNum(i, tmp)
        tmp.pop()

makeNum(-1, [])
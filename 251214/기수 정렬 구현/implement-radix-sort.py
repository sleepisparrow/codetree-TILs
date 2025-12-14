import math

n = int(input())
arr = list(map(int, input().split()))

mx = 0;
for i in range(n):
    if mx < arr[i]:
        mx = arr[i]

k = 0
while(mx >= 1):
    k += 1
    mx /= 10

for i in range(k):
    t_a = [[] for row in range(10)] 
    for j in range(n):
        x = math.floor(arr[j] / (10 ** (k - i - 1)) % 10)
        t_a[x].append(arr[j])
    r_a = []
    for j in range(10):
        for k in range(len(t_a[j])):
            r_a.append(t_a[j][k])

    arr = r_a

for i in range(n):
    print(arr[i], end=" ")

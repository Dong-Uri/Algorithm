n, k = map(int, input().split())
arr = [
    [''],
    ['1'],
    ['1+1', '2'],
    ['1+1+1', '1+2', '2+1', '3'],
]
i = 4
while i <= 11:
    lst = []
    for sik in arr[-1]:
        lst.append('1+' + sik)
    for sik in arr[-2]:
        lst.append('2+' + sik)
    for sik in arr[-3]:
        lst.append('3+' + sik)
    arr.append(lst)
    i += 1
if len(arr[n]) < k:
    print(-1)
else:
    print(arr[n][k - 1])
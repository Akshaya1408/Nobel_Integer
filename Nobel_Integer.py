def nobelinteger(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if i==arr[i]:
            return 1
    return -1        

arr=list(map(int,input().split()))
print(nobelinteger(arr))
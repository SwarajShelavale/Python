if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    while(mx in arr):
        arr.remove(mx)
    mx = max(arr)
    print(mx)

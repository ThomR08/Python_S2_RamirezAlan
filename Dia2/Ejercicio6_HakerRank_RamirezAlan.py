if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr=list(set(arr))

if(2<=n<=10 and all(-100<=x<=100 for x in arr)):
    arr.sort(reverse=True)
    print(arr[1])

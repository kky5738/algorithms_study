def solution():
    result = 0
    n, m, k = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())), reverse=True)
    print(arr)
    # print(8 % 3)
    # print(8 // 3)
    if arr[0] == arr[1]:
        result = arr[0] * m
    elif arr[0] > arr[1]:
        x = m % (k+1)
        y = m // (k+1) * k
        print(x,y)
        result += arr[0] * k * x + arr[1] * y
        
    return result

def main():
    result = solution()
    print(result)
    
if __name__ == '__main__':
    main()
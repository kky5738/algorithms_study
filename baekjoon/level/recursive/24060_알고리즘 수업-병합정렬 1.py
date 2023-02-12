# 백준 24060번 알고리즘 수업 - 병합 정렬 1
import sys

def main():
    solution()
    
def solution():
    global k
    n, k = map(int, sys.stdin.readline().rstrip().split(' '))
    
    array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    sorted_array = merge_sort(array, 0, n-1)
    if k > 0:
        print(-1)

def merge_sort(array, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        result = merge(array, p, q, r)
        return result

def merge(array, p, q, r):
    global k
    
    i = p
    j = q + 1
    t = 1
    temp = []
    while i <= q and j <= r:
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= q:
        temp += [array[i]]
        i += 1
    while j <= r:
        temp += [array[j]]
        j += 1
    
    i = p
    t = 0
    
    while i <= r:
        array[i] = temp[t]
        k -= 1
        if k == 0:
            print(array[i])

        t += 1
        i += 1
    return array
        

if __name__ == '__main__':
    main()
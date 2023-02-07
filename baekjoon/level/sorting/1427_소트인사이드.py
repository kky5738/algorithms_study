# 백준 1427번 소트인사이드
import sys

def main():
    solution()
    
def solution():
    # 내림차순 정렬
    n = list(map(int, sys.stdin.readline().rstrip()))
    result = merge_sort(n)
    for x in result:
        print(x, end='')
    
def merge_sort(array):
    if len(array) < 2: return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    merged_list = []
    l_idx = r_idx = 0
    
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            merged_list.append(right[r_idx])
            r_idx += 1
        else:
            merged_list.append(left[l_idx])
            l_idx += 1
    
    merged_list += left[l_idx:]
    merged_list += right[r_idx:]
    
    return merged_list
    

if __name__ == '__main__':
    main()
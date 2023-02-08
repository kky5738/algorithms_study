# 백준 11651번 좌표 정렬하기2
import sys

def main():
    solution()
    
def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        array.append([x, y])
        
    sorted_array = merge_sort(array)
    for x, y in sorted_array:
        print(x, y)

def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    l_idx = r_idx = 0
    merged_list = []
    
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx][1] > right[r_idx][1]:
            merged_list.append(right[r_idx])
            r_idx += 1
            
        elif left[l_idx][1] == right[r_idx][1]:
            if left[l_idx][0] > right[r_idx][0]:
                merged_list.append(right[r_idx])
                r_idx += 1
            else:
                merged_list.append(left[l_idx])
                l_idx += 1
        else:
            merged_list.append(left[l_idx])
            l_idx += 1
    
    merged_list += left[l_idx:]
    merged_list += right[r_idx:]
    
    return merged_list
            
if __name__ == '__main__':
    main()
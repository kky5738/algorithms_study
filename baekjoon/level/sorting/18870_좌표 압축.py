# 백준 18870번 좌표 압축
import sys

def main():
    solution()
    
def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    
    sorted_list = merge_sort(list(set(array)))
    values = [i for i in range(len(sorted_list))]
    answer = dict(zip(sorted_list, values))
    
    for key in array:
        print(answer[key], end=' ')
    
    
def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    l_idx = r_idx = 0
    merged_list = []
    
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] > right[r_idx]:
            merged_list.append(right[r_idx])
            r_idx += 1
        else:
            merged_list.append(left[l_idx])
            l_idx += 1
    
    merged_list += left[l_idx:]
    merged_list += right[r_idx:]
    return merged_list
if __name__ == "__main__":
    main()
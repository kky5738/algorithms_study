import sys

def main():
    solution()

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    
    sorted_list = merge_sort(array)
    
    for x in sorted_list:
        print(x)

def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    left_idx = right_idx = 0
    merged_list = []
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            
            merged_list.append(right[right_idx])
            right_idx += 1
        else:
            
            merged_list.append(left[left_idx])
            left_idx += 1
    
    merged_list += left[left_idx:]
    merged_list += right[right_idx:]
    return merged_list

if __name__ == '__main__':
    main()
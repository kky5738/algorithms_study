# 백준 1181번 단어 정렬, 다른 정렬 알고리즘도 구현하기
import sys

def main():
    solution()

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = set()
    
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        array.add(word)
        
    array = list(array)
    result = merge_sort(array)
    for word in result:
        print(word)
        
def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    l_idx = r_idx = 0
    merged_list = []
    
    while l_idx < len(left) and r_idx < len(right):
        if len(left[l_idx]) > len(right[r_idx]):
            merged_list.append(right[r_idx])
            r_idx += 1
        
        elif len(left[l_idx]) == len(right[r_idx]):
            if left[l_idx] > right[r_idx]:
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
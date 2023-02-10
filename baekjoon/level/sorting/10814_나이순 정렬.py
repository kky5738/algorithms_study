# 백준 10814번 나이순 정렬, stable 정렬사용하기
import sys

def main():
    solution()

def solution():
    n = int(sys.stdin.readline())
    user = []
    
    for i in range(n):
        age, name = sys.stdin.readline().rstrip().split(' ')
        user.append([int(age), name, i+1])
    
    def merge_sort(array: list) -> list:
        if len(array) < 2:
            return array
        
        left = merge_sort(array[:len(array)//2])
        right = merge_sort(array[len(array)//2:])
        
        l_idx = r_idx = 0
        merged_list = []
        
        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx][0] > right[r_idx][0]:
                merged_list.append(right[r_idx])
                r_idx += 1
            elif left[l_idx][0] == right[r_idx][0]:
                if left[l_idx][2] > right[r_idx][2]:
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
            
    answer = merge_sort(user)
    for age, name, _ in answer:
        print(age, name)
    
if __name__ == '__main__':
    solution()
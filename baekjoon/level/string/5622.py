import sys

def solution():
    inputs = sys.stdin.readline().rstrip()
    
    time_dict = dict()
    
    for i in range(2, 10):
        time_dict[i] = i+1
    
    alpha_dict = dict()
    upper_case = 65
    dial = 1
    cnt = 0
    
    for num in range(upper_case, upper_case+26):
        if cnt % 3 == 0 and cnt < 18:
            dial += 1
        if cnt > 18 and cnt < 25:
            if cnt % 3 == 1: dial += 1

        alpha_dict[chr(num)] = dial
        cnt += 1
    
    answer = 0
    for d in inputs:
        answer += time_dict[alpha_dict[d]]
    
    print(answer)

if __name__ == '__main__':
     solution()
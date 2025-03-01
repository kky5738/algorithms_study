# 백준 1009 분산처리. 수학, 구현

import sys



t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr = dict()
    
    # 제곱수의 1의 자리는 1개에서 4개의 자연수가 규칙적으로 반복된다.
    # 따라서 a^4까지만 살펴보고 중복된 수를 제거한 다음, b % (규칙적으로 등장하는 숫자 개수)를 해주면 오버플로우 발생 없이 마지막 데이터의 처리를 구할 수 있음
    for i in range(1, 5):
        arr[int(str(a**int(i))[-1])] = None
    
    ans_arr = list(arr.keys())
    answer = ans_arr[b % len(ans_arr) - 1]
    print(answer if answer != 0 else 10)
    
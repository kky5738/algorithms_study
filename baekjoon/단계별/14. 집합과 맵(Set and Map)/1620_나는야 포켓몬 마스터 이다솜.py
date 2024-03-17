# 백준_단계별로 풀어보기_14. 집합과 맵_1620번 나는야 포켓몬 마스터 이다솜
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

name_dict = []

for i in range(1, n + 1):
    pokemon = sys.stdin.readline().rstrip()
    name_dict.append((pokemon, str(i)))

name_dict = dict(name_dict)
num_dict = {v:k for k, v in name_dict.items()}

for _ in range(m):
    data = sys.stdin.readline().rstrip()

    if data.isalpha():
        print(name_dict[data])
    else:
        print(num_dict[data])

# BOJ 17175 피보나치는 지겨웡~

def solution():
    import sys

    MOD = 1000000007
    n = int(sys.stdin.readline().rstrip())

    if n < 2:
        return print(1)
    d = [0] * (n+1)
    d[0] = d[1] = 1

    for i in range(2, n+1):
        d[i] = (d[i-1] + d[i-2] + 1) % MOD

    print(d[n])

if __name__ == "__main__":
    solution()
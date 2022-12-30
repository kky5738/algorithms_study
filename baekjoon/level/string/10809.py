import sys

def solution():
    string = sys.stdin.readline().rstrip()
    answer = [-1 for _ in range(26)]
    
    for idx, alphabet in enumerate(string):
        if answer[ord(alphabet) % 97] == -1:
            answer[ord(alphabet) % 97] = idx

    for a in answer:
        print(a, end=' ')

if __name__ == '__main__':
    solution()
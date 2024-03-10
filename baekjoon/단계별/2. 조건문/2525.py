def solution():
    h, m = map(int, input().split(' '))
    c = int(input())

    h += (m + c) // 60
    m = (m + c) % 60

    if h >= 24: h-=24

    print(h, m)

    
def main():
    solution()

if __name__ == "__main__":
    main()
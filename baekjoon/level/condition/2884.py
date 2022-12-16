def solution():
    h, m = map(int, input().split(' '))
    
    if h == 0:
        print(f'0 {m-45}' if m>=45 else f'23 {60-(45-m)}')
    else:
        print(f'{h} {m-45}' if m>=45 else f'{h-1} {60-(45-m)}')
    
def main():
    solution()

if __name__ == "__main__":
    main()
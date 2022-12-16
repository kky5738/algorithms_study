def solution():
    d = int(input())

    print('A' if d>89 else 'B' if d>79 else 'C' if d>69 else 'D' if d>59 else 'F')
    
def main():
    solution()

if __name__ == "__main__":
    main()
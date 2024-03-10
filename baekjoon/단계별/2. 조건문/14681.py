def solution():
    x = int(input())
    y = int(input())
    
    if x > 0:
        print('1' if y>0 else '4')
    else:
        print('2' if y>0 else '3')
    
def main():
    solution()

if __name__ == "__main__":
    main()
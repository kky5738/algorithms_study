import sys

def solution(position):
    col_dict = {"a": 1,
                "b": 2,
                "c": 3,
                "d": 4,
                "e": 5,
                "f": 6,
                "g": 7,
                "h": 8}
    
    col, row = col_dict[position[0]], int(position[1])
    
    """
    1. row + 2 col + 1
    2. row + 2 col - 1
    3. row - 2 col + 1
    4. row - 2 col - 1
    5. row + 1 col + 2
    6. row + 1 col - 2
    7. row - 1 col + 2
    8. row - 1 col - 2
    """
    direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    answer = 0
    for r, c in direction:
        if row + r <= 0 or row + r >= 9:
            continue
        if col + c <= 0 or col + c >= 9:
            continue
        answer += 1
    print(answer)

if __name__ == "__main__":
    position = sys.stdin.readline().rstrip()
    solution(position)
def get_number(generator):
    result = generator

    for n in str(generator):
        result += int(n)

    return result

def solution():
    n = 10000
    answer = [i+1 for i in range(n)]
    
    for num in range(n):
        generator = get_number(num)
        
        try:
            answer.remove(generator)
        except ValueError:
            continue

    for i in answer:
        print(i)

if __name__ == '__main__':
    solution()
def get_self_number(generator):
    result = generator

    for n in str(generator):
        result += int(n)

    return result

def solution():
    array = [i+1 for i in range(50)]
    answer = array
    
    for n in range(50):
        print(n)
        self_num = get_self_number(n)
        # print(self_num)
        try:
            answer.remove(self_num)
        except ValueError:
            continue
        else:
    

    print(answer)

if __name__ == '__main__':
    solution()
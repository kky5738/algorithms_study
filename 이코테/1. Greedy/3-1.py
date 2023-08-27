n = int(input())
result = 0

result += n // 500
n %= 500

result += n // 100
n %= 100

result += n // 50
n %= 50

result += n // 10
n %= 10

print(result)

"""
    # better version
    cash = [500, 100, 50, 10]
    for coin in cash:
        result += n // coin
        n %- coin
    
    print(result)
"""
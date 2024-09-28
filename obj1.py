def getluckynum(a, b):
    luckies = []
    for i in range (a, b + 1):
        digit = 0
        number = i
        while number > 0:
            if number % 10  % 2 == 0:
                digit += 1
            number //= 10

        if 2 * digit == len(str(i)):
            luckies.append(i)
    return luckies
print(getluckynum(*list(map(int, input('').split()))))
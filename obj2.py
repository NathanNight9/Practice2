import math

def datefind(day, month, year):  
    curm = 1
    date = []
    DIM = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    daysum = sum(DIM[i] for i in range(1, month)) + math.floor(year*365.25) + day + 1
    date.append(math.floor(daysum/365.25))
    daysum -= math.floor(math.floor(daysum/365.25) * 365.25)
    while daysum - DIM[curm] >= 0:
        if curm == 12:
            curm = 1
        daysum -= DIM[curm]
        curm += 1
    date.append(curm)
    date.append(daysum)
    date.reverse()
    return date
print(datefind(*list(map(int, input('').split()))))
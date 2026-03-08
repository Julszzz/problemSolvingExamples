def pageCount(n, p):
    # countLow = 0
    # countHigh = 0
    # for i in range(1, p, 2):
    #     countLow += 1
    #     print(countLow)
    # print("---")
    # for x in range(n, p, -2):
    #     countHigh += 1 
    #     print(countHigh)
    # print("---\nResult:")
    # if countLow < countHigh:
    #     print(countLow)
    # else:
    #     print(countHigh)
    countLow = p//2
    countHigh = n//2 - countLow
    return print(min(countLow, countHigh))
        
pageCount(67,23)

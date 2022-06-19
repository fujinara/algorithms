def solve(seats):
    i, res, cnt = 0, 0, 0
    
    while i < len(seats) and seats[i] == '0':
        i += 1
    res = max(res, i)

    while i < len(seats):
        if seats[i] == '1':
            cnt = 0
            res = max(res, round(cnt / 2))
        else:
            cnt += 1
        i += 1
    
    res = max(res, cnt)
    
    return res


seats = input()
print(solve(seats))
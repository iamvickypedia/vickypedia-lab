def diamond_number_pattern(lim):
    arr = [i for i in range(1,lim+2)]+[i for i in range(1,lim+1)[::-1]]
    for a in arr:
        print(' '*(lim*2-a),end="")
        temp=""
        for i in range(1,a+1):
            temp += " "+str(i)
        print(temp)


lim = int(input('Enter the limit for pattern\n'))

diamond_number_pattern(lim)


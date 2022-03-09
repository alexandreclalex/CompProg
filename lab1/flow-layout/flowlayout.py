maxwidth = int(input())

while maxwidth != 0:
    #Read in rows
    windows = []
    inline = input()
    while inline != '-1 -1':
        windows.append(list(map(int, inline.split(' '))))
        inline = input()

    totalwidth = 0
    totalheight = 0
    currentlinew = 0
    currentlineh = 0
    for width, height in windows:
        #Reset Row
        if currentlinew + width > maxwidth:
            if currentlinew > totalwidth:
                totalwidth = currentlinew
            totalheight +=  currentlineh
            currentlinew, currentlineh = 0,0
        currentlinew += width

        #Add to row
        if height > currentlineh:
            currentlineh = height

    #Add last row
    if currentlinew > totalwidth:
        totalwidth = currentlinew
    totalheight +=  currentlineh

    #Print and get next input
    print(totalwidth, 'x', totalheight)

    maxwidth = int(input())
        
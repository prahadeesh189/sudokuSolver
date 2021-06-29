import time




def sudokuSolver( sudokuArr ):

    # preparing points
    points = {}
    for s in range(len(sudokuArr)):
        for r in range(len(sudokuArr[s])):
            row = s+1
            col = r+1           
            point = f"{row}{col}{   (((s//3)*3) + (r//3)) + 1  }"
            points[point] = sudokuArr[s][r]




    # finding empty points and possible values for each empty points
    possibleValues = {}
    emptyPoints  = []

    for point in points:
        if (points[point] == 0):
            Row   = point[0]
            Col   = point[1]
            Block = point[2]

            possibleSet = set([q for q in range(1,10)])

            for _g in points:
                if (( _g[0] == Row or _g[1] == Col or (Block == _g[2])) and points[_g] != 0 and _g != point ):
                    possibleSet.discard(points[_g])

            if (len(possibleSet) == 1):
                for _temp in possibleSet:
                    points[point] = _temp
            else:
                possibleValues[point] = possibleSet
                emptyPoints.append( {'p':point, 'l':len(possibleSet)} )
    
                





    # checking if the value is valid for the given point
    def isPointValid(val , point ):
        reqRow   = point[0]
        reqCol   = point[1]
        reqBlock = point[2]

        if (val == 0):
            return None

        for e in points:
            if ( ( e[0] == reqRow or e[1] == reqCol or (reqBlock == e[2])) and e != point and points[e] != 0  ):
                if ( points[e] == val ):
                    return False
        return True






    global max_start
    max_start = -1



    # back tracking allgorithm
    def solve( start , end ):
        global max_start

        if ( start > end ):
            return True


        if (start > max_start):
            print( f"{(start / end) * 100}  =>  {start} / {end}" )
            max_start = start


        currentEmptyPoint = emptyPoints[start]['p']

        for num in possibleValues[currentEmptyPoint]:
            temp = isPointValid( num , currentEmptyPoint )
            if (temp):
                points[currentEmptyPoint] = num
                if (solve( start+1 , end )):
                    return True
                points[currentEmptyPoint] = 0
        return False




    solve( 0 , len(emptyPoints)-1 )






    # printing the board
    for s in range(len(sudokuArr)):
        for r in range(len(sudokuArr[s])):

            if (sudokuArr[s][r] == 0):
                point = f"{s+1}{r+1}{ (((s//3)*3) + (r//3)) + 1 }"
                print( points[point] , end = ' ' )

            else:
                print( " " , end = ' ')

            if ( ((r+1) % 3 == 0) and ((r+1) < 7 ) ):
                print("|", end = ' ' )

        print()
        if ( ((s+1)%3 == 0) and ((s+1)<=6)):
            print("------|-------|------")









sudoku = (
    (0, 0, 0, 8, 0, 0, 0, 0, 5),
    (3, 2, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (4, 7, 0, 0, 0, 0, 0, 2, 0),
    (6, 0, 0, 0, 5, 0, 0, 0, 0),
    (0, 0, 0, 1, 8, 0, 0, 0, 0),
    (0, 0, 1, 5, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 2, 7, 0),
    (0, 0, 0, 0, 0, 4, 3, 0, 0)
)







t = time.time()
sudokuSolver( sudoku )
print(time.time() - t )

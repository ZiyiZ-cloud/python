def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    result=0
    column=len(matrix[0])
    row=len(matrix)
    for x in range(column):
        for y in range(row):
            if x==y:
                result=result+matrix[x][y]
            if x+y == column:
                result=result+matrix[x][y]
    print(result)
    
    
    
m1 = [
    [1,   2],
    [30, 40],
     ]
sum_up_diagonals(m1)


m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
     ]
sum_up_diagonals(m2)
def maximum_consecutive_in_matrix(matrix:list[list], element)->int:
    count = 0
    result = 0

    for row in matrix:
        for row_element in row:
        
            if row_element == element:
                count += 1

        if count > result:
            result = count

        count = 0
        
    return result


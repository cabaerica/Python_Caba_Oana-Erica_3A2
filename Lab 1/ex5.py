def spiralMatrix(matrix):
    r = 0
    c = 0
    num_of_rows = len(matrix[0])
    num_of_columns = len(matrix)
    
    while (r < num_of_rows and c < num_of_columns):
        for i in range (c, num_of_columns):
            print(matrix[r][i], end = ' ')
        
        r += 1

        for i in range(r, num_of_rows):
            print(matrix[i][num_of_columns - 1], end = ' ')

        num_of_columns -= 1

        if(r < num_of_rows):
            for i in range(num_of_columns - 1, c - 1, -1):
                print(matrix[num_of_rows - 1][i], end = ' ')

            num_of_rows -= 1
        
        if(c < num_of_columns):
            for i in range(num_of_rows- 1, r - 1, -1):
                print(matrix[i][c], end = ' ')
            
            c += 1

matrix = [['f', 'i', 'r', 's'],
          ["n", "_", "l", "t"],
          ["o", "b", "a", "_"],
          ["h", "t", "y", "p"]]

spiralMatrix(matrix)  
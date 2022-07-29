
# Python program to print addition of matrix. 

def mat_addition(matrix_a,matrix_b):
    for i in range(len(matrix_a)) : 
        for j in range(len(matrix_a[0])): 
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result


if __name__ == "__main__" : 
    matrix_a = [[1,2,3],
                [1,2,3],
                [1,2,3]]
    matrix_b = [[1,2,3],
                [1,2,3],
                [1,2,3]]
    

    result = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    matrix_addition = mat_addition(matrix_a,matrix_b)

    print(matrix_addition)
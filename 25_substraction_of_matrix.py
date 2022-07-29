
# Python program to print Substraction of two Matrices. 

def Substract_Matrix(Matrix_A,Matrix_B):
    for i in range(len(Matrix_A)) : 
        for j in range(len(Matrix_B)) : 
            Result[i][j] = Matrix_A[i][j] - Matrix_B[i][j] 
    return Result 

if __name__ == "__main__" : 
    Matrix_A = [[1,2,3],
                [1,2,3],
                [1,2,3]]
    Matrix_B = [[2,3,4],
                [2,3,4],
                [2,3,4]]
    Result = [[0,0,0],[0,0,0],[0,0,0]]

    Sub_Matrix = Substract_Matrix(Matrix_A,Matrix_B)

    print(f"Output: {Sub_Matrix}")

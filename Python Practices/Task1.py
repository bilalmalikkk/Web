print("Enter the number of rows of matrix1: ")
rows1=int(input())
print("Enter the number of columns of matrix1")
col1=int(input())
print("Enter the  number of rows for matrix2:")
rows2=int(input())
print("Enter the number of columns of matrix2")
col2=int(input())

if rows1==col2:
    matrix1=[]
    result=[]
    for rows in range(rows1):
        row1=[]
        for columns in range(col1):
            row1.append(int(input("Enter the element of matrix1")))
        matrix1.append(row1)
    matrix2=[]
    for rows in range(rows2):
        row2=[]
        for columns in range(col2):
            row2.append(int(input("Enter the element of matrix2")))
        matrix2.append(row2)
    for i in range(len(matrix1)):
        myList = []
        for j in range(len(matrix2[0])):
            m = 0;
            for k in range(len(matrix2)):
                m += matrix1[i][k] * matrix2[k][j]
            myList.append(m)
        result.append(myList)
    for r in range(len(result)):
	    print(result[r])
else:
    print("Error!")
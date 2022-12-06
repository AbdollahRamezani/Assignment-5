n=int(input("Please insert row : "))

matrix=[]

for i in range(n):
        row=[]
        for j in range(0,i+1):
            row.append(1)
        matrix.append(row)

for i in range(2,n):
        for j in range(1,i):
            matrix[i][j]=matrix[i-1][j]+matrix[i-1][j-1]

for row in matrix:
        for cell in row:
            print(cell,end=' ')
        print("")
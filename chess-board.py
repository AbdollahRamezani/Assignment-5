n=int(input("please enter row:"))
m=int(input("please enter col:"))

for row in range (n):
     for column in range(m):
        if (row % 2==0 and column % 2==0) or (row %2 !=0 and column %2 !=0 ):
                print("#",end="")
        else:
                print("*",end="")
     print("")


        
        
        
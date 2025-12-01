pos_x = int(input("x: "))
pos_y = int(input("y: "))
for i in range(1,9):
    for j in range(1,9):
        if i == pos_y and j == pos_x:                    
            print("F", end=' ')
        elif i == pos_y or j == pos_x:                   
            print("1", end=' ')
        elif abs( i - pos_y) == abs( j - pos_x):         
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()
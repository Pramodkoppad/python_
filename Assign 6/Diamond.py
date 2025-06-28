for row in range(5):
    for space in range(4-row):
        print(' ',end=" ")
    for col in range(row+1):
        print('*',end=" ")
    for col in range(row+1):
        print('*',end=" ")
    print()
for row in range(5):
    for space in range(row+1):
        print(' ',end=" ")
    for col in range(4-row):
        print('*',end=" ")
    for col in range(4-row):
        print('*',end=" ")
    print()
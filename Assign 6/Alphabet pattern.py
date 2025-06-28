alpha=65 #ascii value 
for row in range(6):
    for col in range(1,row+1):
        print(chr(64+col),end=" ")
    print( )
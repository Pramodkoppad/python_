tri1=int(input('Enter the lenght '))
tri2=int(input('Enter the lenght '))
tri3=int(input('Enter the lenght '))
if tri1==tri2 and tri2==tri3 and tri3==tri1 :
    print('Equilatreal')
elif tri1==tri2:
    print('Isosceles')
else:
    print('Scalane')
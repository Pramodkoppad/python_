age=int(input('Ente the age '))
if age>18:
    print('Allowed to football match ')
    if age>=18 and age<30:
        print('Need to pay $30','Indian Rupee',30*73,'GST 18%',(73*30)*(18/100))
    elif age>=30 and age<50:
        print('Need to pay $40','Indian Rupee',40*73,'GST 18%',(40*73)*(18/100))
    elif age>50:
        print('Free Entry')
else:
    print('Not allowed to football match')

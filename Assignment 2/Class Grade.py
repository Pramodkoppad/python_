marks_obt=int(input('Enter the obtained marks '))
total_marks=600
per=(marks_obt/total_marks)*100
if per<35:
    print('Fail')
elif per>=35 and per<50:
    print('B grade')
elif per>=50 and per<80:
    print('A grade')
elif per>80 and per<=100:
    print('A+ grade')
else:
    print('Invalid percentage',per)
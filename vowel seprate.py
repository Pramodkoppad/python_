val='abcdefgh'
a='aeiou,AEIOU'
for x in val:
    if x in a:
        print(x, end=',')


val='abcdefgh'
a='aeiou,AEIOU'
for x in val:
    if x not in a:
        print(x,end=',')

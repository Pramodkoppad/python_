a=int(input('Enter the temperature in Degree '))
b=input('Enter the Degree ')
if b=='Kelvin':
    x=a+273.15
    print('Temp in Kelvin',x)
elif b=='Fahrenheit':
    d=a*(9/5)+32
    print('Temperatue in Fahrenheit',d)
else:
    print("Default",a)
temperature=float(input('enter temperature:'))
print('select number:1.c->k 2.k->c 3.f->c 4.c->f 5.f->k 6.k->f')
number=(int(input('enter number:')))
if number==1:
    celsius=temperature-273
    print(celsius)
elif number==2:
    kelvin=temperature+273
    print(kelvin)   
elif number==3:
    farenhight=(temperature*1.8)+32
    print(farenhight) 
elif number==4:
    celsius=(temperature-32)/1.8
    print(celsius)
elif number==5:
    farenhight=1.8*(temperature-273)+32
    print(farenhight)
elif number==6:
    kelvin=(temperature+459)/1.8
    print(kelvin)

wight=int(input('please enter your wight (kg):'))
hight=float(input('please enter your hight (m):'))
mbi=wight/(hight**2)
print('your mbi:', mbi)
if 16<mbi<18.5 :
    print('eat enough food and get enough sleep :)')
elif 18.5 < mbi < 24:
    print('eat protein and vegetables :)')
elif 24< mbi <30:
    print('do exercise :)')
elif 30< mbi <35:
    print('do exercise and go on diet :)')
elif 35< mbi <40:
    print('eat vgetables and do exercise :)')
elif 40< mbi:
    print('do exercise and go to the docter and go on a diat :)')

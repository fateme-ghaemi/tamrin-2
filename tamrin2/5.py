num=int(input('enter numbert:'))
num1=num
maqus=0
while num > 0:
    num2=num%10
    maqus=((maqus*10)+num2)
    num//=10
if num ==maqus:
    print('number=maqus')
else:
    print('number is not equal to maqus')
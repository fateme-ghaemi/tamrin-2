num=int(input('enter your number:'))
even=0
odd=0
while num>0:
    x= num%10
    num=num//10
    if x%2==0:
        even+=1
    else:
        odd+=1
if even==odd:
    print('even=odd')
elif even>odd:
    print('even>odd')
elif even<odd:
    print('enen<odd')
    


num1 = int(input('Enter A Number To Find LCM:\n'))
num2 = int(input('Enter Another Number To Find LCM:\n'))
max_num = max(num1,num2)
while True:
    if max_num%num1==0 and max_num%num2==0:
        break
    max_num+=1
print(f'The LCM Of {num1} And {num2} Is {max_num}')
# HCF Finder
try:
    num1 = int(input('Enter Number One : \n'))
    num2 = int(input('Enter Number Two : \n'))
except:
    print('Error!')
min_num = min(num1,num2)
for i in range(1,min_num+1):
    if num2%i==0 and num1%i==0:
        hcf = i
print(f'HCF Of {num1} And {num2} Is {hcf}')
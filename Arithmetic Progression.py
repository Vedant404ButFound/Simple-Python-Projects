def createSeries(a:float,d:float,n:int)->tuple:
    progression = []
    for i in range(1,n+1):
        progression.append(a+((i-1)*d))
    return progression

def findNum(a:float,d:float,n:int)->float:
    a_of_n = createSeries(a,d,n)[-1]
    return a_of_n

def sumProgression(a:float,d:float,n:int)->float:
    l = createSeries(a,d,n)[-1]
    S = (n/2)*(a+l)
    return S

def findn(a:float,d:float,num:float)->int:
    series = createSeries(a,d,99999)
    return series.index(num)+1

command = input("Enter [C] to create progression\nEnter [F] to find a of n\nEnter [N] to find n number\nEnter [S] to sum all numbers in progression\n\nYour input : ")[0].lower()

if command=="c":
    ans = createSeries(float(input("Enter a : ")),float(input("Enter d : ")),int(input("Enter range of progression : ")))
    print(f"Your answer is {ans}")
elif command=="f":
    ans = findNum(float(input("Enter a : ")),float(input("Enter d : ")),int(input("Enter n : ")))
    print(f"Your answer is {ans}")
elif command=="n":
    ans = findn(float(input("Enter a : ")),float(input("Enter d : ")),float(input("Enter number : ")))
    if ans==-1:
        print(f"Given number didn't exist")
    else:
        print(f"Your answer is {ans}")
elif command=="s":
    ans = sumProgression(float(input("Enter a : ")),float(input("Enter d : ")),int(input("Enter n : ")))
    print(f"Your answer is {ans}")
else:
    print("Invalid input !!!")
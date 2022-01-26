def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return True
    return False

number = int(input("Enter a number to find given number is prime or not : "))
flag = is_prime(number)
if flag:
    print(f"\n{number} is a non-prime number.")
else:
    print(f"\n{number} is a prime number.")
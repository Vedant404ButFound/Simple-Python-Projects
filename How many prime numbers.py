def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return True
    return False

start = int(input("Enter first number to find prime numbers in given range : "))
stop = int(input("Enter last number to find prime numbers in given range : "))

prime_nums = [i for i in range(start,stop+1) if not is_prime(i)]
if 1 in prime_nums:
    prime_nums.remove(1)
print(f"All prime numbers between {start} to {stop} is given below\n\n{prime_nums}")
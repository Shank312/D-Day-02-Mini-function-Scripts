
# Check if a number is prime — divisible only by 1 and itself.

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
         return False
    return True

n = int(input("Enter the number n to check the number is prime or not : "))
print(is_prime(n))



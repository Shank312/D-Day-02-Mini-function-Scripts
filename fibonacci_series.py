
# Print the Fibonacci series up to n terms:  0, 1, 1, 2, 3, 5, 8, 13...

def fabonacci(n):
    if n <= 0:
        return [ ]
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib = [0, 1]
    for i in range (2, n):
        fib.append(fib[-2] + fib[-1])
    return fib


n = int(input("Enter the number n : "))
print(fabonacci(n))
     
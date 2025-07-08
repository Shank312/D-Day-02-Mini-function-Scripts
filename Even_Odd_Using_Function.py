
# Check whether a number is even or odd using a function.

def num(n):
    if n%2 == 0:
        return "even" 
    else:
        return "odd"
    
n = int(input("Enter the number n : "))
print(num(n))    

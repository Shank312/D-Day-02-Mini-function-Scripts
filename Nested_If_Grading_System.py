
'''
Problem:
Create a function that accepts a score and returns a grade based on the following logic:

90 <= score <= 100: Grade A

80 <= score < 90: Grade B

70 <= score < 80: Grade C

60 <= score < 70: Grade D

< 60: Grade F

Invalid: If score < 0 or > 100

'''

def score(n):
    if n < 0 or n > 100:
        return "Invalid"
    elif n >= 90:
        return "Grade A"
    elif n >= 80:
        return "Grade B"
    elif n >= 70: 
        return "Grade C"
    elif n >= 60: 
        return "Grade D"
    else:
        return "Grade F"
    
n = int(input("Enter the number n : "))
print(score(n))




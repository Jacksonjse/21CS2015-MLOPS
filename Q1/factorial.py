#FACTORIAL FUNCTION

def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n < 0:
        return "negative"
    else:
        return n * factorial(n-1)
def fibonnaci(n):
    first = 0
    second = 1
    lst = [first, second]
    
    if n==0 or n== 1:
        return n
    elif n<0:
        return False
    else:
        for i in range(n-2):
            lst.append(first + second)
            first = second
            second = lst[-1]
        return lst
if __name__ == "__main__":
    print(fibonnaci(8))
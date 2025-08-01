def find_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            print(i)
            if n%i == 0:
                return False
        return True

if __name__ == "__main__":
    print(find_prime(5))
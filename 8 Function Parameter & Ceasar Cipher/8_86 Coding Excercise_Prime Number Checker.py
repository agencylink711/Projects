# Prime Number Checker

n = int(input("Type your desired Number here: "))  # Check this number

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it's a Prime Number")
    else:
        print("It's NOT a prime number")

prime_checker(number=n)



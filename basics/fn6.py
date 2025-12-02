# WAF to accept a number and check whether the number is a prime number or not 
# and return boolean 

def check_prime(number):

    if number <= 1:
        return False
    # start = 2, stop = number - 1, step = 1

    for i in range(2,number):

        if number % i == 0:
            return False
        
    return True

n = int(input("Enter a number: "))

if check_prime(n):
    print(f"Number {n} is a prime number")
else:
    print(f"Number {n} is not a prime number")

# WAP to print series of prime number from 1 to n
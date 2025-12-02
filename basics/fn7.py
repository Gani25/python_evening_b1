# WAP to print series of prime number from 1 to n
# n = 100
# start = 2, stop = n
def check_prime(number):

    if number <= 1:
        return False
    # start = 2, stop = number - 1, step = 1

    for i in range(2,number):

        if number % i == 0:
            return False
        
    return True
def prime_number_series(num):
    if(num >=2):
        print(f"Series of prime number till {num}")
    else:
        print("Enter number greater than or equal to 2")
    for i in range(2,num+1):
        if(check_prime(i)):
            print(i, end=" ")

n = int(input("Enter a number: "))

prime_number_series(num=n)


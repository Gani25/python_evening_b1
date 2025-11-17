# WAP to check whether the number is prime number or not
# self table and only divisible by 1

num = int(input("Enter a number: "))

is_prime = True

if(num <= 1):
    is_prime = False

i = 2

while(i <= num-1):

    if num % i == 0:
        # is not prime
        is_prime = False
        break

    i = i + 1
if is_prime:
    print(f"Number = {num} is a prime number")
else:
    print(f"Number = {num} is not a prime number")
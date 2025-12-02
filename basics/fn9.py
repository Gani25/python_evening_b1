# create a function to check whether the number is Armstrong Number or Not

# create a function to print series of Armstrong Number from 1 to n

#Armstrong Number =  sum of digit of power of length

def calculate_digit(number:int):
    digit = 0
    while(number > 0):
        digit = digit + 1
        number = number // 10
    
    return digit

def check_armstrong(number:int):

    if number < 0:
        return False
    # Find total_digit
    if number >= 1 and number <= 9:
        total_digit = 1
    else:
        total_digit = calculate_digit(number)

    sum = 0
    i = number
    while i > 0:
        last_digit = i % 10
        power = last_digit ** total_digit
        sum = sum + power
        i = i // 10

    return number == sum

def print_armstrong_series(n:int):

    if n > 0:
        print(f"Armstrong Number from 1 to {n} is: ")
        for i in range(1,n+1):
            if(check_armstrong(i)):
                print(i, end=" ")
    else:
        print("Armstrong number is greater than 0")

num = int(input("Enter a number: "))

print_armstrong_series(n=num)
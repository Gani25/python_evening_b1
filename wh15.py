# WAP to check whether the number is Armstrong number or not
# Armstrong number
# sum of power of digit = number

num = input("Enter a number: ") 
if(int(num)> 0):
    digits = len(num)

    # convert num to integer
    num = int(num)
    i = num 
    sum = 0

    while i > 0:
        last_digit = i % 10
        power = last_digit ** digits
        sum = sum + power
        i = i // 10

    if(sum == num):
        print(f"Number = {num} is Armstrong Number")
    else:
        print(f"Number = {num} is not Armstrong Number, since sum of power of digits  = {sum}")

else:
    print("Armstrong Number cannot be negative")
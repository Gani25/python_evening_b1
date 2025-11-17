# WAP to reverse a number
# n = 1352 -> reverse = 2531 

num = int(input("Enter a number: "))

i = num

reverse = 0

while i > 0:
    last_digit = i % 10
    reverse = reverse * 10 + last_digit
    i = i // 10

print(f"Value of number = {num} and Reverse = {reverse}")

if(num == reverse):
    print("Palindrome")
else:
    print("Not a Palindrome")
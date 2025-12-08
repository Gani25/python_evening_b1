# Function which accept multiple values -> args

def addition(*numbers):
    print(numbers)
    
    print(type(numbers))
    print("Additions = ",sum(numbers))


addition(6,10,100,-60)



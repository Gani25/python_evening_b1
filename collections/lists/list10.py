matrix = [
    [10,20,30,66],
    [60,80,90,99],
    [1,3,9,35]
]



print(matrix)

for row in matrix:

    for col in row:
        print(col,end="\t")
    
    print()

print("Row Size = ",len(matrix))
print("Column Size = ",len(matrix[0]))
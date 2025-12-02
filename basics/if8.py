'''
Electricity Bill Generator:
Accept Unit Consumption
Based on below criteria charge bill amount
1. First 50 units: 5/unit
2. Next 150 units: 8/unit
3. Next 250 units: 15/unit // 500 -> 300
4. Units above 250: 20/unit
'''

unit_cosumption = int(input("Enter a number: "))
bill_amount = None
if unit_cosumption <= 50:
    bill_amount = unit_cosumption * 5
elif unit_cosumption <= 200:
    bill_amount = 50 * 5 + (unit_cosumption - 50) * 8
elif unit_cosumption <= 500:
    bill_amount = 50 * 5 + 150 * 8 + (unit_cosumption - 200) * 15
else:
    bill_amount = 50 * 5 + 150 * 8 + 250 * 15  + (unit_cosumption - 500) * 20

print(f"------------------------------------------------------------------\nUnit Consumed = {unit_cosumption}\nTotal Amount = {bill_amount}\n------------------------------------------------------------------")

'''
WAP to accept marks of 5 subject
Display sum and average
Based on average display grades:
if avg is above 90 -> A
if avg is above 75 -> B
if avg is above 50 -> C
if avg is above 35 -> D
if avg below 35 -> Fail
'''
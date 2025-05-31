number = int(input("Enter a number to see its multiplication table: "))
multiply_by = range(0,11,1)
for num in multiply_by:
    result = num * number
    print(f"{number} * {num} = {result}")
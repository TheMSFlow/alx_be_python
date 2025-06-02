FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celcius):
    return celcius * CELSIUS_TO_FAHRENHEIT_FACTOR

try:
    temp = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result:.2f}°F")
elif unit == "F":
    result = convert_to_celcius(temp)
    print(f"{temp}°F is {result:.2f}°C")
else:
    print("Invalid unit, cannot process")

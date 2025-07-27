FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result

while True:
    temperature = int(input("Enter the temperature to convert: "))
    celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if celsius_or_fahrenheit == "c":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature} celsius is {fahrenheit} fahrenheit")
    elif celsius_or_fahrenheit == "f":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature} fahrenheit is {celsius} celsius")
    else:
        print("Invalid temperature. Please enter a numeric value.")
        break

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_DIFFERENCE = 32

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using global factor."""
    return (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_DIFFERENCE

def main():
    temp_input = input("Enter the temperature to convert: ").strip()

    # Validate temperature input
    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}\u00B0F is {result}\u00B0C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}\u00B0C is {result}\u00B0F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()


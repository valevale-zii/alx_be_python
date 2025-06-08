# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Welcome to the Temperature Conversion Tool!")
    try:
        temp_input = input("Enter the temperature (numeric value): ").strip()
        temp_value = float(temp_input)  # Will raise ValueError if input is not numeric

        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted:.2f}°F.")
        elif unit == 'F':
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted:.2f}°C.")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

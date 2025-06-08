# temp_conversion_tool.py

# ✅ Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# ✅ Implement conversion functions
def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ✅ User interaction and input handling
def main():
    print("Welcome to the Temperature Conversion Tool!")
    try:
        temp_input = input("Enter the temperature (numeric value): ").strip()
        
        # Try to convert to float — if fails, raise ValueError
        temp_value = float(temp_input)

        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted:.2f}°F.")
        elif unit == 'F':
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted:.2f}°C.")
        else:
            # Explicit invalid unit check
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # ✅ Implementation of ValueError
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Invalid temperature. Please enter a numeric value.")

# Entry point
if __name__ == "__main__":
    main()


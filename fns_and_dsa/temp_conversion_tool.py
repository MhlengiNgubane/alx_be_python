# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion function: Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Conversion function: Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
def main():
    while True:
        try:
            # Prompt user for temperature input
            temperature_str = input("Enter the temperature to convert: ").strip()
            if not temperature_str:
                raise ValueError("Temperature value cannot be empty.")
                
            temperature = float(temperature_str)
            
            # Prompt user for unit input (Celsius or Fahrenheit)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            if unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature:.1f}°F is {converted_temp:.2f}°C")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature:.1f}°C is {converted_temp:.2f}°F")
            else:
                raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        except ValueError as e:
            print(f"Error: {e}")
            continue
        
        except KeyboardInterrupt:
            print("\nExiting...")
            break

# Entry point of the script
if __name__ == "__main__":
    main()

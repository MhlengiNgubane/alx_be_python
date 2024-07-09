def safe_divide(self, numerator, denominator):
    try:
        self.numerator = float(numerator)
        self.denominator = float(denominator)
        
        result = numerator / denominator
        
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
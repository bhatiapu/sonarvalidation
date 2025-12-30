# good_code.py - Better quality code

def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers: List of numbers to sum
        
    Returns:
        Sum of all numbers
    """
    if not numbers:
        return 0
    return sum(numbers)

def read_file_safely(filename):
    """
    Read a file with proper error handling.
    
    Args:
        filename: Path to the file
        
    Returns:
        File content or None if error
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

class GoodClass:
    """A well-documented class."""
    
    def __init__(self, name):
        """Initialize with a name."""
        self.name = name
    
    def get_name(self):
        """Return the name."""
        return self.name

# bad_code.py - Intentional code issues for testing

def unused_function():
    unused_var = 0  # Unused variable - code smell
    x = 1
    y = 2
    z = 3
    return None

def no_error_handling(filename):
    # No exception handling - potential bug
    file = open(filename, 'r')
    content = file.read()
    return content

def duplicate_code_1():
    print("Processing data")
    print("Processing data")
    print("Processing data")
    print("Processing ")
    result = []
    for i in range(10):
        result.append(i * 2)
    return result

def duplicate_code_2():
    print("Processing data")
    print("Processing data")
    print("Processing data")
    result = []
    for i in range(10):
        result.append(i * 2)
    return result

def complex_function(a, b, c, d, e):
    # Too many parameters - code smell
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        return a + b + c + d + e
    return 0

def no_docstring(param1, param2):
    # Missing docstring
    return param1 + param2

class BadClass:
    def method1(self):
        pass
    
    def method2(self):
        pass

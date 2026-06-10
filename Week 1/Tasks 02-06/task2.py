# Task 2: Data Type Explorer

# Variables Creation
Integer = 42
Float = 3.14
String = "Hello, World!"
Boolean = True
complex_Number = 2 + 3j

# Print data along with data type
print(f"Integer: {Integer} (Type: {type(Integer).__name__})")
print(f"Float: {Float} (Type: {type(Float).__name__})")
print(f"String: {String} (Type: {type(String).__name__})")
print(f"Boolean: {Boolean} (Type: {type(Boolean).__name__})")
print(f"Complex Number: {complex_Number} (Type: {type(complex_Number).__name__})")

print("\nData Type Conversions:")

# Convert Integer to Float
Integer_to_Float = float(Integer)
print(f"Integer to Float: {Integer_to_Float} (Type: {type(Integer_to_Float).__name__})")

# Convert Float to String
Float_to_String = str(Float)
print(f"Float to String: '{Float_to_String}' (Type: {type(Float_to_String).__name__})")

# Convert Integer to String
Integer_to_String = str(Integer)
print(f"Integer to String: '{Integer_to_String}' (Type: {type(Integer_to_String).__name__})")
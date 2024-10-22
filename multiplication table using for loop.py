Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input("Enter a number to print its multiplication table: "))
Enter a number to print its multiplication table: 8
>>> print(f"Multiplication Table of {num}:")
Multiplication Table of 8:
>>> for i in range(1, 11):
	 result = num * i
	 print(f"{num} x {i} = {result}")

	 
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
>>> input_string = input("Enter a string: ")
Enter a string: Bhavya sujatha 2002@
>>> letters_count = 0
>>> digits_count = 0
>>> special_symbols_count = 0
>>> for char in input_string:
	if char.isalpha():
		letters_count += 1
	elif char.isdigit():
		digits_count += 1
	elif not char.isspace():
		special_symbols_count += 1
   print(f"Letters: {letters_count}")
   
SyntaxError: unindent does not match any outer indentation level
>>> input_string = input("Enter a string: ")
Enter a string: Bhavya sujatha2002@
>>> for char in input_string:
	if char.isalpha():
		letters_count += 1
	elif char.isdigit():
		digits_count += 1
	elif not char.isspace():
		special_symbols_count += 1
print(f"Letters: {letters_count}")
SyntaxError: invalid syntax
>>> for char in input_string:
	if char.isalpha():
		letters_count += 1
	elif char.isdigit():
		digits_count += 1
	elif not char.isspace():
		special_symbols_count += 1
        print(f"Letters: {letters_count}")
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for char in input_string:
	if char.isalpha():
		letters_count += 1
	elif char.isdigit():
		digits_count += 1
	elif not char.isspace():
		special_symbols_count += 1
                print(f"Letters: {letters_count}")
                
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for char in input_string:
	if char.isalpha():
		letters_count += 1
	elif char.isdigit():
		digits_count += 1
	elif not char.isspace():
		special_symbols_count += 1
        print(f"Letters: {letters_count}")
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
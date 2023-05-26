"""

Q.1. Create two int type variables, apply addition, subtraction, division and multiplications and store the results in variables. Then print the data in the following format by calling the variables:
First variable is __ & second variable is __. Addition: __ + __ = __
Subtraction: __ - __ = __
Multiplication: __ * __ = __
Division: __ / __ = __

"""

# Solution

# Create two variables
first_variable = 40
second_variable = 30

# Perform arithmetic operations and store the results
addition = first_variable + second_variable
subtraction = first_variable - second_variable
multiplication = first_variable * second_variable
division = first_variable / second_variable

# Print the results
print("First variable is", first_variable, "& second variable is", second_variable) # First variable is 40 & second variable is 30
print("Addition:", first_variable, "+", second_variable, "=", addition) # Addition: 40 + 30 = 70
print("Subtraction:", first_variable, "-", second_variable, "=", subtraction) # Subtraction: 40 - 30 = 10
print("Multiplication:", first_variable, "*", second_variable, "=", multiplication) # Multiplication: 40 * 30 = 1200
print("Division:", first_variable, "/", second_variable, "=", division) # Division: 40 / 30 = 1.3333333333333333


"""

Q.2. What is the difference between the following operators:
(i) ‘/’ & ‘//’
(ii) ‘**’ & ‘^’

Solution- (i) The difference between the / and // operators is as follows:
              '/' is the division operator, which performs normal division and returns a float result.
              '//' is the floor division operator, which performs division and rounds down the result to the nearest whole number. It returns an integer result.
                
              Example- x = 5
                       y = 2
                        
                       result1 = x / y
                       result2 = x // y
                        
                       print(result1)  # Output: 2.5
                       print(result2)  # Output: 2
                       
              '**' is the exponentiation operator, which raises the left operand to the power of the right operand.
               '^' is not the exponentiation operator. Instead, it is the bitwise XOR operator, used for performing bitwise XOR operation on the binary representation of the operands.


             Example- x = 2
                      y = 3
                        
                      result1 = x ** y
                      result2 = x ^ y
                        
                      print(result1)  # Output: 8
                      print(result2)  # Output: 1 (bitwise XOR of 2 and 3 in binary is 0001, which is 1 in decimal)


"""

"""
Q.3. List the logical operators.

Solution- The logical operators are:

           (i) and: The and operator returns True if both operands are True, and False otherwise.
           
           (ii) or: The or operator returns True if at least one of the operands is True, and False otherwise.
           
           (iii) not: The not operator returns the opposite boolean value of its operand. If the operand is True, not returns False, and if the operand is False, not returns True.

"""

"""

Q.4. Explain right shift operator and left shift operator with examples.

Solution- (i) right shift operator- The right shift operator (>>) are bitwise shift operators. It moves the bits of a number towards the right by a specified number of positions.
                                    Each shift to the right effectively divides the number by 2. The rightmost bit is discarded, and a new bit of 0 is inserted at the leftmost position.
                                    
                                    Example- x = 10  # Binary: 1010
                                             shifted = x >> 2  # Right shift by 2 positions
                                            
                                             print(shifted)  # Output: 2
                                             
                                             
         (ii) left shift operator- The left shift operator (<<) are bitwise shift operators. It moves the bits of a number towards the left by a specified number of positions.
                                   Each shift to the left effectively multiplies the number by 2. The leftmost bit is discarded, and a new bit of 0 is inserted at the rightmost position.  
                                   
                                   Example- x = 5  # Binary: 101
                                            shifted = x << 3  # Left shift by 3 positions
                                            
                                            print(shifted)  # Output: 40
                            
         

"""

"""

Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is present in the list or not.

"""

# Solution

# Create a list of integers

my_list = [2, 6, 8, 10, 12, 14, 16, 23, 25, 29, 30, 32, 34, 39, 40]

# Check if 10 is present in the list
if 10 in my_list:
    print('10 is present in the list.')
else:
    print('10 is not present in the list. ')
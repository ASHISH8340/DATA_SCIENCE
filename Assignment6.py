"""
Q.1. What are keywords in python? Using the keyword library, print all the python keywords.

Solution- Keywords in Python are reserved words that have predefined meanings and cannot be used as variable names or identifiers.


"""

# Program
import keyword

# Get all the Python keywords as a list
all_keywords = keyword.kwlist

# Print each keyword
for keyword in all_keywords:
    print(keyword)

"""
Q.2. What are the rules to create variables in python?

Solution- A variable name must start with a letter or the underscore character
          A variable name cannot start with a number
          A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
          Variable names are case-sensitive (age, Age and AGE are three different variables).

"""

"""
Q.3. What are the standards and conventions followed for the nomenclature of variables in python to improve code readability and maintainability?

Solution- In Python, following certain standards and conventions for variable naming can greatly improve code readability and maintainability. Here are some commonly followed standards and conventions:

            1. Use descriptive names: Choose variable names that are meaningful and describe the purpose or content of the variable. This helps in understanding the code and its intent.

            2. Use lowercase letters: Variable names in Python are typically written in lowercase letters. This is known as the "lowercase with underscores" or "snake_case" convention. For example: my_variable, total_count.

            3. Separate words with underscores: If a variable name consists of multiple words, separate them with underscores for better readability. This enhances the clarity and distinguishes between individual words. For example: first_name, student_age.

            4. Avoid single-letter variable names: While single-letter variable names like x, y, or i are allowed, it's generally recommended to use more descriptive names that convey the purpose of the variable. This improves code readability and makes it easier to understand the context.

            5. Be consistent and meaningful: Maintain consistency in naming conventions throughout your codebase. Use variable names that accurately represent the data they hold or the functionality they support. Avoid generic names like data, value, or temp unless the purpose is clear within the context.

            6. Follow the PEP 8 style guide: PEP 8 is a widely accepted style guide for Python code. It provides guidelines for writing clean and readable code, including variable naming conventions. Adhering to PEP 8 can make your code more consistent and easier to understand by other developers.
"""

"""

Q.4. What will happen if a keyword is used as a variable name?

Solution- If a keyword is used as a variable name, it will result in a syntax error. Keywords have predefined meanings and are reserved for specific purposes in the language.
          They cannot be used as variable names or identifiers.

"""

"""
Q.5. For what purpose def keyword is used?

Solution- The def keyword is used to create, (or define) a function.

"""

"""
Q.6. What is the operation of this special character ‘\’?

Solution- The backslash (\) is used as an escape character. It is used to indicate that the character following it has a special meaning or needs to be treated differently.

"""

"""
Q.7. Give an example of the following conditions: 
(i)   Homogeneous list
(ii)  Heterogeneous set
(iii) Homogeneous tuple

Solution- (i) Homogeneous list: A homogeneous list is a list where all the elements have the same data type.
                                Here's an example of a homogeneous list containing integers:
                                
                                integer_list = [1, 2, 3, 4, 5]
            
            
          (ii) Heterogeneous set: A heterogeneous set is a set where the elements can have different data types.
                                  Here's an example of a heterogeneous set containing elements of different types:
                                  
                                  heterogeneous_set = {1, 'apple', 3.14, True}
                                  
                                  
          (iii) Homogeneous tuple: A homogeneous tuple is a tuple where all the elements have the same data type.
                                   Here's an example of a homogeneous tuple containing strings:
                                   
                                   string_tuple = ('apple', 'banana', 'cherry')




"""


"""
Q.8. Explain the mutable and immutable data types with proper explanation & examples.

Solution- (i) Mutable Data Types: Mutable data types are those whose values can be modified after they are created.
                                  Examples of mutable data types in Python include:
                                  List
                                  Set
                                  Dictionary
                                  
                                  Here's an example demonstrating the mutability of a list:
                                  
                                  my_list = [1, 2, 3]
                                  my_list.append(4)       # Adding an element to the list
                                  my_list[1] = 5          # Modifying a specific element
                                    
                                  print(my_list)          # Output: [1, 5, 3, 4]
                                  
                                  
         (ii) Immutable Data Types: Immutable data types are those whose values cannot be modified after they are created. If you need to change the value of an immutable object, you have to create a new object with the desired value.
                                    Examples of immutable data types in Python include:

                                    Numeric types: int, float, complex
                                    String
                                    Tuple
                                    
                                    
                                    Here's an example demonstrating the immutability of a string:
                                    
                                    string = "Hello"
                                    new_string = string + " World"  # Concatenating strings
                                    
                                    print(string)       # Output: "Hello"
                                    print(new_string)   # Output: "Hello World"



"""

"""
Q.9. Write a code to create the given structure using only for loop.
         *
        ***
       *****
      *******
     *********

"""

# Solution

num_rows = 5  # Number of rows in the structure

for i in range(num_rows):
    # Print spaces before each row
    for j in range(num_rows - i - 1):
        print(" ", end="")

    # Print asterisks for each row
    for k in range(2 * i + 1):
        print("*", end="")

    print()  # Move to the next line


"""
Q.10. Write a code to create the given structure using while loop.

        |||||||||
         ||||||| 
          ||||| 
           ||| 
            |
"""
# Solution

num_rows = 5  # Number of rows in the structure
row = num_rows
spaces = 0

while row > 0:
    # Print spaces before each row
    spaces_count = 0
    while spaces_count < spaces:
        print(" ", end="")
        spaces_count += 1

    # Print vertical bars for each row
    bars_count = 0
    while bars_count < 2 * row - 1:
        print("|", end="")
        bars_count += 1

    print()  # Move to the next line
    row -= 1
    spaces += 1

"""
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
/
+
6
"""

"""
solution: 
--values--
    'hello' - String
    -87.8   - float
     6      - integer
     
--Expression--
    -    ->  Subtraction
    /    ->  Division Operator
    +    ->  Addition
 
    
"""

"""
2. What is the difference between string and variable?

solution- A string is a data type used to represent a sequence of characters.
          A variable is usa named storage location that can hold different types of values. It is used
          to store a value or an object in memory.
"""
"""
3. Describe three different data types.

solution- 1. int data type:
                We can use int data type to represent whole numbers (integral values)
                 Eg; a = 10
                 type(a) #int
                 
          2. bool data type:
                We can use this data type to represent boolean values.
                The only allowed values for this data type are:
                    • True and False
                    • Internally Python represents True as 1 and False as 0
                      Eg;  b = True
                           type(b) -›bool
                           
          3. float data type:
                . We can use float data type to represent floating point values (decimal values).
                  Eg: f= 1.234
                     type(f) #float
                . We can also represent floating point values by using exponential form (Scientific Notation)
                  Eg: f = 1.2e3 -> instead of 'e' we can use 'E' 
                      print(f) 1200.0
                  
                . The main advantage of exponential form is we can represent big values in less memory.
"""

"""
4. What is an expression made up of? What do all expressions do?

solution- Expression is made up of combination of values, variables, operators, and function calls that evaluates 
          to a single value.
          
          The purpose of an expression is to compute a value by combining and evaluating the provided components.
          
          Expressions  can include the following components:

          Values:       These can be literals such as numbers (e.g., 1, 3.14) or strings (e.g., "hello", 'world'). 
                        Values can also include constants, boolean values (True or False), or special values like None.

          Variables:    These are names that represent stored values in memory. 
                        Variables can hold different types of values, and their contents can be used within expressions.

          Operators:    These are symbols that perform operations on values or variables. 
                        various operators such as arithmetic operators (+, -, *, /), 
                        comparison operators (==, !=, >, <, >=, <=), logical operators (and, or, not), 
                        assignment operators (=, +=, -=, *=, /=), and more.

         Function calls: These involve calling built-in or user-defined functions that perform specific operations
                         or return values. Functions can be used within expressions to manipulate values or perform computations.

"""
"""
5. This assignment statements, like spam = 10. What is the difference between an
   expression and a statement?
   
solution-  Expressions are used to calculate values or perform operations.
           
           Statement is a complete unit of code that performs an action or carries out a specific task.
"""
# 10 + 5 * 2 is an expression that evaluates to 16. The resulting value is then assigned to the variable spam.
spam = 10 + 3 * 2
print(spam)

# spam = 10 is an assignment statement that assigns the value 10 to the variable spam
spam = 10  # Assignment statement
# if statement is a conditional statement that controls the flow of execution based on the condition
if spam > 5:  # Conditional statement
    print("Spam is greater than 5")  # Print statement

"""
6. After running the following code, what does the variable bacon contain?
    bacon = 22
    bacon + 1
    
solution - The variable bacon will still contain the value 22. The expression bacon + 1 evaluates to 23, but it is not 
           assigned to any variable. Therefore, the value of bacon remains unchanged. 
           If you want to update the value of bacon with the result of bacon + 1:
           
           bacon = bacon + 1

"""
"""
 7. What should the values of the following two terms be?
     'spam' + 'spamspam'
     'spam' * 3
     
solution - 'spam' + 'spamspam' - spamspamspam
            'spam' * 3         - spamspamspam
"""
# program:
a = 'spam' + 'spamspam'
b = 'spam' * 3
print(a) # spamspamspam
print(b) # spamspamspam

"""
8. Why is eggs a valid variable name while 100 is invalid?

solution- "eggs" is a valid variable name because it consists of lowercase letters and does not start with a digit or 
           contain any special characters. It follow to the rules for variable names in Python.
            
          "100" is invalid as a variable name because it starts with a digit. Variable names cannot begin with a number;
           they must start with a letter or an underscore. Therefore, "100" violates the naming rules
           and is not a valid variable name in Python.
"""

"""
9. What three functions can be used to get the integer, floating-point number, or string version of a value?

"""
# solution:
x = int(6.8)  # Converts float 6.8 to integer 6
print(x)
y = int("10")  # Converts string "10" to integer 10
print(y)

a = float(6)  # Converts integer 6 to float 6.0
print(a)
b = float("1.11")  # Converts string "1.11" to float 1.11
print(b)

c = str(12)  # Converts integer 12 to string "12"
print(c)
d = str(1.11)  # Converts float 1.10 to string "1.11"
print(d)

"""
10. Why does this expression cause an error? How can you fix it?
    'I have eaten' + 99 + 'burritos'

solution - cause an error because concatenate a string ('I have eaten') with an integer (99).
           so, we resolve this error by casting or taking 99 as string '99'
           
            'I have eaten ' + str(99) + ' burritos.'
            'I have eaten ' + '99' + ' burritos.'

    
"""
# Program

x = 'I have eaten ' + str(99) + ' burritos.'
print(x)

y = 'I have eaten ' + '99' + ' burritos.'
print(y)
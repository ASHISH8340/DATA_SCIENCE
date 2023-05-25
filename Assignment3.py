"""
1. Why are functions advantageous to have in your programs?

Solution- Functions allow to write modular and reusable code. You can define a function once and then use it multiple times throughout your program.
          This saves time and effort by avoiding the need to rewrite the same code in multiple places.

"""

"""

2. When does the code in a function run: when it's specified or when it's called?

Solution- The code in a function runs when the function is called, not when it is specified.

"""


# Program
def greet():
    print("Hello, world!")


print("Before function call")
greet()
print("After function call")

# output
# Before function call
# Hello, world!
# After function call

"""
3. What statement creates a function?

Solution- The def statement is used to create a function

"""

"""
4. What is the difference between a function and a function call?

Solution- 1. Function: A function consists of the def statement and the code in its def clause.
          2. Function Call: A function call is the actual execution of a function. It is the point in the program where the code inside the function is run.
                            The function call transfers control to the function, executes the code within it, and returns the result (if applicable).
"""

"""
5. How many global scopes are there in a Python program? How many local scopes?

Solution- There is one global scope, and a local scope is created whenever a function is called.

"""

"""
6. What happens to variables in a local scope when the function call returns?

Solution- When a function returns, the local scope associated with that function is destroyed, and the variables defined within that local scope cease to exist.

"""

"""
7. What is the concept of a return value? Is it possible to have a return value in an expression?

Solution- A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.

"""

"""
8. If a function does not have a return statement, what is the return value of a call to that function?

Solution- If a function does not have a return statement, the return value of a call to that function is None.

"""


# Program
def greet(name):
    print("Hello, " + name + "!")


result = greet("Ashish")
print(result)  # Output: None

"""
9. How do you make a function variable refer to the global variable?

Solution- You can make a function variable refer to a global variable by using the global keyword within the function.

"""
# Program

count = 0


def increment_counter():
    global count
    count += 1


increment_counter()
print(count)  # Output: 1

"""
10. What is the data type of None?

Solution- The data type of None is NoneType.

"""
# Program
result = None
print(type(result))  # Output: <class 'NoneType'>


"""
11. What does the sentence import areallyourpetsnamederic do?

Solution- That import statement imports a module named areallyourpetsnamederic. (This isn't a real Python module, by the way.)

"""

"""
12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

Solution- This function can be called with spam.bacon().
          
          Example- import spam
                   spam.bacon()


"""

"""
13. What can you do to save a programme from crashing if it encounters an error?

Solution- To prevent a program from crashing when it encounters an error, we can implement error handling mechanisms using exception handling.
          
          The key components of exception handling are try, except, else, and finally blocks.

"""

"""
14. What is the purpose of the try clause? What is the purpose of the except clause?

Solution- The purpose of the try clause is to define a block of code where you anticipate that an exception may occur. It allows you to enclose the code that might raise an exception and handle it gracefully. The try clause is followed by one or more except clauses.

          The purpose of the except clause is to define a block of code that will be executed if a specific exception occurs within the associated try block. The except clause allows you to catch and handle specific types of exceptions that may occur during the execution of the try block.
          It helps you provide alternative code paths or error handling logic to handle exceptional conditions without causing the program to crash.
"""
"""
1.What are the two values of the Boolean data type? How do you write them?

solution- There are the two values of the Boolean data type:
          1. True
          2. False

          x = True
          y = False
"""
# Program
a = 10
b = 20
c = a < b
print(c) # True
d = a > b
print(d) # False

"""
2. What are the three different types of Boolean operators?

Solution- There are three different types of Boolean operators:
          1. Logical AND (and)
          2. Logical OR (or)
          3. Logical NOT (not)
"""

"""
3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for 
    the operator and what it evaluate ).
    
Solution- 1. Logical AND (and): This operator returns True if both operands are True, and False otherwise. 
                                It evaluates to False as soon as any operand is False.
                                
                                Truth Table:
                                Operand 1	Operand 2	Result
                                    True	 True	    True
                                    True	 False	    False
                                    False	 True	    False
                                    False	 False	    False
                                    
         2. Logical OR (or): This operator returns True if at least one of the operands is True, and False if both operands are False.
                             It evaluates to True as soon as any operand is True.
                             
                             Truth Table:
                             Operand 1	Operand 2	Result
                              True	     True	    True
                              True	     False	    True
                              False	     True	    True
                              False	     False	    False
                              
                              
        3. Logical NOT (not): This operator is a unary operator that negates the value of its operand. 
                              It returns True if the operand is False, and False if the operand is True.
                              
                              Truth Table:
                              Operand	Result
                              True	    False
                              False	    True

"""

"""
4. What are the values of the following expressions?
        (5 > 4) and (3 == 5)
        not (5 > 4)
        (5 > 4) or (3 == 5)
        not ((5 > 4) or (3 == 5))
        (True and True) and (True == False)
        (not False) or (not True)
        
solution -  (5 > 4) and (3 == 5) evaluates to False.
            not (5 > 4) evaluates to False.
            (5 > 4) or (3 == 5) evaluates to True.
            not ((5 > 4) or (3 == 5)) evaluates to False.
            (True and True) and (True == False) evaluates to False.
            (not False) or (not True) evaluates to True.
        

"""
# Program
a = 5 > 4 #True
b = 3 == 5 #False
result = a and b
print(result) #False

c = 5 > 4 #True
result = not c
print(result) #False

d = 5 > 4 #True
e = 3 == 5 #False
result = d or e
print(result) #True

f = 5 > 4 #True
g = 3 == 5 #False
h = f or g #True
result = not h
print(result) #False


i = True and True #True
j = True == False #False
result = i and j
print(result) #False


k = not False #True
l = not True  #False
result = k or l
print(result) #True

"""
5. What are the six comparison operators?

Solution- There are the six comparison operators:
          1. Equal to (==)
          2. Not equal to (!=)
          3. Greater than (>)
          4. Less than (<)
          5. Greater than or equal to (>=)
          6. Less than or equal to (<=)

"""

"""
6. How do you tell the difference between the equal to and assignment operators?
   Describe a condition and when you would use one.
   
Solution- The equal to operator (==) is used for comparison, while the assignment operator (=) is 
          used for variable assignment.
"""
# 1. Equal to operator (==): It is used to compare if two values are equal. It evaluates the equality of the operands and returns True if they are equal, and False otherwise
# Program

x = 5
y = 7

if x == y: #Equal to operator (==)
    print("x and y are equal")
else:
    print("x and y are not equal")

# 2. Assignment operator (=): It is used to assign a value to a variable. It assigns the value on the right side of the operator to the variable on the left side
x = 5 #Assignment operator (=)

"""
7. Identify the three blocks in this code:
    spam = 0
    if spam == 10:
    print('eggs')
    if spam > 5:
    print('bacon')
    else:
    print('ham')
    print('spam')
    print('spam')

Solution - There are three blocks in this code:
           Block 1:  if spam == 10:
                     print('eggs')
                     
           Block 2:  if spam > 5:
                     print('bacon')
                     
           Block 3:    else:
                       print('ham')
                       print('spam')
                       print('spam')

"""

"""
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

Solution- 
            # Give different-different spam values
                spam = 2
                if spam == 1:
                    print('Hello')
                
                elif spam == 2:
                    print('Howdy')
                
                else:
                    print('Greetings!')
"""
# Program
# Give different-different spam values
spam = 2
if spam == 1:
    print('Hello')

elif spam == 2:
    print('Howdy')

else:
    print('Greetings!')


"""
9.If your programme is stuck in an endless loop, what keys you’ll press?

Solution- CTRL + C 
"""

"""

10. How can you tell the difference between break and continue?

Solution- 1. break statement: When the break statement is encountered within a loop, it immediately terminates the loop 
                              and transfers the control to the next statement after the loop.
                              
                              for i in range(1, 5):
                                    if i == 3:
                                        break
                                    print(i)
                                    
                                output - 1
                                         2
                                         
         2. continue statement: When the continue statement is encountered within a loop, it immediately skips the rest of the loop's code 
                                for the current iteration and moves to the next iteration.
                                
                                for i in range(1, 5):
                                    if i == 3:
                                        continue
                                    print(i)
                                    
                                output - 1
                                         2
                                         4
                                
                                
"""
# Program
# break statement
for i in range(1, 5):
    if i == 3:
        break
    print(i)# 1  2

# continue statement
for i in range(1, 5):
    if i == 3:
        continue
    print(i)# 1 2 4

"""
11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Solution- 1. range(10): This expression generates a sequence of numbers starting from 0 and ending at 9 (exclusive), incrementing by 1 by default. It is equivalent to range(0, 10, 1)


          2. range(0, 10): This expression generates a sequence of numbers starting from 0 and ending at 9 (exclusive), incrementing by 1. The starting value of 0 is explicitly specified. 
          3. range(0, 10, 1): This expression generates a sequence of numbers starting from 0 and ending at 9 (exclusive), incrementing by 1. Both the starting value and the increment are explicitly specified.
          
          The difference lies in the way the arguments are provided to the range() function, with the second and third forms allowing explicit specification of the starting value and the increment.
"""

"""
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

"""
# Solution
# Program of For loop

for i in range(1, 11):
    print(i)

# Program of while loop

i = 1
while i < 11:
    print(i)
    i += 1

"""
13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

Solution-  import spam
           spam.bacon()


"""


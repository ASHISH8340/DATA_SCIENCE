"""
1. What exactly is []?

Solution- An empty list [] is a list with no elements. It signifies that the list is currently empty and does not contain any items.
"""

# Program

my_list = []
print(my_list)  # Output: []

"""
2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
  

Solution- spam[2] = 'hello' (The third value in a list is at index 2 because the first index is 0.)
"""

# Program
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
print(spam)  # Output: [2, 4, 'hello', 8, 10]

"""
 Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

"""

"""
3. What is the value of spam[int(int('3' * 2) / 11)]?

Solution-  '3' * 2 results in the string '33'.
            int('33') converts the string to an integer 33.
            33 / 11 performs integer division, resulting in 3.
            spam[3] accesses the element at index 3 in the list spam.
            
            Therefore, the value of spam[int(int('3' * 2) / 11)] is 'd'.

"""

"""
4. What is the value of spam[-1]?

Solution- 'd' (Negative indexes count from the end.)


"""

"""
5. What is the value of spam[:2]?

Solution- '['a', 'b']'

"""

# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

"""
6. What is the value of bacon.index('cat')?

Solution- 1

"""

"""
7. How does bacon.append(99) change the look of the list value in bacon?

Solution- [3.14, 'cat', 11, 'cat', True, 99]

"""

"""
8. How does bacon.remove('cat') change the look of the list in bacon?

Solution- [3.14, 11, 'cat', True]

"""

"""
9. What are the list concatenation and list replication operators?

Solution- 1. List Concatenation (+): The + operator is used to concatenate or combine two lists into a single list. 
                                     It creates a new list that contains all the elements from both lists, in the order they appear.
          
          2. List Replication (*): The * operator is used for list replication, which means creating a new list by repeating the elements of an existing list multiple times.
"""

# Program
# List Concatenation (+):
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# List Replication (*):
original_list = [1, 2, 3]
replicated_list = original_list * 3
print(replicated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

"""
10. What is difference between the list methods append() and insert()?

Solution- append() will add values only to the end of a list, insert() can add them anywhere in the list.

"""
# Program

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # Output: [1, 5, 2, 3]

"""
11. What are the two methods for removing items from a list?

Solution- The del statement and the remove() list method are two ways to remove values from a list.

"""

"""
12. Describe how list values and string values are identical.

Solution- The identical between Lists and Strings is that both are sequences.

"""

"""
13. What's the difference between tuples and lists?

Solution- Lists are mutable; they can have values added, removed, or changed. It use the square brackets, [ and ].
          Tuples are immutable; they cannot be changed at all. It using parentheses ( and ).
"""

# Program
# list
fruits = ["bananas", "apple", "pineapple"]
print(fruits)  # ['bananas', 'apple', 'pineapple']

fruits[1] = "mango"
print(fruits)  # ['bananas', 'mango', 'pineapple']

# tuple
fruits = ("bananas", "apple", "pineapple")
print(fruits)  # ('bananas', 'apple', 'pineapple')

"""
14. How do you type a tuple value that only contains the integer 42?

Solution- (42,) (The trailing comma is mandatory.)

"""

"""
15. How do you get a list value's tuple form? How do you get a tuple value's list form?

Solution- To convert a list value to its tuple form, you can use the tuple().

          Example- my_list = [1, 2, 3, 4, 5]
                   my_tuple = tuple(my_list)
                   print(my_tuple)  # output- (1, 2, 3, 4, 5)

         To convert a tuple value to its list form, you can use the list() function.
         
         Example- my_tuple = (1, 2, 3, 4, 5)
                  my_list = list(my_tuple)
                  print(my_list) # output- [1, 2, 3, 4, 5]



"""

"""

16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

Solution- They contain references to list values.

"""

# Program
my_list = [1, 2, 3, 4, 5]
another_list = my_list

# Modifying the list through the 'another_list' variable
another_list.append(6)

print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
print(another_list)  # Output: [1, 2, 3, 4, 5, 6]

"""
17. How do you distinguish between copy.copy() and copy.deepcopy()?

Solution- The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list.
          That is, only copy.deepcopy() will duplicate any lists inside the list.


"""

import copy

original_list = [1, 2, [3, 4]]
deepcopied_list = copy.deepcopy(original_list)

# Modify a mutable element in the deepcopied list
deepcopied_list[2][0] = 50

print(original_list)  # Output: [1, 2, [3, 4]]
print(deepcopied_list)  # Output: [1, 2, [50, 4]]

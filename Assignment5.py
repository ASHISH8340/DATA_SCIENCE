"""
1. What does an empty dictionary's code look like?

Solution- 1. my_dict = {}
          2. my_dict = dict()

"""

"""
2. What is the value of a dictionary value with the key 'foo' and the value 42?

Solution- my_dict = {"foo": 42}
                    print(my_dict["foo"]) # output-42


"""
# Program
my_dict = {"foo": 42}
print(my_dict["foo"])#42

"""
3. What is the most significant distinction between a dictionary and a list?

Solution- The most significant distinction between a dictionary and a list is that a dictionary is a hash table, while a list is an ordered sequence. 
          This means that dictionaries can be accessed quickly using the key, while lists must be accessed using their index.
"""
# Program
# Dictionary
my_dict = {"foo": 42}

print(my_dict["foo"])#42

#List

my_list = [1, 2, 3]

#print(my_list["foo"])#Error

"""
4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

Solution-   If try to access spam['foo'] when spam is a dictionary with the key-value pair {'bar': 100}, 
            we will get a KeyError exception. This is because the key 'foo' does not exist in the dictionary.

"""

"""
5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

Solution- If a dictionary is stored in the variable spam, there is a difference between the expressions 'cat' in spam and 'cat' in spam.keys():

          1. 'cat' in spam: This expression checks if the key 'cat' exists in the dictionary spam. It returns True if the key is present in the dictionary as a key, and False otherwise. This expression directly checks for the presence of the key in the dictionary.

          2. 'cat' in spam.keys(): This expression checks if the key 'cat' exists in the list of keys of the dictionary spam. It returns True if the key is present in the list of keys, and False otherwise. This expression retrieves all the keys of the dictionary using the keys() method and then checks for the presence of the key in that list.



"""

# Program
spam = {'name': 'Ashish', 'age': 25, 'city': 'Varanasi'}

print('name' in spam)           # True
print('Ashish' in spam)           # False

print('Ashish' in spam.keys())  # False
print('age' in spam.keys())  # True

"""
6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?


Solution-  If a dictionary is stored in the variable spam, there is a difference between the expressions 'cat' in spam and 'cat' in spam.values():

           1. 'cat' in spam: This expression checks if the key 'cat' exists in the dictionary spam. It returns True if the key is present in the dictionary as a key, and False otherwise. This expression directly checks for the presence of the key in the dictionary.

           2. 'cat' in spam.values(): This expression checks if the value 'cat' exists in the dictionary spam. It returns True if the value is present in any of the dictionary's values, and False otherwise. This expression retrieves all the values of the dictionary using the values() method and then checks for the presence of the value in that list.
"""
# Program
spam = {'name': 'Ashish', 'age': 25, 'city': 'Varanasi'}

print('name' in spam)           # True
print('Ashish' in spam)           # False

print('Ashish' in spam.values())  # True
print('age' in spam.values())   # False






"""
7. What is a shortcut for the following code?
        if 'color' not in spam:
        spam['color'] = 'black'
        
Solution-  spam.setdefault('color', 'black')


"""

"""
8. How do you "pretty print" dictionary values using which module and function?

Solution- To pretty print dictionary values use the pprint() function from the pprint module.

            # Program
            import pprint
            
            spam = {'foo': 1, 'bar': 2}
            
            pprint(spam)# output- {'foo': 1, 'bar': 2}



"""



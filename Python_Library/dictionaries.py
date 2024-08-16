# we use dictionaries for when we need to store key value pairs
# for example names or phone numbers of a customer

# this first example is a simple demonstration of dictionaries
customer = {  # must go in curly brackets
    'name': 'John Smith',
    'age': 30,  # You can never have duplicates in a dictionary otherwise you will get an error
    # You can put any data type in a dictionary (list, string, int, float, bollean etc)
    'is_verified': True
}
# To access something in a dictionary you use square brackets like in a list
# if you put something that does not exist in the dictionary you will get an error
print(customer['name'])
# also it is case sensitive
# to get around this error you can use the get method
# here is the get method

customer1 = {
    'name1': 'John Smith 1',
    'age1': 31,
    'is_verified1': True
}

# here is with the get method. we do not have a key for birthdate
print(customer1.get('birthdate'))
# instead of getting an empty like before we will just get 'None' because there is nothing to get
# this is useful if the data is not yet in the dictionary and you do not want to cause an error
# also you can make is supply a default value if there is not one in the dictionary.
# here is how to supply a default value.

customer2 = {
    'name2': 'John Smith',
    'age2': 32,
    'is_verified2': True
}

# now you will see instead pf getting none we get the default value
print(customer2.get('birthdate', 'Sep 22 2007'))

# You can also change the value in a dictionary
# here is how to change the value in a dictionary

customer3 = {
    'name3': 'John Smith',
    'age3': 33,
    'is_verified3': True
}

print('BEFORE CHANGE:', customer3['name3'])
# This is how to change the value in a dictionary. Its like changing a variable
customer3['name3'] = 'Jack Smith'
print('AFTER CHANGE:', customer3['name3'])

# you can also create new values in a dictionary
# here is how to create new values in a dictionary

customer4 = {
    'name4': 'John Smith',
    'age4': 34,
    'is_verified4': True
}

# i am using get so it does not error
print('BEFORE CREATING', customer4.get('birthdate'))
# making the new value in the dictionary. similar to making a variable
customer4['birthdate'] = 'sept 22 2007'
print('AFTER CREATING:', customer4.get('birthdate'))

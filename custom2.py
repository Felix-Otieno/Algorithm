def custom_sort(dictionaries, sort_key):
    """
    A function that sorts a list of dictionaries based on a specified key.
    The function takes two parameters: dictionaries, the list of dictionaries to be sorted.
                                       sort_key, the key within each dictionary that will be used as sort base criteria
    
    """
    def get_sort_value(dictionary): # Inner function that takes a single dictionary as parameter 
        return dictionary[sort_key] # Return the value similar to the specified sorted key in the dictionary
    
    # Extracts the value that will be used for sorting each dictionary.
    # Pass the get_sort_value function as the key argument.
    # The sorted() function internally calls the get_sort_value function for each dictionary in the dictionaries list to obtain the sorting value.
    # The sorted() function returns a new sorted list dictionaries based on the extracted sorting values.
    return sorted(dictionaries, key=get_sort_value) 


# List of the dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 35}
        ]
# Display the output of the sorted list dictionaries based on the "name" key.
print(custom_sort(people, "name")) 
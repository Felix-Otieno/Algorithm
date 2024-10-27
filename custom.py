def custom_sort(dictionaries, sort_key):
    return sorted(dictionaries, key = lambda x: x[sort_key])

# Example list of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 35}
]

# Sort the list of dictionaries based on the "age" key
sorted_people = custom_sort(people, "age")
print(sorted_people)
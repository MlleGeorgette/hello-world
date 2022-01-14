"""
We can sort data based on the built-in sort method. However, sometimes, this doesn't work for some data types.
For instance, you can't 'sort' a tuple because tuples are immutable data structures
However, the 'sorted' method can be used for tuples, lists, strings and other iterable objects

Source: https://www.youtube.com/watch?v=QtwhlHP_tqc
"""
# Here's a list of footballers
footballers = ["Ronaldo", "Martial", "Greenwood", "Wan Bissaka", "De Gea"]

# To sort alphabetically
footballers.sort()
print(footballers)

# To sort in reverse alphabetical order
footballers.sort(reverse=True)
print(footballers)

# "Sort" does not work for tuples so we use "sorted" method instead
legends = ("Cantona", "Rooney", "Best", "Law", "Charlton")
sorted_legends = sorted(legends)
print(legends)
print(sorted_legends)

# The output is a list even though the input was a tuple
print(type(legends))
print(type(sorted_legends))

# Sorted can be used for other types of iterable data
print(sorted("Georgette"))
print(sorted((5, 27, 2, 7, 15)))
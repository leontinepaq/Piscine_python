ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# lists are mutable: assign a value at a given index
ft_list[1] = "World!"

# tuples are immutable: create a new one
ft_tuple = ("Hello", "France!")

# sets are mutable but undordered: add and remove elements but no guarantee on the order of the result
ft_set.discard("tutu!")
ft_set.add("Paris!")
assert ft_set == {"Hello", "Paris!"} #check that the set is the same as the one required by the subject

# dictionaries are mutable: assign a new value to a key
ft_dict["Hello"] = "42Paris"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
def greet(person, greeting='Hi'):
    print(f"{greeting} {person}!")


# the results are the saem 
# theas are three different ways to call the fkt <greet> 
# if arguments of the fkt are given with the name of the var than the order of the argumants dosent matter 
#greet("Peter", "Hi")
#greet(person="Peter", greeting="Hi")
#greet(greeting="Hi", person="Peter")


def add_item(item, items=[]):
   items.append(item)
   return items

print(add_item("apple"))
# a new empty list is given to the fkt 
print(add_item("banana", []))
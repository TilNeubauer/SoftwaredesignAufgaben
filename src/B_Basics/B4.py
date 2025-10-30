import copy

list1 = [[1, 2, 3], [4, 5, 6], ["a", "b", "c"], 2]
list2 = list1 # no copy, the two names point to the same objects 
list3 = copy.copy(list1) # only the outer list is copied, inner objects are shared (not copied)
list4 = copy.deepcopy(list1) # a new list with copys of all layers 

print("List # \tID\tEntries")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)

list1[3] = -2

print("List # \tID\tEntries")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)

list2[2][2] = 9

print("List # \tID\tEntries")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)

list1.append([0, 8, 15])

print("List # \tID\tEntries")
print("1\t", id(list1), "\t", list1)
print("2\t", id(list2), "\t", list2)
print("3\t", id(list3), "\t", list3)
print("4\t", id(list4), "\t", list4)
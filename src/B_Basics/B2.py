list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]


list_zip = []

for e1, e2 in zip(list1, list2):
    list_zip.append(e1)
    list_zip.append(e2)

print(list_zip)



list_odd = []

for e in list1:
    if e %2 != 0:
        list_odd.append(e)

for e in list2:
    if e %2 != 0:
        list_odd.append(e)

print(list_odd)


list_zip_reverse = []

if len(list1) != len(list2):
    print("ERROR: list1 & list2 not the same len")
else:    
    for i in range(len(list1)):
        list_zip_reverse.append(list1[len(list1)-1-i])
        list_zip_reverse.append(list2[len(list2)-1-i])

print(list_zip_reverse)
# tuples

intTuple = (1,2,34,5,5)
stringTuple = ("home", "nuber","agoo")
itemTuple = ("home", 5,67)
# print(itemTuple)
# print(len(stringTuple))
# print("max of string tuple:", max(stringTuple))
# print("min of string tuple:", min(intTuple))
# print("index of element 5:", itemTuple.index(5))
# arrays

list = ["eggs","flower","maize","butter",1]
# print(list)
# print(list[0])
list[0] = "nice"
# print(list[0])
# appending

list.append("Ago")
# print(list)

# insert
list.insert(4, "Books")
# print(list)

# delete
list.remove("Ago")
# print(list)

# del list[1:5]

# print(list)


# print("length of the list:", len(list))
# print("max of the list:", max(list))
# print("min of the list:", min(list))

list2 = ["shoes","clothes","stool","machines"]

masterList = [list,list2]
masterList = list + list2
# print(masterList)
# print(masterList[0][3])

# dictionary
listOfStudents = {
    0: "john Doe",
    1: "jane Doe",
    2: "will Smith",
    3: "Tom Williams"
}

print(listOfStudents[0])
print(listOfStudents.keys())
print(listOfStudents.values())
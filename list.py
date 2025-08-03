fruits = ["apple", "banana", "cherry","banana"]
print(fruits)
# print(type(fruits))
# print(len(fruits))
# if "banana"  in fruits:
#     print("Yes, 'banana' is in the fruits list")
# if"kiwi" not in fruits:
#     print("No, 'kiwi' is not in the fruits list")


# print(fruits[1]) # Accessing the first element
# print(fruits[-3])# Accessing the last element
# print(fruits[1:3]) # Slicing the list
# print(fruits[-3:-1]) # Slicing from index 1 to the end

# fruits.append("kiwi")  # Adding an element to the end
# print(fruits)

# fruits.insert(2, "kiwi")  # Inserting an element at index 1
# print(fruits)

# more_fruits=["kiwi", "orange"]
# fruits.extend(more_fruits)  # Extending the list with another list
# print(fruits)

# fruits.remove("banana")  # Removing an element
# print(fruits)

# fruits.pop(1)
# print(fruits)  # Removing the first element

# fruits[1] = "kiwi"  # Changing the second element
# print(fruits)

# fruits[1:3] = ["litchu"]  # Changing a slice of the list
# print(fruits)

# fruits.sort()  # Sorting the list
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)  # Sorting the list in reverse order

# new_fruits=[fruits for fruits in fruits if "a" in fruits]
# print(new_fruits)  # List comprehension to filter fruits containing 'a'

# new_fruits = fruits.copy()  # Creating a copy of the list
# print(new_fruits)  # Displaying the copied list

# new_fruits =fruits+new_fruits  # Concatenating two lists
# print(new_fruits)  # Displaying the concatenated list

# fruits.insert(2,["kiwi", "orange"])  # Finding the index of an element
# print(fruits)  # Displaying the list after finding index
# print(fruits[2][0])
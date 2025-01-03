# # append is add item to the last in arr
# count is Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# cars = ["Food" , "Volvo" , "JoJo"]
# cars.append("Honda")
# cars.pop(0)
# cars.remove("Food")
# print(cars)

# fruits = ['apple', 'banana', 'cherry','cherry','cherry']
# x = fruits.count("cherry")
# print(f"Cherry has {x} in array list")

# arr1 = ['apple', 'banana', 'cherry']
# arr2 = ['Ford', 'BMW', 'Volvo']
# arr1.extend(arr2)
# print(arr1)


# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)

# myArray = ["apple","bean","tomato"]
# myArray.insert(2,"Coconut")
# print(myArray)

# myArray = ["apple","bean","tomato"]
# myArray.reverse()
# print(myArray)

# arrList = [1,3,4,2,5,3]
# arrList = ["B","A","E","D","C","F"]
# arrList.sort()
# print(arrList)

person = [
    {"id" : 1, "Name": "Yo Shi"},
    {"id" : 2, "Name": "Ii Nam"},
    {"id" : 3, "Name": "Gi Hun"},
]
def myFuc(e):
    return e['id']
person.sort(key= myFuc ,reverse=True)
print(person)

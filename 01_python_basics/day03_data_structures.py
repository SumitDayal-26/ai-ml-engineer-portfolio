# Day 3: Data Structures in Python

#1. Lists
numbers =[ 10,20,30,40,50]
print("List:", numbers)
#accessing an element from the List
print ("First element:", numbers[0])
#Adding an element to the end of the list
numbers.append(60)
print("New List:", numbers)
#Loop through List
print("Looping through List:")
for num in numbers:
    print(num)

#2.Tuples
student =("Sumit", 20, "AI/ML")
print("\nTuple:", student)
#accessing an element from Tuple
print("Name:", student[0])

#3. Dictionaries
student_info = {
    "name":"Sumit",
    "age": 20,
    "branch": "AI/ML"
}
print ("\n Dictionary:", student_info)
# accessing an element from Dictionary
print("student name:", student_info["name"])
#Loop through Dictionary
print("\n dictionary items:")
for key,value in student_info.items():
    print(key, ";", value)
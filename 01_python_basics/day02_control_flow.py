# Day 2: Control Flow in Python

# 1. if-else condition
age = int(input("enter age:"))
if age>= 18:
 print("you are eligible to Vote")
else:
 print("you are not eligible to vote")

 #2. if-elif-else condition
marks=int(input("enter your marks:"))
if marks>=90:
  print("Grade A")
elif marks>=80:
  print("Grade B")
elif marks>=70:
  print("Grade c")
else:
  print("grade D")   

#3. for loop example(printing numbers from 1 to 5)
for i in range(1,6):
 print(i)

#4. while loop example(printing numbers from 1 to 5)
count = 1
while count <=5:
 print(count)
 count+=1 


#ex1 
students = ['John',"Michael"]
print(students[1])
print(students[-1])

#ex2
foods = ('Fries',"Burger")
for food in foods:
  print(food + " is a good food")

#ex3
for i in range(1,3):
  print(foods[-i])

#ex4
home_town = {
"city":"Arcadia",
"state":"California",
"population":"58000"}
print("I was born in " + home_town["city"] + "," + home_town["state"] + " - population of " + home_town["population"])

#ex5
for item in home_town:
  print(item + " = " + home_town[item])

#ex6
cohort = []
# for i, student in enumerate(students):
for student in students:
  cohort.append( {'student': student, 'fav_food' : foods[students.index(student)]})
for student in cohort:
  print(student)

#ex7
awesome_students = [(student + " is awesome!") for student in students]
for awesome_student in awesome_students:
  print(awesome_student)

#ex8
print("ex8")
foods_with_a = [food for food in foods if "a" in food]
for food_with_a in foods_with_a:
  print(food_with_a)
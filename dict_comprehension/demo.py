sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
student = {
    "angela":20,
    "kabir":90,
    "Mohammed":100,
    "amina": 40
}

# Don't change code above 👆
# for (key, value) in student.items():
#     print(key, value)
# Write your code below:
new_student_list = {name:scores for (name,scores) in student.items()}
print(new_student_list)

new = {word:len(word) for(word) in sentence.split()}
print(new)
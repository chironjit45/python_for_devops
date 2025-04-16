# Variable declaration and initialization
name = "Alice"          # string
age = 25                # integer
height = 5.6            # float
is_student = True       # boolean

# Display values and types
print("---- Variable Info ----")
print(f"name: {name} (type: {type(name)})")
print(f"age: {age} (type: {type(age)})")
print(f"height: {height} (type: {type(height)})")
print(f"is_student: {is_student} (type: {type(is_student)})")

# Reassign values
name = "Bob"
age = age + 1           # update age
height = height - 0.1   # update height
is_student = False      # change boolean value

# Display updated values
print("\n---- Updated Variable Info ----")
print(f"name: {name}")
print(f"age: {age}")
print(f"height: {height}")
print(f"is_student: {is_student}")

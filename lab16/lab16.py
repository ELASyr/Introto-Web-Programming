# Lab 16
# JSON Module in Python

import json

print("=== 1) Converting Python Objects to JSON (Serialization) ===")
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

print("\n=== 2) Writing JSON to a File ===")
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON written to data.json")

print("\n=== 3) Reading JSON from a File ===")
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)

print("\n=== 4) Converting JSON String to Python Object (Deserialization) ===")
json_text = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_text)

print(data["name"])
print("Type:", type(data))

print("\n=== 5) Working with Lists in JSON ===")
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

json_string = json.dumps(users, indent=4)
print(json_string)

print("\n=== 6) Writing a List of Dictionaries to a File ===")
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("Users written to users.json")

print("\n=== 7) Handling JSON Errors ===")
invalid_json = '{"name": "Alice", "age": 25, "city": "New York"'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Error loading JSON: {e}")

# ---------------- Lab Exercises ----------------

print("\n=== Lab Exercise 1 ===")
student_info = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "courses": ["Database", "OOP", "DSA"]
}

json_string = json.dumps(student_info, indent=4)
print(json_string)

print("\n=== Lab Exercise 2 ===")
student_json = '''{
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "courses": ["Database", "OOP", "DSA"]
}'''

student_data = json.loads(student_json)
print(student_data)

print("\n=== Lab Exercise 3 ===")
filename = "student.json"

with open(filename, "w") as f:
    json.dump(student_info, f, indent=4)

print(f"Data written to {filename}")

with open(filename, "r") as f:
    data_loaded = json.load(f)

print("Loaded data:", data_loaded)

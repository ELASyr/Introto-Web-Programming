# Lab 15
# File Handling in Python

import csv

print("=== 1) Writing to a File ===")
with open("example.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python makes handling easier\n")

print("\n=== 2) Reading from a File ===")
with open("example.txt", "r") as f:
    contents = f.read()
    print(contents)

print("\n=== 3) Reading Files Line by Line ===")
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

print("\n=== 4) Appending Data to a File ===")
with open("example.txt", "a") as f:
    f.write("\nThis line was added later.")

print("\n=== 5) Checking if a File Exists Before Writing ===")
try:
    with open("example.txt", "x") as f:
        f.write("This file was created.")
except FileExistsError:
    print("File already exists")

print("\n=== 6) Processing Text Files ===")
with open("example.txt", "r") as f:
    for line in f:
        print(f"Processed line: {line.strip()}")

print("\n=== 7) Writing Data to a CSV File ===")
data = [
    ["Name", "Age", "City"],
    ["Alice", "32", "New York"],
    ["Bob", "34", "New York"],
    ["Luc", "21", "Washington"]
]

with open("example.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV file written.")

print("\n=== 8) Reading Data from a CSV File ===")
with open("example.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("\n=== 9) Reading CSV with Column Headers ===")
with open("example.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}")

print("\n=== 10) Appending Data to a CSV File ===")
new_data = [["David", "28", "San Francisco"]]

with open("example.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(new_data)

print("New row appended to CSV.")

# ---------------- Lab Exercises ----------------

print("\n=== Lab Exercise 1: Basic Text File Operations ===")
filename = "sample_text.txt"

content = """Hello, world!
This is a sample text file.
It contains multiple lines of text for testing file operations."""

with open(filename, "w") as file:
    file.write(content)

print(f"Content has been written to {filename}")

with open(filename, "r") as file:
    read_content = file.read()

print("Content read from the file:")
print(read_content)

print("\n=== Lab Exercise 2: Processing CSV Files ===")
csv_filename = "people.csv"

data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Data has been written to {csv_filename}")

print("Reading data from the CSV file:")
with open(csv_filename, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print("\n=== Lab Exercise 3: Appending Data to an Existing File ===")
additional_text = "\nThis line is appended to the file."

with open(filename, "a") as file:
    file.write(additional_text)

print(f"Additional text has been appended to {filename}")

with open(filename, "r") as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)

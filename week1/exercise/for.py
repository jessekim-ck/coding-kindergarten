students = {
  "Jesse": 100,
  "Bob": 80,
  "John": 77,
  "Sonia": 63,
  "Alex": 0,
}

for student in students:
    # student = "Jesse"
    score = students[student] # score = students["Jesse"]

    if score >= 90:
        print(f"{student} is A")
    elif score >= 80:
        print(f"{student} is B")
    # ...
    else:
        print(f"{student} is F")

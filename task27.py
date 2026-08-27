person = ("Rahul", 25, 5.9)
print(person[1])


try:
    person[0] = "Joe"
except Exception as e:
    print(print(f"Error {e} - Tuples are immutable."))
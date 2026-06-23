# Append a new line to notes.txt.
with open("notes.txt", "a") as file:
    file.write("Appended line")
print("Data Appended")
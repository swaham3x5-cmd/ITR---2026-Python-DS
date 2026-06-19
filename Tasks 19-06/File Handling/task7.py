# Print line numbers with each line, like:
   # 1: Hello Python
   # 2: Appended line
with open("notes.txt", "r") as file: 
    lines = file.readlines()
for i, line in enumerate(lines, 1): 
    print(f"{i}: {line.strip()}")
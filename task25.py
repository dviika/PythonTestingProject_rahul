line_count = 0
with open('testFile.txt', 'r') as file:
    for line in file:
        line_count = line_count + 1  # OR line_count += 1
print(f"Total lines: {line_count}")
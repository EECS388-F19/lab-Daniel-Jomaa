students = ["Charlie", "Jenny", "Kanu"]
students.sort()
longest_name = students[0]
longest_size = len(students[0])
for name in students:
    first_name = name[:-1]
    print(first_name)
    if len(name) > longest_size:
        longest_name = name

print(longest_name)


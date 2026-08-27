#file close already in this mode
# r read mode, w - write to file
#Task read the file and store all lines in the list, reverse the list
#write the list back to the file
with open ('testFile.txt', 'r') as reader:
    content = reader.readlines()
    reversed_list = []
    # Start at the last index (len(my_list) - 1), stop before index -1 (which includes 0), step by -1
    for i in range(len(content) - 1, -1, -1):
        reversed_list.append(content[i])
    with open('testFile.txt', 'w') as writer:
        writer.writelines(reversed_list)

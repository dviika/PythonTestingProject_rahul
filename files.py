file = open('testFile.txt')
#read all the contents of the file
print(file.read())

#read first 2 letters/bits by passing a parameteres
#print(file.read(3))

#read first line(row)
#print(file.readline())

#print line(row) by line with an empty line separation in console using readline method and while
# line = file.readline()
# while line !='':
#     print(line)
#     line = file.readline()

#will read and store lines in the list -> list [apple\n,banana\n, cinema\n,dream\n,elefant\n,friend]
# list = file.readlines()
# print(list[2])

# for line in file.readlines():
#     print(line[-1])

file.close()
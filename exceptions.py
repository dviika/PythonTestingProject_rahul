ItemsInCart = 0
#2 items will be added to the cart

if ItemsInCart !=2: #raise Exception products count doesn't match
    pass

assert(ItemsInCart == 0) # only pass when cond = True otherwise fails

#try, except
try:
    with open('testFile1.txt', 'r') as file:
        file.readline()

except:
    print('File not found')

#try, except with python error msg
try:
    with open('testFile2.txt', 'r') as file:
        file.readline()

except Exception as e:
    print(e)

finally: #will be executed if try and except pass
    print('Finally block is working')
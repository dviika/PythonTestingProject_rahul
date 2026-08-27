# list = [1, 4, 7, 10]
#
# for i in list:
#     print(i * 3)

user_input = int(input('Please enter a number: '))
if 5 <= user_input <= 11:
    print('Good Morning')
elif 12 <= user_input <= 17:
    print('Good Afternoon')
elif  18 <= user_input <= 21:
    print('Good Evening')
else:
     print('Good Night')
print('Greeting code has completed.')

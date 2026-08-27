sentence = "Sashko.Malynychenko.com"
experience = 6
str0= 'Sashko'
str1='malyn'

print(sentence[0:6])
print(sentence[-1])

splited_sentence = sentence.split(".")
print(splited_sentence)
print(splited_sentence[0])

name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")
# Output: Name: Alice, Age: 22

print(f"{sentence} has professional experience = {experience}")
#format() syntax
print("{} has professional experience = {}".format(sentence, experience))

print(str0 in sentence)  #otput True
print(str1 in sentence) # outpu flase ( case sensitive)

#remove space
str2 = ' Congratulations'
print(str2.strip)

data = [
    'Натрій (Sodium)',
    'Референтний діапазон: 135–145 ммоль/л',
    'Калій (Potassium)',
    'Референтний діапазон: 3,5–5,2 ммоль/л',
    'Хлориди (Chloride)',
    'Референтний діапазон: 98–111 ммоль/л',
    'Бікарбонат (Bicarbonate)',
    'Референтний діапазон: 20–29 ммоль/л',
    'Аніонна різниця (Anion Gap)',
    'Референтний діапазон: 5–17 ммоль/л',
    'Глюкоза (Glucose)',
    'Референтний діапазон: 70–99 мг/дл',
    'Азот сечовини крові (Blood Urea Nitrogen, BUN)',
    'Референтний діапазон: 7–25 мг/дл',
    'Креатинін (Creatinine)',
    'Референтний діапазон: 0,50–1,10 мг/дл',
    'Кальцій (Calcium)',
    'Референтний діапазон: 8,5–10,5 мг/дл',
    'Загальний білок (Total Protein)',
    'Референтний діапазон: 6,4–8,3 г/дл',
    'Альбумін (Albumin)',
    'Референтний діапазон: 3,5–5,1 г/дл',
    'Глобуліни (Globulin)',
    'Референтний діапазон: 2,2–4,0 г/дл',
    'Співвідношення альбумін/глобулін (A/G Ratio)',
    'test',
    'Загальний білірубін (Total Bilirubin)',
    'Референтний діапазон: 0,3–1,2 мг/дл',
    'Лужна фосфатаза (Alkaline Phosphatase)',
    'Референтний діапазон: 33–120 Од/л',
    'Аланінамінотрансфераза (Alanine Aminotransferase, ALT)',
    'Референтний діапазон: 8–37 Од/л',
    'Аспартатамінотрансфераза (Aspartate Aminotransferase, AST)',
    'Референтний діапазон: < 35 Од/л',
    'Розрахункова швидкість клубочкової фільтрації (eGFR)',
    'Референтне значення: > 60 мл/хв/1,73 м²']

# list_1 = []
# for i in data[::2]:
#     list_1.append(i)
#
# print(list_1)
#
# result = {}
#
# for item in data:
#     key, _, rest = item.partition(' (')
#     value = rest.rstrip(')')
#
#     if rest:  # only add if parentheses exist
#         result[key] = value
#
# print(result)
#
#
#
# for key in result:
#     print(key)
#
# for value in result.values():
#     print(value)
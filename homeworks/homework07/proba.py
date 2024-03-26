stroka = 'ПАра-ра-рам рам-пам-папАМ па-ра-пИ-дам'
VOWELS = 'аеёиоуэюяы'


stroka_vowels = "".join([char for char in stroka.lower() if char in VOWELS or char == ' '])
if len(stroka_vowels) <= 1:
    print("Количество фраз должно быть больше одной!")
else:
    result = [len(word) for word in stroka_vowels]
    print("Парам пам-пам") if len(set(result)) == 1 else print("Пам парам")

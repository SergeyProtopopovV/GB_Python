# Пользователь вводит текст(строка). Словом считается последовательность не пробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

input_text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

separated_text = input_text.lower().split()

word_count = {}
for word in separated_text:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(len(word_count))

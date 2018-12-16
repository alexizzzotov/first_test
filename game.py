from random import *
words = ('апельсин','мандарин','яблоко', 'банан','грейпфрукт','виноград','клубника','черешня','абрикос','смородина')
word = choice(words)
correct = word

jumble = ''
while word:
    posit = randrange(len(word))
    jumble += word[posit]
    word = word[:posit] + word[posit+1:]

print('Добро пожаловать в игру Анаграмма! Переставьте буквы так, чтобы получилось слово (для завершения нажмите Enter)')
print('Вот анаграмма:',jumble)
guess = input('Попробуйте отгадать исходное слово:')
while guess !=correct and guess !='':
    print('Попробуйте еще раз')
    guess = input('Попробуйте отгадать исходное слово:')
if guess == correct:
    print('Поздравляю! Вы правильно угадали слово')

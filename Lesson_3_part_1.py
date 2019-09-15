import random
number = random.randint(1, 100)
print('Это число ', number, '?')
start = 1
end = 100
user_input_char = int(input('Выберите ответ: 1. Больше загаданного 2. Меньше загаданного 3. Бинго! '))
while user_input_char != 3:
    if user_input_char == 2:
        start = number + 1
        number = random.randint(start, end)
        print('Ваше число ', number, '?')
        user_input_char = int(input('Выберите ответ: 1. Больше 2. Меньше 3. Бинго!'))
    elif user_input_char == 1:
        end = number - 1
        number = random.randint(start, end)
        print('Ваше число ', number, '?')
        user_input_char = int(input('Выберите ответ: 1. Больше 2. Меньше 3. Бинго!'))
print('Искусственный интеллект умнее всех!')

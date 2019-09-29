class Word:
    text = "None"
    part = "Сущ"

    def __init__(self, text, part):
        self.text = text
        self.part = part


class Sentence:
    content = [0, 4, 2]

    def __init__(self, content):
        self.content = content

    def show(self, self_words):
        text = ''
        content = self.content
        for i in content:
            text += self_words[i].text + " "
        print(text)

    def show_parts(self, self_words):
        content_grammar = []
        content = self.content
        for i in content:
            if self_words[i].part not in content_grammar:
                content_grammar.append(self_words[i].part)
        print(content_grammar)


# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
# Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное),
# а для Verb — «гл» (сокращение от глагол). Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.


class Noun(Word):
    text = 'none'
    __grammar = 'сущ'

    def __init__(self, text):
        self.text = text
        self.part()
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.

    def part(self):
        self.part = 'существительное'


class Verb(Word):
    text = 'none'
    __grammar = 'гл'

    def __init__(self, text):
        self.text = text
        self.part()
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.

    def part(self):
        self.part = 'глагол'


big_word = Noun("сосной")
word_1 = Noun("собака")
word_2 = Verb("ела")
word_3 = Noun("колбасу")
word_4 = Word("вечером", "наречие")
word_5 = Word("под", "предлог")
words = [word_1, word_2, word_3, word_4, word_5, big_word]

words_2 = [Noun("собака"), Verb("ела"), Noun("колбасу"), Noun("кот"), Word("тихой", "прилагательное"), Word("ночью", "существительное")]

# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
test = Sentence([1, 2, 0, 3, 4, 5])
test.show(words)
test.show_parts(words)
test.show(words_2)
test.show_parts(words_2)

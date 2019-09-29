# 1. Создайте класс Word. (Вспомните, какое зарезервированное слово используется для создания класса).
# 2. Добавьте свойства text (класс будет хранить слово) и part (часть речи, которой является слово.
# Например, существительное, прилагательное и т.п.). Для добавления свойств воспользуйтесь методом __init__.


class Word:
    text = "None"
    part = "Сущ"

    def __init__(self, text, part):
        self.text = text
        self.part = part

# 4. Создайте класс Sentence. (по аналогии с п. 1).
# 5. Добавьте свойство content. (по аналогии с п. 2).
# 7. Добавьте в класс Sentence метод show, составляющий предложение. Метод должен перебирать числа из свойства content и
# подставлять соответствующие слова, которые хранятся в свойстве text экземпляров класса Word. Данные извлекаем из
# списка words, который получили на прошлом шаге. При соединении слов в предложение не забудьте добавить пробел между
# словами.
# 8. Добавьте в класс Sentence метод show_parts, отображающий, какие части речи входят в предложение. По
# аналогии с п. 7 перебирайте в цикле числа из свойства content и сохраняйте результат в отдельный список. Учтите,
# что части речи могут повторяться, но список не должен содержать дубликаты.


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
        content_part = []
        content = self.content
        for i in content:
            if self_words[i].part not in content_part:
                content_part.append(self_words[i].part)
        print(content_part)

# 3. Создайте экземпляр класса Word, передав в качестве параметров любое слово и указав его часть речи.


big_word = Word("сосной", "сущ")


# 6. Создайте из массива (можете взять приведённый выше или придумать свой) список, каждый элемент которого является
# экземпляром класса Word. Примечание: список list (назовём его words) — отдельная переменная, не относящаяся к
# классам Word и Sentence.

word_1 = Word("собака", "сущ")
word_2 = Word("ела", "глагол")
word_3 = Word("колбасу", "сущ")
word_4 = Word("вечером", "наречие")
word_5 = Word("под", "предлог")
words = [word_1, word_2, word_3, word_4, word_5, big_word]

test = Sentence([1, 2, 4, 5])
test.show(words)
test.show_parts(words)


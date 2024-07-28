from random import choice


class Hangman:
    __stages = ['  ---  ',
                ' |   | ',
                '  ===  ',
                ' \\ | / ',
                '   |   ',
                '  / \\  ']

    def __init__(self, word):
        self.word = word
        self.right_symbols = []
        self.res_list = []
        self.res_str = '_' * len(self.word)
        self.attempts = len(self.__stages)
        self.count = 0

    def __draw_hangman(self, attempts):
        for i in range(6 - attempts):
            print(self.__stages[i])
        print()

    @staticmethod
    def __is_valid_input(ch):
        if len(ch) == 1 and ch.isalpha():
            return True
        return False

    def play(self):

        while self.word != self.res_str and self.attempts > 0:
            ch = input('Буква: ')
            if self.__is_valid_input(ch):
                if not ch in self.word:
                    print('Неправильно')
                    self.count += 1
                    self.attempts -= 1
                    self.__draw_hangman(self.attempts)
                    print('Слово: ')
                    print(self.res_str)
                else:
                    print('Правильно')
                    self.right_symbols.append(ch)
                    self.res_list = list(map(lambda x: '_' if x not in self.right_symbols else x, self.word))
                    self.res_str = "".join(self.res_list)
                    self.__draw_hangman(self.attempts)
                    print('Слово: ')
                    print(self.res_str)
                print()
            else:
                print('Нужно ввести одну букву')

        if self.attempts == 0:
            print(f"Вы проиграли. Правильное слово было: {self.word}")
        if self.word == self.res_str:
            print("Вы выиграли")


with open('words.txt', 'r', encoding='utf-8') as file1:
    list1 = [i.strip() for i in file1.readlines()]
    word = choice(list1)

hangman = Hangman(word)
hangman.play()
hangman1 = Hangman(word)
hangman1.play()

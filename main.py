from random import choice


def draw_hangman(attempts):
    stages = [[' ', ' _', '_', '_ ', ' '],
              [' ', '| ', ' ', ' |', ' '],
              [' ', ' ^', '^', '^ ', ' '],
              [' ', '\\', ' |', " /", ' '],
              [' ', ' ', ' |', '  ', ' '],
              [' ', '/', '  ', ' \\', ' ']]

    for i in range(6 - attempts):
        print(''.join(stages[i]))
    print()


def get_word():
    with open('words.txt', 'r', encoding='utf-8') as file1:
        list1 = [i.strip() for i in file1.readlines()]
        return choice(list1)


def validate_input(ch):
    if len(ch) == 1 and ch.isalpha():
        return True
    return False


def hangman():
    word = get_word()
    right_symbols = []
    res_str = '_' * len(word)
    attempts = 6
    count = 0
    while word != res_str and attempts > 0:
        ch = input('Буква: ')
        if validate_input(ch):
            if not ch in word:
                print('Неправильно')
                count += 1
                attempts -= 1
                draw_hangman(attempts)
                print('Слово: ')
                print(res_str)
            else:
                print('Правильно')
                right_symbols.append(ch)
                res_list = list(map(lambda x: '_' if x not in right_symbols else x, word))
                res_str = "".join(res_list)
                draw_hangman(attempts)
                print('Слово: ')
                print(res_str)
            print()
        else:
            print('Нужно ввести одну букву')


hangman()

##########################################################
#### Функция для корректировки неправильной раскладки ####

#### Утилитарный словарь в глобальной переменной
LAYOUT = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                           "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))

def turn_layout(word):
    return word.translate(LAYOUT)

if __name__ == "__main__":
    word = "ghbdtn!"
    correct_word = turn_layout(word)
    print(correct_word)
    
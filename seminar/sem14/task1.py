# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
from string import ascii_letters

def del_symbol(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()

#    2 вариант
# def del_symbol(text: str) -> str:
#     new_text = ''
#     for char in text.lower():
#         if char in ascii_letters:
#             new_text += char
#         elif char == ' ':
#             new_text += char
#     return new_text

if __name__ == '__main__':
    print(del_symbol('ytЫЫАytrd 44545RDGS'))

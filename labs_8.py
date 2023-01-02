"""Algorithmic simulator."""
# # 1.
# choice = 'y'.lower()
# if choice.lower():
#     pass
#
# # 2.
# my_string = 'a b c d e f g'
# space_count = 0
# for ch in my_string:
#     if ch == ' ':
#         space_count += 1
#
# # 3.
# my_string = '123adsac'
# digit_count = 0
# for ch in my_string:
#     if ch.isdigit():
#         digit_count += 1
#
# # 4.
# my_string = 'ABC DFG adwqtk lasah'
# up_count = 0
# for ch in my_string:
#     if ch.isupper():
#         up_count += 1

# 5.
# my_string = 'www.Blacklight911.com'
#
# def com_chk(any_str):
#     return False if any_str[-4:].find('.com') == -1 else True

# 6.
# my_string = 'in this string "t" will be replaced by "T".'
# my_string = my_string.replace('t', 'T')

# 7.
# my_string = 'This text will be reversed'
#
# def reverse_string(text):
#      return text[::-1]

# # 8.
# my_string = 'This is simply string.'
# print(my_string[:3])
#
# # 9.
# my_string = 'This is simply string.'
# print(my_string[-3:])
#
# # 10.
# my_string = 'pies>milk>cocking>apple pie>ice cream'
# new_my_string = my_string.split('>')
# print(new_my_string)

"""Programming exercises."""


# Initials.
def initials():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    pat = input('Enter your patronymic: ')

    print(f'{first_name[0]}.{pat[0]}.{last_name[0]}')


# Sum of digits in a string.
def sum_of_digits_in_string():
    str_numbers = input('Enter a series of single-digit '
                       'numbers without separators: ')
    total = 0

    for ch in str_numbers:
        total += int(ch)

    print('Sum of digits per line:', total)


# Date printer.
def date_printer():
    usr_input = input('Enter date in the format xx/xx/xxxx: ')
    date_list = usr_input.split('/')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
              'Sep', 'Okt', 'Nov', 'Dec']
    print(f'Date: {date_list[0]} {months[int(date_list[1][1])]} {date_list[2]} year.')


# Morse code converter
def morse_code_converter():
    morse_code = ''
    morse = {' ' : ' ', ',' : '--..--', '.' : '.-.-.-', '?' : '..--..',
             '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--',
             '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...',
             '8' : '---..', '9' : '----.', 'A' : '.-', 'B' : '-...',
             'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.',
             'H' : '....', 'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..',
             'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-',
             'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-',
             'W' : '.--', 'X' : '-..-', 'Y' : '-.-', 'Z' : '--..'}

    print('Morse code converter.')
    usr_input = input('Enter your text: ').upper()

    for ch in usr_input:
        morse_code += morse.get(ch)

    print(morse_code)


# Alphabet translator phone number.
def alphabet_translator_phone_num():
    phn_number = input('Enter phone number in format(***-***-****): ').upper()
    number = ''
    alphabet = {'A' : 2, 'B' : 2, 'C' : 2,
                'D' : 3, 'E' : 3, 'F' : 3,
                'G' : 4, 'H' : 4, 'I' : 4,
                'J' : 5, 'K' : 5, 'L' : 5,
                'M' : 6, 'N' : 6, 'O' : 6,
                'P' : 7, 'Q' : 7, 'R' : 7,
                'S' : 7, 'T' : 8, 'U' : 8,
                'V' : 8, 'W' : 9, 'X' : 9,
                'Y' : 9, 'Z' : 9}


    for ch in phn_number:
        if not ch.isdigit() and ch != '-':
            number += str(alphabet.get(ch))
        else:
            number += ch


    print(number)


# Average word count.
def average_word_count():
    lines_list = []
    words_count = 0

    try:
        with open('Data/text.txt', 'r', encoding='utf-8') as file:
            for line in file:
                lines_list.append(line.rstrip('\n'))


        file.close()

        for line in lines_list:
            words_count += line.count(' ')

        print('Average words:', (words_count + len(lines_list)) // len(lines_list))
    except IOError:
        print('Error file reading.')
    except:
        print('Error.')


# Character analysis.
def character_analysis():
    upper_count = 0
    lower_count = 0
    num_count = 0
    space_count = 0

    with open('Data/text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            for ch in line.rstrip('\n'):
                if ch.isupper():
                    upper_count += 1
                if ch.islower():
                    lower_count += 1
                if ch.isdigit():
                    num_count += 1
                if ch == ' ':
                    space_count += 1

        file.close()

    print(f'Upper characters: {upper_count}')
    print(f'Lower characters: {lower_count}')
    print(f'Number characters: {num_count}')
    print(f'Space characters: {space_count}')


# Sentence Corrector.
def sentence_corrector():
    usr_input = 'hey! my name is joe. and what is your name?'
    # usr_input = input('Enter text: ')

    def string_capitalize(text):
        # text = 'hi! my name is serega. and im not gay im coder?'
        # thislist = text.split()
        # pnkt_list = ["!", "."]
        # a = -1
        # thislist[0] = thislist[0].capitalize()
        # for i in thislist:
        #     # print(i)
        #     a += 1
        #     for j in i:
        #         for g in pnkt_list:
        #             if ord(j) == ord(g):
        #                 print(1)
        #                 thislist[a + 1] = thislist[a + 1].capitalize()
        #                 break
        #
        # print(' '.join(thislist))
        #
        # return thislist
        pnkt_list = ['!', '.', '?']
        list_text = text.split()
        new_text = ''
        tmp_text = ''
        print(list_text)
        i = 0
        while i != len(text):
            if text[i] in pnkt_list and text[i+1] == ' ':
                i += 2
                new_text += text[i].upper()

            else:
                new_text += text[i]
            i += 1
        print(new_text)
        # for word in list_text:
        #     tmp_text += word + ' '
        #     if '!' in tmp_text or '.' in tmp_text or '?' in tmp_text:
        #         new_text += tmp_text.capitalize()
        # Заметка: Создать список позиций знаков препинания в тексте
        # Или создать переменную и переписать весь текст в нее используя знаки.
        # препинания как триггеры подстановки к новую строку.



    print(string_capitalize(usr_input))


# Vowels and consonants.
def vowels_and_consonants():
    usr_input = input('Enter your text: ')


    def vowel_search(txt):
        vowel_list = ['a', 'e', 'u', 'o', 'i']
        count = 0
        for ch in txt:
            if ch.lower() in vowel_list:
                count += 1
        return count

    def consonants_search(txt):
        consonants_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                           'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        count = 0
        for ch in txt:
            if ch.lower() in consonants_list:
                count += 1
        return count

    print('Vowels:', vowel_search(usr_input))
    print('Consonants:', consonants_search(usr_input))


# Most frequent symbol.
def most_frequent_character():
    # usr_input = input('')
    usr_input = input('Enter your text: ')

    def space_remove(text):
        len_text = text.count(' ')
        text = text.replace(' ', '', len_text)
        return text

    def count_symbol(text):
        text = text.lower()
        count_ch = 0
        char = ''
        for ch in text:
            tmp_count_ch = text.count(ch)
            if count_ch < tmp_count_ch:
                char = ch
                count_ch = tmp_count_ch

        if tmp_count_ch > 1:
            return char
        else:
            return None

    if count_symbol(space_remove(usr_input)) is None:
        print('There are no repeating characters in the text')
    else:
        print(f'Symbol: {count_symbol(space_remove(usr_input))}')


# Word separator.
def word_separator():
    usr_input = input('Enter your text: ')
    # usr_input = 'StopAndSmellTheRoses'

    def separate_words(text):
        new_text = ''
        for ch in text:
            if ch.isupper():
                new_text += ' ' + ch
            else:
                new_text += ch
        return new_text.lstrip()

    print(separate_words(usr_input).capitalize())


# Pig Latin.
def pig_latin():
    usr_input = input('Enter your text: ').upper()

    def change_words(text):
        text_list = text.split()
        for i in range(len(text_list)):
            temp_1 = text_list[i][:1]
            text_list[i] = text_list[i][1:] + temp_1
            text_list[i] = text_list[i] + 'AY'

        return ' '.join(text_list)

    print(change_words(usr_input))


# Lottery Powerball
def lottery_powerball():
    numbers_list = []
    with open('Data/pbnumbers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            numbers_list.append(line.rstrip('\n'))

        file.close()

    def counting_numbers(list_numbers):
        counting_dict = {}
        split_numbers = [line.split() for line in list_numbers]

        for l_nums in split_numbers:
            for num in l_nums:
                if int(num) in counting_dict:
                    counting_dict[int(num)] += 1
                else:
                    counting_dict[int(num)] = 1
        return counting_dict

    dict_numbers = sorted(counting_numbers(numbers_list).items())
    print(dict_numbers)



lottery_powerball()


# Gasoline prices.
def gasoline_prices():
    pass


gasoline_prices()
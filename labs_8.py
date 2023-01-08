"""Algorithmic simulator."""
import collections

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
    print(
        f'Date: {date_list[0]} {months[int(date_list[1][1])]} {date_list[2]} year.')


# Morse code converter
def morse_code_converter():
    morse_code = ''
    morse = {' ': ' ', ',': '--..--', '.': '.-.-.-', '?': '..--..',
             '0': '-----', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.', 'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
             'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
             'W': '.--', 'X': '-..-', 'Y': '-.-', 'Z': '--..'}

    print('Morse code converter.')
    usr_input = input('Enter your text: ').upper()

    for ch in usr_input:
        morse_code += morse.get(ch)

    print(morse_code)


# Alphabet translator phone number.
def alphabet_translator_phone_num():
    phn_number = input(
        'Enter phone number in format(***-***-****): ').upper()
    number = ''
    alphabet = {'A': 2, 'B': 2, 'C': 2,
                'D': 3, 'E': 3, 'F': 3,
                'G': 4, 'H': 4, 'I': 4,
                'J': 5, 'K': 5, 'L': 5,
                'M': 6, 'N': 6, 'O': 6,
                'P': 7, 'Q': 7, 'R': 7,
                'S': 7, 'T': 8, 'U': 8,
                'V': 8, 'W': 9, 'X': 9,
                'Y': 9, 'Z': 9}

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

        print('Average words:',
              (words_count + len(lines_list)) // len(lines_list))
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
    usr_input = input('Enter text: ')

    def string_capitalize(text):
        list_text = text.split()
        found_end = False

        for index in range(len(list_text)):
            if found_end or index == 0:
                list_text[index] = list_text[index].capitalize()
                found_end = False

            if list_text[index].endswith(('!', '.', '?')):
                found_end = True
                continue

        return ' '.join(list_text)

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
                           'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                           'z']
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
    LOTTERY_NUMBERS = 69
    PB_NUMBERS = 26
    MAX_VALUE_OVERDUE = 10
    list_numbers = []

    with open('Data/pbnumbers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            list_numbers.append(line.rstrip('\n'))
        file.close()

    def get_all_numbers(list_pb_numbers):
        list_nums = []
        split_list = [w_line.split() for w_line in list_pb_numbers]

        for w_line in split_list:
            for nums in w_line:
                list_nums.append(int(nums))

        return list_nums

    def most_and_least_numbers():
        def get_frequency(num_list, max_value):
            frequency = [0] * (max_value + 1)
            for i in range(len(num_list)):
                num = num_list[i]

                frequency[num] += 1

            return frequency

        def most_common(freq_list):
            common_sorted = []
            tmp_list = []

            def highest_position(num_list):
                high = 0
                highest_pos = 0
                for i in range(len(num_list)):
                    if num_list[i] > high:
                        high = num_list[i]
                        highest_pos = i

                return highest_pos

            for item in range(len(freq_list)):
                tmp_list.append(freq_list[item])

            for item in range(len(tmp_list)):
                position = highest_position(tmp_list)
                common_sorted.append(position)
                tmp_list[position] = -1

            # Remove last pos '0'.
            common_sorted.remove(0)

            return common_sorted

        numbers_list = get_all_numbers(list_numbers)
        freq = get_frequency(numbers_list, LOTTERY_NUMBERS)
        sorted_list_by_most_common = most_common(freq)

        print('Ten most common numbers (descending)')
        print('------------------------------------')
        for i in range(10):
            print(sorted_list_by_most_common[i])

        print()

        sorted_list_by_most_common.reverse()
        print('Ten Least common numbers(ascending).')
        for i in range(10):
            print(sorted_list_by_most_common[i])

    def overdue_numbers():
        def get_last_position(numbers_list, max_number):
            last_position = [0] * (max_number + 1)

            for i in range(len(numbers_list)):
                num = numbers_list[i]

                last_position[num] = i

            return last_position

        def most_overdue(pos_list):
            overdue_sorted = []

            def pos_lowest_last_value(num_list):
                lowest = num_list[1]
                lowest_pos = 1
                for i in range(2, len(num_list)):
                    if num_list[i] < lowest:
                        lowest = num_list[i]
                        lowest_pos = i
                return lowest_pos

            temp_list = []
            for item in pos_list:
                temp_list.append(item)

            max_value = max(temp_list)

            if MAX_VALUE_OVERDUE < len(temp_list):
                num_overdue = MAX_VALUE_OVERDUE
            else:
                num_overdue = len(temp_list)

            for _ in range(num_overdue):
                position = pos_lowest_last_value(temp_list)
                overdue_sorted.append(position)
                temp_list[position] = max_value + 1
            return overdue_sorted

        lotto_numbers = get_all_numbers(list_numbers)
        last_position_list = get_last_position(lotto_numbers, LOTTERY_NUMBERS)
        most_overdue_nums = most_overdue(last_position_list)

        if MAX_VALUE_OVERDUE < len(most_overdue_nums):
            num_overdue = MAX_VALUE_OVERDUE
        else:
            num_overdue = len(most_overdue_nums)

        print('Ten most overdue numbers')
        print('---------------------')
        for i in range(num_overdue):
            print(most_overdue_nums[i])

    def frequency_numbers():
        def get_numbers(list_n):
            lotto_nums = []
            pb_numbers = []
            for i in range(len(list_n)):
                number_set = list_n[i].split()
                for j in range(len(number_set) - 1):
                    lotto_nums.append(int(number_set[j]))
                pb_numbers.append(int(number_set[len(number_set) - 1]))

            pb_lottery = [[], []]
            pb_lottery[0] = lotto_nums
            pb_lottery[1] = pb_numbers

            return pb_lottery

        lottery_list = get_numbers(list_numbers)

        reg_frequency = [0] * (LOTTERY_NUMBERS + 1)
        pb_frequency = [0] * (PB_NUMBERS + 1)

        for i in range(len(lottery_list[0])):
            num = lottery_list[0][i]

            reg_frequency[num] += 1

        for i in range(len(lottery_list[1])):
            num = lottery_list[1][i]

            pb_frequency[num] += 1

        print('Frequency of Regular Numbers')
        print('----------------------------')
        for i in range(1, len(reg_frequency)):
            print(i, 'was chosen', reg_frequency[i], 'times.')

        print()

        print('Lottery number frequency')
        print('------------------------')
        for i in range(1, len(pb_frequency)):
            print(i, 'was chosen', pb_frequency[i], 'times.')

    most_and_least_numbers()
    print()
    overdue_numbers()
    print()
    frequency_numbers()


# Gasoline prices.
def gasoline_prices():
    prices_dict = {}
    with open('Data/GasPrices.txt', 'r', encoding='utf-8') as file:
        for line in file:
            prices_dict.setdefault(line[:10],
                                   float(line[11:].rstrip('\n')))

    def get_years_list(p_dict):
        years = []
        for item in p_dict.keys():
            if int(item[6:]) not in years:
                years.append(int(item[6:]))

        return years

    def get_months_count_list(p_dict):
        months = {}
        for item in p_dict.keys():
            if item[:2] + '-' + item[6:10] in months.keys():
                months[item[:2] + '-' + item[6:10]] += 1
            else:
                months[item[:2] + '-' + item[6:10]] = 1

        return months

    def get_avg_price(years_l):
        avg_prices = {}

        def get_avg_price_per_year(year):
            year_count = 0
            for key, val in prices_dict.items():
                if str(year) in key:
                    year_count += val
            return year_count / 12

        for y in years_l:
            avg_prices[y] = get_avg_price_per_year(y)

        return avg_prices

    def get_avg_prices_per_months(months_count, p_dict):
        avg_per_month = {}
        months_values = list(p_dict.values())

        for key, val in months_count.items():
            sum_nums = 0.0
            for i in reversed(range(val)):
                sum_nums += months_values.pop(i)
            avg_per_month[key] = sum_nums / val

        return avg_per_month

    def highest_and_lowest_prices_per_years(p_dict, years_l):
        high_and_low_year = {}

        def year_slice(prices_d, year):
            year_dict = {}
            for key, value in prices_d.items():
                if str(year) in key:
                    year_dict[key] = value
            return year_dict

        def high_and_low(year_d):
            h_l_year = {}
            lowest_key = ''
            highest_key = ''
            lowest = 0
            highest = 0
            for key, val in year_d.items():
                if lowest == 0 and highest == 0:
                    lowest, highest = val, val
                    lowest_key, highest_key = key, key
                if lowest > val:
                    lowest = val
                    lowest_key = key

                if highest < val:
                    highest = val
                    highest_key = key

            h_l_year[highest_key] = highest
            h_l_year[lowest_key] = lowest
            return h_l_year

        for y in years_l:
            high_and_low_year[y] = high_and_low(year_slice(p_dict, y))

        return high_and_low_year

    def writing_dict_in_file(filename, sortd_dict):
        with open(filename+'.txt', 'w', encoding='utf-8') as file_dict:
            for k, v in sortd_dict.items():
                file_dict.write(f'{str(k)} : {str(v)}\n')

    get_years = get_years_list(prices_dict)
    prices_per_years = get_avg_price(get_years)

    get_months_count = get_months_count_list(prices_dict)
    monthly_avg = get_avg_prices_per_months(get_months_count, prices_dict)

    high_and_low_years_dict = highest_and_lowest_prices_per_years(prices_dict, get_years)

    print('Average price per year')
    print('----------------------')
    for key, value in prices_per_years.items():
        print(f'Year {key}  average gasoline price {value}')
    print()
    print('Average price per month')
    print('-----------------------')
    for key, value in monthly_avg.items():
        print(f'Month {key[:2]} year {key[3:]} average price {value}')

    print()
    print('Highest and lowest Prices per year:')
    print('Date:--------Highest:--Date:-------Lowest:')
    for value in high_and_low_years_dict.values():
        print(value)

    print()

    sorted_d_dict = dict(sorted(prices_dict.items(), key=lambda x: x[1]))
    sorted_a_dict = dict(sorted(prices_dict.items(), key=lambda x: x[1],
                                reverse=True))

    writing_dict_in_file('lowest_to_highest', sorted_d_dict)
    writing_dict_in_file('highest_to_lowest', sorted_a_dict)


gasoline_prices()

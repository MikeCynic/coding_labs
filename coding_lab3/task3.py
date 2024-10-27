# TODO  Напишите функцию count_letters
def count_letters(text):
    dict_count= {}
    for letter in text:
        letter_processed = letter.lower()
        if letter_processed.isalpha():
            if letter_processed in dict_count:
                dict_count[letter_processed] += 1
            else:
                dict_count[letter_processed] = 1
    return dict_count


# TODO Напишите функцию calculate_frequency


def calculate_frequency(dict_original):
    sum_freq = 0
    dict_freq = {}
    for letter in dict_original:
        sum_freq += dict_original[letter]
    for letter in dict_original:
        dict_freq[letter] = dict_original[letter]/sum_freq
    return dict_freq


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
frequency = calculate_frequency(count_letters(main_str))
for letter in frequency:
    print(f'{letter}: {frequency[letter]:.2f}')
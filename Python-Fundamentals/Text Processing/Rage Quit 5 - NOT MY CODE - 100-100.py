sequences = input().upper()
list_unique = ""

for el in sequences:
    if not el.isdigit() and el not in list_unique:
        list_unique += el

last_digit = sequences[-1]
new_sequences = ""
final_list = ""
digit = ""

for i in range(len(sequences)):
    if sequences[i].isdigit():
        if sequences[i] == last_digit and i == len(sequences) - 1:  # проверяваме дали цифрата е последната
            digit += sequences[i]
            final_list += (new_sequences * int(digit))
            break

        if sequences[i + 1].isdigit():   # проверяваме дали следващият индекс е цифра
            if not i + 1 == len(sequences) - 1:   # проверяваме дали следващата цифра не е последна
                digit += sequences[i]
                digit += sequences[i + 1]
            else:                                 # ако е, записваме настоящата цифра
                digit += sequences[i]
                continue
        else:
            digit += sequences[i]
        final_list += (new_sequences * int(digit))
        new_sequences = ""

    else:
        digit = ""
        new_sequences += sequences[i]

print(f"Unique symbols used: {len(list_unique)}")
print(final_list)


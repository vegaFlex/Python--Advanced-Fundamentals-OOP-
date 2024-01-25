english_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# morse_to_english = dict(sorted(english_to_morse.items(), key=lambda x: x[1]))
morse_to_english = dict((v, k) for k, v in english_to_morse.items())

line = input().split('|')

new_string = ""
for characters in line:
    for symb in characters.split():
        if symb in morse_to_english:
            curr_character = morse_to_english[symb]
            new_string += curr_character
    new_string = new_string + ' '

print(new_string)


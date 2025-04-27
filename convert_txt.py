import pyfiglet
import random

def word_scrambler(txt):
    words = txt.split()
    scrambled_words = []
    for word in words:
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            scrambled_words.append(word[0] + ''.join(middle) + word[-1])
        else:
            scrambled_words.append(word)
    print(' '.join(scrambled_words))


def morse_code_3(txt):
    morse_code = {
        'A': "120",
        'B': "21110",
        'C': "21210",
        'D': "2110",
        'E': "10",
        'F': "11210",
        'G': "2210",
        'H': "11110",
        'I': "110",
        'J': "12220",
        'K': "2120",
        'L': "12110",
        'M': "220",
        'N': "210",
        'O': "2220",
        'P': "12210",
        'Q': "22120",
        'R': "1210",
        'S': "1110",
        'T': "20",
        'U': "1120",
        'V': "11120",
        'W': "1220",
        'X': "21120",
        'Y': "21220",
        'Z': "22110",
        '1': "122220",
        '2': "112220",
        '3': "111220",
        '4': "111120",
        '5': "111110",
        '6': "211110",
        '7': "221110",
        '8': "222110",
        '9': "222210",
        '0': "222220",
        ' ': "0"
    }
    txt = txt.upper()
    txt = [morse_code[int] for int in txt]
    txt = ''.join(map(str, txt))
    print(txt)


def morse_code(txt):
    morse_code = {
        'A': ".- ",
        'B': "-... ",
        'C': "-.-. ",
        'D': "-.. ",
        'E': ". ",
        'F': "..-. ",
        'G': "--. ",
        'H': ".... ",
        'I': ".. ",
        'J': ".--- ",
        'K': "-.- ",
        'L': ".-.. ",
        'M': "-- ",
        'N': "-. ",
        'O': "--- ",
        'P': ".--. ",
        'Q': "--.- ",
        'R': ".-. ",
        'S': "... ",
        'T': "- ",
        'U': "..- ",
        'V': "...- ",
        'W': ".-- ",
        'X': "-..- ",
        'Y': "-.-- ",
        'Z': "--.. ",
        '1': ".---- ",
        '2': "..--- ",
        '3': "...-- ",
        '4': "....- ",
        '5': "..... ",
        '6': "-.... ",
        '7': "--... ",
        '8': "---.. ",
        '9': "----. ",
        '0': "----- "
    }
    txt = txt.upper()
    txt = [morse_code[int] for int in txt]
    txt = ''.join(map(str, txt))
    print(txt)


def ascii_art(txt):
    ascii_art = pyfiglet.figlet_format(txt)
    print(ascii_art)
    
def character_shift(txt):
    shift = int(input("give me the shift number: "))
    result = []
    for char in txt:
        result.append(chr(ord(char) + shift))
    print(''.join(result))


def reverse_text(txt):
    print(txt[::-1])


def char_frequency(txt):
    freq = {}
    for char in txt:
        freq[char] = freq.get(char, 0) + 1
    print(freq)


def palindrome_check(txt):
    txt = txt.replace(' ', '').lower()
    if txt == txt[::-1]:
        print("The text is a palindrome.")
    else:
        print("The text is not a palindrome.")


def caesar_cipher(txt, shift=3):
    result = []
    for char in txt:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    print(''.join(result))


def text_to_binary(txt):
    print(' '.join(format(ord(c), 'b') for c in txt))


def pig_latin(txt):
    words = txt.split()
    result = []
    for word in words:
        if word[0] in 'aeiouAEIOU':
            result.append(word + 'way')
        else:
            result.append(word[1:] + word[0] + 'ay')
    print(' '.join(result))


def leetspeak(txt):
    leet_dict = {
        'A': '4', 'B': '8', 'C': '<', 'E': '3', 'G': '6', 'I': '1', 'L': '1',
        'O': '0', 'S': '$', 'T': '7', 'Z': '2'
    }
    result = ''.join([leet_dict.get(c.upper(), c) for c in txt])
    print(result)


def text_to_hex(txt):
    print(' '.join(format(ord(c), 'x') for c in txt))


def word_count(txt):
    words = txt.split()
    word_freq = {word: words.count(word) for word in set(words)}
    print(word_freq)


def replace_spaces(txt, char='_'):
    result = txt.replace(' ', char)
    print(result)

def character_shift_des(txt):
    shift = int(input("give me the shift number: "))
    result = []
    for char in txt:
        result.append(chr(ord(char) - shift))
    print(''.join(result))    



def menu():
    
    print("\nSelect an option:")
    print("1. Morse Code 3")
    print("2. Morse Code")
    print("3. ASCII Art")
    print("4. Character Shift")
    print("5. Word Scrambler")
    print("6. Reverse Text")
    print("7. Character Frequency")
    print("8. Palindrome Check")
    print("9. Caesar Cipher")
    print("10. Text to Binary")
    print("11. Pig Latin")
    print("12. Leetspeak")
    print("13. Text to Hexadecimal")
    print("14. Word Count")
    print("15. Replace Spaces")
    print("16. Character Shift")
    print("0. Exit")
        
    while True:
        
        x = int(input("Enter choice: "))
        if x == 0:
            print("Exiting...")
            break
        elif x in range(1, 17):
            a = input("Enter text: ")
            if x == 1:
                morse_code_3(a)
            elif x == 2:
                morse_code(a)
            elif x == 3:
                ascii_art(a)
            elif x == 4:
                character_shift(a)
            elif x == 5:
                word_scrambler(a)
            elif x == 6:
                reverse_text(a)
            elif x == 7:
                char_frequency(a)
            elif x == 8:
                palindrome_check(a)
            elif x == 9:
                caesar_cipher(a)
            elif x == 10:
                text_to_binary(a)
            elif x == 11:
                pig_latin(a)
            elif x == 12:
                leetspeak(a)
            elif x == 13:
                text_to_hex(a)
            elif x == 14:
                word_count(a)
            elif x == 15:
                replace_spaces(a)
            elif x == 16:
                character_shift_des(a)
        else:
            print("Invalid choice, please try again.")
menu()
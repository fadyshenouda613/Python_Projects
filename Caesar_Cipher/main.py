import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
special_characters = "!@#$%^&*()-+?_=,<>/"""
print(art.logo)

text_array = []


def caesar(text, shift, direction):
    caesar_text = ""
    for letter in text:
        if letter.isnumeric() or letter.isspace() or letter in special_characters:
            caesar_text += letter
            continue
        position = alphabet.index(letter)
        if direction == 'encode':

            new_position = position + shift
            new_letter = alphabet[new_position]
            caesar_text += new_letter
        elif direction == 'decode':
            new_position = position - shift
            new_letter = alphabet[new_position]
            caesar_text += new_letter
    print(f"The {direction}d text is {caesar_text}")


end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)
    user_decision = input("Do you want to restart the program? type 'yes' or 'no' ").lower()
    if user_decision == 'no':
        end = True
        print("Good Bye !!!")

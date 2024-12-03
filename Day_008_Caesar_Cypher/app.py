# Creating Ceasar Cypher

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

print(logo)

def caesar(original_text, shift_amount, encode_decode):
    cipher_text = ""
    if encode_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the {encode_decode}d result: {cipher_text}")

should_continue = False

while not should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart == "no":
        should_continue = True
        print('Goodbye!')
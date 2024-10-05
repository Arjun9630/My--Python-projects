decoding_reference = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
                      14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

encoding_reference = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
                      'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def plain_text__To__cipher_text(plain_text, key):
    enc_cipher_text = ""
    for letter in plain_text.lower():
        try:
            encoding = (encoding_reference[letter] + key) % 26
            encoding_To_Char = decoding_reference[encoding]
            enc_cipher_text += encoding_To_Char
        except KeyError:
            enc_cipher_text += letter  # Keeps non-alphabetic characters unchanged
    return enc_cipher_text

def cipher_text__To__plain_text(cipher_text, key):
    dec_plain_text = ""
    for letter in cipher_text.lower():
        try:
            decoding = (encoding_reference[letter] - key) % 26
            decoding_To_Char = decoding_reference[decoding]
            dec_plain_text += decoding_To_Char
        except KeyError:
            dec_plain_text += letter  # Keeps non-alphabetic characters unchanged
    return dec_plain_text


def main():
    print("Message Encoder and Decoder: \n\n1. Encode Message\n2. Decode Message\n")
    choice = int(input("Enter your choice (1 & 2) = "))
    match choice:
        case 1:
            plain_text = input("Enter the message to be encoded = ")
            encode_key = int(input("Enter the security key = "))
            encoded_text = plain_text__To__cipher_text(plain_text, encode_key)
            print(f"Encoded message = {encoded_text}")
        
        case 2:
            cipher_text = input("Enter the message to be decoded = ")
            decode_key = int(input("Enter the security key = "))
            decoded_text = cipher_text__To__plain_text(cipher_text, decode_key)
            print(f"Decoded message = {decoded_text}")
        
        case _:
            print("Invalid Choice!!")

if __name__ == "__main__":
    main()

import re
import nltk

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
names_list = names.words()


def encrypt(text, key):
    cipher_text = ""
    for n in range(len(text)):
        char = text[n]
        if char.isupper():
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
            # char not letter just add to cipher_txt
            cipher_text += char

    return cipher_text


def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


def crack(text):

    for i in range(26):
        phrase = decrypt(text, i)

        words_split = phrase.split()
        word_count = 0
        for word in words_split:
            word = re.sub(r"[^A-Za-z]+", "", word)
            if word.lower() in word_list or word in names_list:
                word_count += 1

        if (word_count / len(words_split)) > .4:
            return " ".join(words_split)
        else:
            return ""


if __name__ == "__main__":
    e = encrypt("hello", 1)
    crack = crack(e)
    print(crack)

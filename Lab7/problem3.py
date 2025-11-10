#We can create another substitution cipher by permutating the alphabet and map the letters to the corresponding permutated alphabet. Write a function which takes a text and a dictionary to decrypt or encrypt the given text with a permutated alphabet.
#Author - Vedika Udgir

def outer():
    def inner(text, shift):
        result = []
        s = shift % 26
        for ch in text:
            if 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + s) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + s) % 26 + ord('A')))
            else:
                result.append(ch)
        return ''.join(result)
    return inner

cipher_func = outer()

plain = "Hello, World!"
shift = 3
cipher = cipher_func(plain, shift)

print("Plain: ", plain)
print("Shift: ", shift)
print("Cipher:",cipher)
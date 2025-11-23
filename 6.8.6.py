def only_consonants(text):
    vowels = "aeiouAEIOU"
    result = ""
    for c in text:
        if c not in vowels:
            result += c
    return result
def only_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for c in text:
        if c in vowels:
            result += c
    return result
def only_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for c in text:
        if c in vowels:
            result += c
    return result
def is_palindrome(text):
    clean = ""
    for c in text.lower():
        if c.isalpha():
            clean += c

    return clean == clean[::-1]

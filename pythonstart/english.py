def translate_to_vowel(phrase, vowel="a"):
    """Converts 'y' characters back to a specified vowel."""
    original_phrase = ""
    for letter in phrase:
        if letter == "y":
            original_phrase += vowel
        else:
            original_phrase += letter
    return original_phrase

# Original translate function
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation += "y"
        else:
            translation += letter
    return translation

# Input and usage
translated_phrase = translate(input("Enter a phrase to translate: "))
print("Translated:", translated_phrase)

# Convert back to English with a specific vowel
chosen_vowel = input("Enter a vowel to replace 'y' in the translated phrase: ")
print("Original approximation:", translate_to_vowel(translated_phrase, chosen_vowel))

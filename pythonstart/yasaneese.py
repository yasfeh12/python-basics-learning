def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Y"
            else:
                translation=translation+"y"
        else:
            translation = translation + letter
    return translation

print(translate(input("enter a phrase: ")))
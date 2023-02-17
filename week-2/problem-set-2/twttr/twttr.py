# prompts the user for a str of text
text = input("Input: ")

# outputs the same text with all vowels omitted
for s in text:
    if not s.casefold() in ["a", "e", "i", "o", "u"]:
        print(s, end="")

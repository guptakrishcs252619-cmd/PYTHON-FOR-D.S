sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
char_count = len(sentence)

lowercase = sentence.lower()
uppercase = sentence.upper()
modified_sentence = sentence.replace(" ", "_")

print("Number of words:", word_count)
print("Number of characters:", char_count)
print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Modified sentence:", modified_sentence)

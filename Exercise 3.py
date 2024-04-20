sentence=input("Enter a Text :").strip()
if len(sentence) > 10:
    l ="longer"
else:
    l="shorter"
print(f"This string is {l} than 10 characters")
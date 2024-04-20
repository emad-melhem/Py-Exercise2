sentence=input("Enter a string :").strip()
print(f"This string is {len(sentence)} characters long.")
if len(sentence) >=3 and len(sentence) % 3 == 0:
    x=sentence[::-1]
    print(x)
elif len(sentence) > 0:
    print(sentence)
else:
    print("This string is empty !!")
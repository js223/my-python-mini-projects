acronym_list = []

print("Enter a Phrase:")
input_phrase = input()

splitted = input_phrase.split()

for i in splitted_list:
    first_letter = i[0]
    first_letter = first_letter.upper()
    acronym_list.append(first_letter)
     
acronym = "".join(acronym_list)
print(acronym)
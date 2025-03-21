def word_count(book_text):
    num_words = book_text.split()
    word_count = len(num_words)
    #print (f"{w_count} words found in the document")
    return (word_count)

def indy_character_count(book_text):
    character_list = {}
    characters = book_text.lower()
    for character in characters:
        if character in character_list:
            character_list[character] += 1
        else:
            character_list[character] = 1
    #print(character_list)
    return character_list

def sort_on(item):
    return item[1]

def sorted_character_count(character_list):
    filtered_characters = {char: count for char, count in character_list.items() if char.isalpha()}
    
    sorted_character_count = sorted(filtered_characters.items(), key=sort_on, reverse=True)
    
    return sorted_character_count


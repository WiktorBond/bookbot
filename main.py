def main():
    path="books/frankenstein.txt"
    text=get_book_text(path)
    word_count=get_word_count(text)
    char_count=get_character_count(text)
    letter_list=char_dictionary(char_count)
    
    letter_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for char_dict in letter_list:
        if char_dict["name"].isalpha():
            print (f"The '{char_dict['name']}' character was found {char_dict['num']} times")

    print("--- end report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):      
    words=text.split()
    return len(words)

def get_character_count(text):
    char_dict={}
    lower_chars=text.lower()
    char_list=list(lower_chars)
    for letter in char_list:
        if letter.isalpha():
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict

def char_dictionary(char_count):
    letter_list=[]
    for letter, count in char_count.items():
        letter_dict={"name": letter , "num": count}
        letter_list.append(letter_dict)
    return letter_list

def sort_on(letter_list):
    return letter_list["num"]
    
main()
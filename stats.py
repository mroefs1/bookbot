def number_of_words(text):
    words_arr = text.split()
    return len(words_arr)

def number_of_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []
    for char in dict:
        if char.isalpha():
            dict_list.append({"char": char, "num": dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

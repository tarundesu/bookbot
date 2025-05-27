def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(d):
    return d["num"]

def sort_char_count(char_count_dict):
    char_list = []

    for char, count in char_count_dict.items():
        if char.isalpha():  # only include alphabetic characters
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

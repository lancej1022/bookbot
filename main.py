def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = count_words(text)
    letter_counts = count_letters(text)

    letters_list = convert_dict_to_list(letter_counts)
    letters_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{wc} words found in the document\n")
    for dict in letters_list:
        key = dict["key"]
        value = dict["value"]
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["value"]

def convert_dict_to_list(dict):
    result_list = []

    # Iterate through the items in the input dictionary
    for key in dict:
        # Create a dictionary with keys "key" and "value"
        dict_entry = {"key": key, "value": dict[key]}
        # Append the dictionary to the result list
        result_list.append(dict_entry)
    return result_list

def get_book_text(path):
    with open(path) as file:
        return file.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_counts = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    for char in text:
        lowered = char.lower()
        if lowered in letter_counts:
            letter_counts[lowered] += 1

    return letter_counts

main()
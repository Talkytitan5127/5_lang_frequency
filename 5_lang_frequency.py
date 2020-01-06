import os
import re
from collections import Counter


def get_strings_from_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as file_handler:
        return file_handler.read().lower()


def count_frequent_of_words(string_list):
    quantity_of_encounter_words = 10
    word_list = re.findall(r"\w+", string_list)
    return Counter(word_list).most_common(quantity_of_encounter_words)


def print_rating(counter_list):
    print("The most frequent words in this text is:")
    for word_number, word in enumerate(counter_list):
        print("{}) \"{}\" Amount = {}".format(word_number+1, word[0], word[1]))

if __name__ == "__main__":
    string_list = get_strings_from_file(input("Enter the path to the file:"))
    print_rating(count_frequent_of_words(string_list))

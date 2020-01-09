import os
import re
import argparse
from collections import Counter


def get_content_from_file(filepath):
    if not os.path.exists(filepath):
        raise FileExistsError('File doesn\'t exist')
    with open(filepath, "r") as file_handler:
        return file_handler.read().lower()


def count_frequent_of_words(content: str):
    quantity_of_encounter_words = 10
    word_list = re.findall(r"\w+", content)
    return Counter(word_list).most_common(quantity_of_encounter_words)


def print_rating(most_frequent_words):
    print("The most frequent words in this text is:")
    for index, data in enumerate(most_frequent_words, 1):
        word, amount = data
        print("{}) \"{}\" Amount = {}".format(index, word, amount))


def create_argparser():
    parser = argparse.ArgumentParser(description='Get most frequent words in file')
    parser.add_argument('--filepath', type=str, help='path to your file')
    return parser


if __name__ == "__main__":
    parser = create_argparser()
    args = parser.parse_args()

    content = get_content_from_file(args.filepath)
    most_frequent_words = count_frequent_of_words(content)
    print_rating(most_frequent_words)

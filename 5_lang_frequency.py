import os
import re
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    return re.findall(r'\w+', open(filepath).read().lower())

def count_words(data):
    return Counter(file).most_common(10)

def print_words(data):
    for word in data:
        print(*word)

    
if __name__=='__main__':
    print("Enter the path to the file")
    file=load_data(input())
    print_words(count_words(file))
      
    

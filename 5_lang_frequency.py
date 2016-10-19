import os
import re
from collections import Counter

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,"r") as file_handler:
        return file_handler.read().lower()

def count_words(data):
    quantity_of_encounter_words=10
    words=re.findall(r'\w+',data)
    return Counter(words).most_common(quantity_of_encounter_words)

def print_words(data):
    print("The most frequent words in this text is:")
    for word_number,word in enumerate(data):
        print(word_number+1,')',sep='',end=' ')
        print('"',word[0],'"',sep='',end=' ')
        print("Amount =",word[1])

if __name__=='__main__':
    print("Enter the path to the file")
    file=load_data(input())
    print_words(count_words(file))
    
      
    

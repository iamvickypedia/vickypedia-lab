from itertools import product, permutations
import time
from nltk.corpus import wordnet, words

def make_word(i,arr):
    return permutations(arr,i)
arr = input('Enter letters to generate words with\n')
arr = set(arr.replace(' ',''))
total_count = 0

def add_words(all_words):
    word_list = set()
    for word in all_words:
        word = ''.join(word)
        if word in words.words():
            yield word

print('All letter Combinations --')
start_time = time.time()
try:
    for i in range(3,10):
        got_words = make_word(i,arr)
        #print(list(got_words))
        temp_h = 0
        for i,word in enumerate(add_words(got_words)):
            if i > temp_h:
                temp_h = i
            print(word)
        total_count += temp_h
    print('\nEndtime {}, and length of list {}'.format(time.time() - start_time,total_count))

except BaseException as be:
    print(be)
    print(f'\n{total_count} Counted so far')

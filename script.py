import nltk
import re

nltk.download('words')

from helper import ADDITIONAL_WORDS, letter_frequency, score_words
from nltk.corpus import words

word_list = [word for word in words.words() if re.match("^[a-z]{5}$", word)]
word_list += ADDITIONAL_WORDS
word_list = list(set(word_list))

frequency = letter_frequency(word_list)
scored_words = score_words(word_list, frequency)
sorted_scored_words = sorted(scored_words.items(), key=lambda x: x[1], reverse=True)

print(len(sorted_scored_words))
for i in range(5):
    print(sorted_scored_words[i][0] + ' :: ' + str(sorted_scored_words[i][1]))

new_word_list = word_list
regex = ['.'] * 5
letters_in = []
letters_out = []

while len(new_word_list) > 1:
    guess = input('Guess: ')
    result = input('Result (gray=1, yellow=2, green=3): ')

    if len(guess) != 5 or len(result) != 5:
        continue

    for i in range(5):
        if result[i] == '3':
            regex[i] = guess[i]
        elif result[i] == '2':
            if type(regex[i]) == list:
                regex[i].append(guess[i])
            else:
                regex[i] = [guess[i]]
            letters_in.append(guess[i])
        elif result[i] == '1':
            letters_out.append(guess[i])

    for i in range(5):
        if type(regex[i]) == list:
            regex[i] = "[^{}]".format(''.join(regex[i]))

    new_word_list = [word for word in new_word_list if re.match("^{}$".format(''.join(regex)), word)]
    letters_in = list(set(letters_in))
    for letter in letters_in:
        new_word_list = [word for word in new_word_list if letter in word]
    letters_out = list(set(letters_out))
    for letter in letters_out:
        new_word_list = [word for word in new_word_list if letter not in word]

    scored_words = score_words(new_word_list, frequency)
    sorted_scored_words = sorted(scored_words.items(), key=lambda x: x[1], reverse=True)

    num_print = 5 if len(sorted_scored_words) > 5 else len(sorted_scored_words)

    print(len(sorted_scored_words))
    for i in range(num_print):
        print(sorted_scored_words[i][0] + ' :: ' + str(sorted_scored_words[i][1]))

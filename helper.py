import string

ADDITIONAL_WORDS = [
    'masse'
]


def letter_frequency(word_list):
    frequency = {}

    word_list_stringified = ''.join(word_list)
    len_word_list_stringified = len(word_list_stringified)

    letters = list(string.ascii_lowercase)
    for letter in letters:
        frequency[letter] = word_list_stringified.count(letter) / len_word_list_stringified * 100

    return frequency


def score_words(word_list, frequency):
    word_scores = {}

    for word in word_list:
        score = 0
        for letter in word:
            score += frequency[letter] / word.count(letter)
        word_scores[word] = round(score, 4)

    return word_scores

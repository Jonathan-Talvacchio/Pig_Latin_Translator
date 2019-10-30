from collections import deque

vowels = ['a', 'e', 'i', 'o', 'u']


def find_vowels(word_list_selected):
    # --Reset num_consonants for next word--
    num_consonants = 0
    num_vowel = 0
    # --Finds vowels--
    for letter in ''.join(word_list_selected).lower():
        if '{}'.format(letter) not in vowels:
            num_consonants += 1
        elif '{}'.format(letter) in vowels:
            num_vowel += 1
            return num_consonants, num_vowel
    if num_vowel == 0:
        return num_consonants, num_vowel


def switch_letters(num_consonants, num_vowels, word_selected):
    reordered_list = list()
    # --Switch letters--
    for i in range(num_consonants):
        if num_vowels > 0:
            letter_copy = deque(word_selected).popleft()  # --Copy far left letter--
            del word_selected[0]  # --Delete far left letter--
            reordered_list.append(letter_copy)  # --Add copied letter to far right of new list--

    return reordered_list


def rebuild_word(word_selected, reordered_list, num_consonants):
    # --Rebuild word with list combinations and suffix--
    new_word = "{0}-{1}{suffix} ".format(''.join(word_selected),
                                         ''.join(reordered_list).lower(),
                                         suffix="ay" if num_consonants >= 1 else "way")  # Start w/ const -ay else -way
    return new_word

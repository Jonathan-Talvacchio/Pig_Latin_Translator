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
            # --Subtract one so first letter starts at 0 like an array--
            print('Contains: {letter}, in position {number}'.format(letter=letter.upper(),
                                                                    number=(num_consonants + num_vowel) - 1))
    return num_consonants, num_vowel

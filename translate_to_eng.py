import translate_to_pig as t_pig
import json
import gzip
import os
import re

file_name = 'Pig_Dict.json'
path = "Dictionaries/"
regex = re.compile('[^a-zA-Z ]')  # --A white list of characters not to delete--


def save_json_file(data):
    save_file_json_frame(path + file_name, data)


def save_file_json_frame(_file, data):
    with gzip.GzipFile(_file, 'w') as f:
        json_str = json.dumps(data)
        json_bytes = json_str.encode('utf-8')

        f.write(json_bytes)


def load_json_file():
    return load_file_json_frame(path + file_name)


def load_file_json_frame(_file):
    with gzip.GzipFile(_file, 'r') as f:
        json_bytes = f.read()
        json_str = json_bytes.decode('utf-8')
        data = dict(json.loads(json_str))
        return data


def save_word_to_dict(new_word):
    def to_pig(_og_list, _word_selected, _reordered_list):
        for word in range(len(_og_list)):
            # --Grab word from list--
            _word_selected = list(_og_list[word])

            # --Finds vowels--
            num_consonants, num_vowels = t_pig.find_vowels(_word_selected)

            # --Switch letters in word--
            _reordered_list = t_pig.switch_letters(num_consonants, num_vowels, _word_selected)

            # --Save to dictionary--
            _new_word = rebuild_word(_word_selected, _reordered_list, num_consonants).lower().split()
            loaded_dict[''.join(_new_word)] = ''.join(_og_list[word]).lower()
            save_json_file(loaded_dict)

    if isinstance(new_word, str):
        compiled_new_word = regex.sub('', new_word)

        if len(list(compiled_new_word.split())) == 1:
            to_pig(list(compiled_new_word.split()), list(), list())
            print('Word saved!')
        else:
            print('Must be ONLY one word.')
    else:
        print('Input MUST be str.')


def rebuild_word(word_selected, reordered_list, num_consonants):
    # --Rebuild word with list combinations and suffix--
    new_word = '{0}{1}{suffix} '.format(''.join(word_selected).lower(),
                                        ''.join(reordered_list).lower(),
                                        suffix='ay' if num_consonants >= 1 else 'way')  # Start w/ const -ay else -way
    return new_word


def translate_to_eng(user_input, _dict):
    new_word = ''
    unk_word = ''

    if user_input.lower() in _dict:
        new_word = '{0} '.format(_dict[user_input.lower()])
        return new_word, unk_word
    else:
        new_word = '"{word}" '.format(word=user_input)
        unk_word = new_word
        return new_word, unk_word


def app_start():
    # --If file exists--
    if os.path.isfile(path + file_name):
        if os.stat(path + file_name).st_size != 0:
            _loaded_dict = load_json_file()
            return _loaded_dict
        else:
            save_json_file(dict())
            _loaded_dict = load_json_file()
            return _loaded_dict
    else:
        print('Dictionary not found. Creating dictionary...')
        os.mkdir(path)
        save_json_file(dict())
        _loaded_dict = load_json_file()
        print('Dictionary created.')
        return _loaded_dict


loaded_dict = app_start()

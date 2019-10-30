from custom_prompts import run_custom_prompts, cls
import translate_to_pig as t_pig
import translate_to_eng as t_eng
import re

custom_promt_hotkey = '`'
toggle_key = ["/t", "-t"]
toggle = True
regex = re.compile('[^a-zA-Z ]')  # --A white list of characters not to delete--

def to_pig(_og_list, _word_selected, _reordered_list, _new_list):
    for word in range(len(_og_list)):
        # --Grab word from list--
        _word_selected = list(_og_list[word])

        # --Finds vowels--
        num_consonants, num_vowels = t_pig.find_vowels(_word_selected)

        # --Switch letters in word--
        _reordered_list = t_pig.switch_letters(num_consonants, num_vowels, _word_selected)

        # --Save to dictionary--
        new_word = t_eng.rebuild_word(_word_selected, _reordered_list, num_consonants).lower().split()
        t_eng.loaded_dict[''.join(new_word)] = ''.join(_og_list[word]).lower()
        t_eng.save_json_file(t_eng.loaded_dict)

        # --Rebuilds word then reorder back into sentence word by word--
        _new_list.append(t_pig.rebuild_word(_word_selected, _reordered_list, num_consonants))

    # --Print translated sentence--
    print(">>> {0}\n".format(''.join(_new_list).capitalize()))


def to_eng(_og_list, _word_selected, _new_list):
    unk_list = list()
    for word in range(len(_og_list)):
        # --Grab word from list--
        _word_selected = list(_og_list[word])

        # --Finds word in dictionary then add to list word  by word--
        new_word, unk_word = t_eng.translate_to_eng(''.join(_word_selected), t_eng.loaded_dict)
        _new_list.append(new_word)

        # --Adds unknown words to unknown list--
        if re.search('[a-zA-Z]', unk_word):
            unk_list.append(unk_word)

    # --Print translated sentence--
    print(">>> {0}\n".format(''.join(_new_list).capitalize()))

    # --Print unknown words--
    if len(unk_list) > 0:
        print("Unknown Words: ")
        for _word in unk_list:
            print('-{0}'.format(_word))
        print("\n")


def app_start():
    cls()
    print("Would you like to translate from english to pig latin? This may be changed later.")
    while (True):
        user_input = input("(y,n): ").lower()
        if user_input == 'y':
            _toggle = True
            cls()
            return _toggle
        elif user_input == 'n':
            _toggle = False
            cls()
            return _toggle
        else:
            print("Input not recognized.")


def app_main(_toggle):
    while (True):
        user_input = input("Type in {0}: ".format("english" if _toggle else "pig latin"))
        compiled_input = regex.sub('', user_input)  # --Remove any non-letters expt spaces--
        og_list = list(compiled_input.split())  # --Splits and sets input into list--
        word_selected = list()
        reordered_list = list()
        new_list = list()

        # --Starts custom debug consul--
        if user_input == custom_promt_hotkey:
            run_custom_prompts(user_input, custom_promt_hotkey)
            print('\n')
            continue
        elif user_input in toggle_key:
            _toggle = not _toggle
            cls()
            print('\n')
            continue
        elif not re.search('[a-zA-Z]', compiled_input):
            print("No words found.\n")
            continue

        if _toggle:
            to_pig(og_list, word_selected, reordered_list, new_list)

        if not _toggle:
            to_eng(og_list, word_selected, new_list)


toggle = app_start()

app_main(toggle)

import translator_debug as t_debug
from translate_to_eng import *
from cmd import Cmd
import json
import os

print_dict_file = 'Printed-Dictionary.json'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class MyPrompts(Cmd):
    def do_toggle(selfm, args):
        """'/t' is currently used to switch translations."""
        print("{key} is currently used to switch translations.".format(key='\\t'))

    def do_switch(self, args):
        """Switch translation. CURRENTLY NOT WORKING."""
        print('Switch translation. CURRENTLY NOT WORKING. ')

    def do_open_dict(self, args):
        """Open archived dictionary"""
        for key in loaded_dict:
            print('{value}'.format(value=''.join(loaded_dict[key]).upper()))
            print('{key} : {value}\n'.format(key=key, value=loaded_dict[key]))
        print('Items in the dictionary: {dict_count} !'.format(dict_count=len(loaded_dict)))

    def do_clear_dict(self, args):
        """Deletes archived dictionary"""
        print('Are you sure you want to delete th dictionary?')
        user_input = input('(y,n): ').lower()
        if user_input == 'y':
            print('Clearing dictionary...')
            save_json_file(dict())
            loaded_dict = load_json_file()
            print('Dictionary cleared.')
        else:
            print('Dictionary NOT deleted')

    def do_print_dict(self, args):
        """Save readable version of dictionary to file."""
        print('Printing dictionary to file: "{0}"'.format(print_dict_file))
        with open(print_dict_file, 'w') as f:
            # json.dump(loaded_dict, f)
            for i in loaded_dict:
                json_str = '{value}:\n({key}:{value})\n\n'.format(key=json.dumps(i),
                                                                  value=json.dumps(loaded_dict[i])).upper()

                f.write(json_str)
        print('Print completed.\n')
        print('Would you like to open {0}?'.format(print_dict_file))
        user_input = input('(y,n): ').lower()
        if user_input == 'y':
            os.startfile(print_dict_file)

    def do_delete_print(self,args):
        """Deletes printed dictionary file."""
        if os.path.isfile(print_dict_file):
            os.remove(print_dict_file)
        else:
            print('Can\'t find file: {file}'.format(print_dict_file))

    def do_vowel_count(self, args):
        """Count vowels, and placement in input word."""
        if len(args) != 0:
            num_consonants, num_vowel = t_debug.find_vowels(args)
            print('input text: {0}, vowels: {1}, consonants: {2} '.format(''.join(args).upper(),
                                                                          num_vowel,
                                                                          num_consonants))
        else:
            print('No word input.')

    def do_in_dict(self, args):
        """Checks if input word is in the dictionary."""
        if len(args) > 0:
            if args in loaded_dict.values():
                print('{word} was found!'.format(word=args.upper()))
            else:
                print('{word} not found.\n'.format(word=args.upper()))
                print('Would you like to add {word}?'.format(word=args.upper()))
                user_input = input('(y,n): ').lower()
                if user_input == 'y':
                    save_word_to_dict(args)
                else:
                    print('Word not saved.')
        else:
            print('Search canceled, no word input.')

    def do_delete_key(self, args):
        """Delete input key form dictionary."""
        if args in loaded_dict:
            print('"{value}"'.format(value=loaded_dict[args]).upper())
            print('{key} : {value}\n'.format(key=args, value=loaded_dict[args]).upper())

            print('Are you sure you would like to remove the key: {key} ?'.format(key=args.upper()))
            user_input = input('(y,n): ').lower()
            if user_input == 'y':
                del loaded_dict[args]
                save_json_file(loaded_dict)
                load_json_file()
                print('Key deleted.')
            else:
                print('Key not deleted.')
        else:
            print('Key: {key} not found.'.format(key=args.upper()))

    def do_clear(self, args):
        """Clear terminal and return to application."""
        cls()
        return True

    def do_return(self, args):
        """Returns to application."""
        return True

    def do_quit(self, args):
        """Quits the application."""
        print('Quitting...')
        raise SystemExit


def run_custom_prompts(check_string, string_key):
    if __name__ == 'custom_prompts' and check_string == string_key:
        prompt = MyPrompts()
        prompt.prompt = '\n>>> '
        prompt.cmdloop('\nStarting prompt...')

from collections import deque

user_str = input('Type in english: ')
og_list = list(user_str)
vowels = ['a', 'e', 'i', 'o', 'u']
num = 0

while (True):

    # --Finds vowels--
    for letter in user_str.lower():
        if '{}'.format(letter) not in vowels:
            num = num + 1
            # print(num)
        elif '{}'.format(letter) in vowels:
            # print('input text: {0}, contains: {1}, in position: {2} '.format(user_str.upper(), letter.upper(), num))
            break
    # print('--NEXT--')

    reordered_list = list()

    # --Switch letters--
    for i in range(num):
        letter_copy = deque(og_list).popleft()
        del og_list[0]

        reordered_list.append(letter_copy)

    # print('--END--')
    print('{0}-{1}ay\n'.format(''.join(og_list), ''.join(reordered_list).lower()))

    user_str = input('Type in english: ')
    og_list = list(user_str)
    num = 0

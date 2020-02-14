#!usr/bin/env python3

def char_count(str_):
    char_dict = {}
    for char in str_:
        char_dict[char] = char_dict.get(char, 0) + 1
    for key in char_dict:
        print(key, char_dict[key])

if __name__ == '__main__':
    s = input('Enter a string: ')
    char_count(s)

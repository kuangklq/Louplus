def char_count(str_):
    countdict = {}
    for char in str_:
        countdict[char] = countdict.get(char, 0) + 1
    for key,value in countdict.items():
        print(key,value)
if __name__ == '__main__':
    s = input('Enter a string:')
    char_count(s)

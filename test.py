try:
    dict_file = '/home/timr/code/CIT95FA23/flash-bonus-code-challenge-hangman-game-timr/list.txt'
    dict_open = open(dict_file, 'r')
except Exception as err:
    print(err)
finally:
    # print(dict_open.readlines().remove())
    dict_array = []
    with open(dict_file) as f:
        my_list = f.read().splitlines()
        dict_array = my_list
    # file_word = dict_open.readline()
    # while file_word != "":
    #     dict_array.append(file_word)
    #     file_word = dict_open.readline()

print(dict_array)
# print(my_list)
print(type(dict_array))
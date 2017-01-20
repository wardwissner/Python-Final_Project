import random
import time
import datetime
from datetime import date
from time import strftime
print(date.today())
print(date.today().strftime("%A %d. %B %Y"))
todays_date = date.today().strftime("%A %d. %B %Y")


def read_text_file(input_file):
    # read text file
    str_value = ""
    with open(input_file) as read_me:
        for line in read_me:
            str_value += line
# filter text file form list and filtered string
        str_value_filtered = str_value.splitlines()
        str_value = ""
        for phrases in str_value_filtered:
            str_value += phrases + " "
        return str_value


def form_word_list(str_value):
    word_set = []
    word = ""
# form word list
    for i in range(0, len(str_value)):
        word += str_value[i]
        if str_value[i] == " ":
            word_set.append(word)
            word = ""
    print("word set  ", word_set)
    return word_set


def form_dictionary(word_set):
    # form dictionary
    dict_nary = {}
    for i in range(0, len(word_set) - key_size):
        key_value = word_set[i]
        for j in range(1, key_size):
            key_value += word_set[i + j]
            print("key value  ", key_value)
        if key_value in dict_nary.keys():
            print("key value match  ", key_value)
            dict_nary[key_value].append(word_set[i + key_size])
        else:
            dict_nary[key_value] = [word_set[i], word_set[i + key_size]]
            for keys_items in dict_nary.keys():
                print(keys_items, ":", dict_nary[keys_items])
    return dict_nary


def form_sonnett_string(dict_nary, word_set):
    rand_int = random.randint(0, len(word_set) - key_size - 1)
    initial_key = word_set[rand_int]
    for j in range(1, key_size):
        initial_key += word_set[rand_int + j]
    print("random integer %s  initial key  %s word_set1  %s   word_set2  %s" %
          (rand_int, initial_key, word_set[rand_int], word_set[rand_int + 1]))

    todays_date = date.today().strftime("%A %d. %B %Y")


# form sonnett character string & write a line of sonnett

    sonnett_string = initial_key
    print(" sonnett string", sonnett_string)
    with open(output_file, "a") as sonnet_line:
        sonnet_line.writelines("Sonnett for Pat  " + todays_date + '\n')
        sonnet_line.writelines("" + '\n')

    num_lines = 0
    while num_lines <= 13:
        while len(sonnett_string) <= 50:
            new_word_set = dict_nary[initial_key]
            print("new word set", new_word_set)
            random_integer = random.randint(1, len(new_word_set) - 1)
            new_word = new_word_set[random_integer]
            print(" random integer new word", random_integer, new_word)
            sonnett_string += new_word
            print("sonnet_string", sonnett_string)
            new_key = initial_key + new_word
            print("new_key", new_key)
            initial_key = new_key[len(new_word_set[0]):len(new_key)]
            print("initial_key", initial_key)
        else:
            with open(output_file, "a") as sonnet_line:
                sonnet_line.writelines(sonnett_string + '\n')
                print("sonnet_line", sonnet_line)
                num_lines += 1
                sonnett_string = ""
                print("initial key   ", initial_key)
                print("number of lines  ", num_lines)
    return


def write_sonnett(input_file, output_file):
    str_value = read_text_file(input_file)
    word_set = form_word_list(str_value)
    dict_nary = form_dictionary(word_set)
    form_sonnett_string(dict_nary, word_set)
    return
input_file = "Sonnetts-large.txt"
output_file = "markov_sonnet.txt"
key_size = 2
write_sonnett(input_file, output_file)

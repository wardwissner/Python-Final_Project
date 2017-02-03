import random
import time
import datetime
from datetime import date
from time import strftime
import pronouncing


def form_last_word_dictionary(rhyme_set):
  last_word_dictionary = {}
  for i in range(len(rhyme_set)):
     if rhyme_set[i] in last_word_dictionary.keys():
        last_word_dictionary[rhyme_set[i]].append(i)
     else:
        last_word_dictionary[rhyme_set[i]] = [i]
  for key in last_word_dictionary.keys():
#      print(last_word_dictionary.keys().index(key),':',last_word_dictionary[key])
       print( list(last_word_dictionary.keys()).index(key),':',key,':',last_word_dictionary[key]) 
  L =last_word_dictionary     
  return  L

def read_text_file(input_file):
    # read text file
    str_value = ""
    num_lines = 0
    rhyme_set = []
    char_len = 0
    char_len_sq =0
    with open(input_file,"r") as read_me:
      for line in read_me:
        line = line.lower()        
        num_lines  += 1
        last_str_value = line
        print(len(last_str_value))
        char_len += len(last_str_value)
        char_len_sq += len(last_str_value)**2
        if len(last_str_value) > 1 :
          last_str_value = last_str_value.translate(bytes.maketrans(b"!?.:;,'", b"       "))
          print(last_str_value.rsplit(None, 1)[-1], num_lines)
          last_word = last_str_value.rsplit(None, 1)[-1]
          print(last_word, num_lines)
          rhyme_set.append(last_word)        
        str_value += line
        str_value = str_value.translate(bytes.maketrans(b"!?.:;,'", b"       ") ) 
# filter text file form list and filtered string
      str_value_filtered = str_value.splitlines()
      str_value = ""
      for phrases in str_value_filtered:
        str_value += phrases + " "
    for i in range(len(rhyme_set)):
        print(i, ":", rhyme_set[i])
    list_read = [str_value,rhyme_set]
    print (rhyme_set)
    av_char = char_len/float(num_lines)
    print(av_char,num_lines)
    std_char_len  = ((char_len_sq- num_lines*av_char**2)/(float(num_lines)- 1)) **.5
    print("average line size","...",av_char,"std...",std_char_len)  
    return list_read



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
        print("key Item: ", keys_items, ":", dict_nary[keys_items])

    return dict_nary

def form_initial_key(word_set):
   rand_int = random.randint(0, len(word_set) - key_size - 1)
   initial_key=word_set[rand_int]
   for j in range(1, key_size):
      initial_key += word_set[rand_int + j]
      print("random integer %s  initial key  %s word_set1  %s   word_set2  %s" %
          (rand_int, initial_key, word_set[rand_int], word_set[rand_int + 1]))
   return initial_key


def form_sonnett_string(dict_nary,initial_key,markov_output_lines):
        
# form sonnett character string 
    sonnett_line_set = []
    num_lines=0
    sonnett_string = ""
    while num_lines < markov_output_lines:
        while len(sonnett_string) <= 50:
            new_word_set=dict_nary[initial_key]
            print("new word set", new_word_set)
            random_integer=random.randint(1, len(new_word_set) - 1)
            new_word=new_word_set[random_integer]
            print(" random integer new word", random_integer, new_word)
            sonnett_string += new_word
            print("sonnet_string", sonnett_string)
            new_key=initial_key + new_word
            print("new_key", new_key)
            initial_key=new_key[len(new_word_set[0]):len(new_key)]
            print("initial_key", initial_key)
        else:
                print("sonnet_line", sonnett_string)
                sonnett_line_set.append(sonnett_string)
                num_lines += 1
                sonnett_string = ""
                print("initial key   ", initial_key)
                print("number of lines  ", num_lines)
    return sonnett_line_set



def find_rhyme_word(string, last_word_dictionary,rhyme_set):
  rhyme_index_correction=[2,2,-2,-2,2,2,-2,-2,2,2,-2,-2,1,-1] 
  ryme_set=pronouncing.rhymes(string)
  if len(ryme_set)>0:
       random_int =random.randint(0,len(ryme_set))
       return ryme_set[random_int-1]
  elif not(string in last_word_dictionary.keys()):
    return string
  else:
      key_values = last_word_dictionary[string]
      rand_integer=random.randint(0,len(key_values)-1)
      index_chosen =key_values[rand_integer]
      index_correction =rhyme_index_correction [index_chosen%14]
      rhyme_index=index_chosen+index_correction
      rhyme_word=rhyme_set[rhyme_index]
      print(key_values,rand_integer,index_correction,rhyme_index,string,rhyme_word)
      return rhyme_word
  


def get_last_word(string):
  last_word= string.rsplit(None, 1)[-1]
  print (last_word)
  return last_word


def replace_last_word(string,rhyme_word):
  last_word=get_last_word(string)
  print(last_word,rhyme_word )
  cut= len(string)-len(last_word)
  print("cut",len(string),cut)
  string= string[0:cut-1] + " " + rhyme_word
  print(string)
  return string

def quatrane(n,pointer,last_word_dictionary,rhyme_set):
  for j in range(0,2):
    last_word=get_last_word(n[pointer+j])
    print(last_word)
    rhyme_word= find_rhyme_word(last_word,last_word_dictionary,rhyme_set)
    print(rhyme_word)
    n[pointer+j+2]=replace_last_word(n[pointer+j+2],rhyme_word)
    print(n[pointer+j+2])
    print(n)
  return n

def cuplet( n ,pointer,last_word_dictionary ,rhyme_set):
    last_word=get_last_word(n[pointer])
    print(last_word)
    rhyme_word= find_rhyme_word(last_word,last_word_dictionary,rhyme_set)
    print(rhyme_word,n[pointer+1])
    n[pointer+1]=replace_last_word(n[pointer+1],rhyme_word)
    print (n)
    return n

def shakespeare_sonnett(n,last_word_dictionary,rhyme_set):
    for pointer in range (0,12,4):
        n= quatrane(n,pointer,last_word_dictionary,rhyme_set)
        print (n)
    n= cuplet(n,12,last_word_dictionary,rhyme_set)
    print(n)
    return n

def out_put_shakespeare_sonnett(l):
  with open(output_file,"a") as flines:
    todays_date=date.today().strftime("%A %d. %B %Y")
    flines.writelines("Sonnett for Pat  " + todays_date + '\n')
    flines.writelines("" + '\n')
    for j in range(0,14):
      flines.write(l[j] + '\n')
      if (j==3 or j==7 or j==11):
        flines.write("" + "\n")
  return

def write_sonnett(input_file, output_file):
    list_read=read_text_file(input_file)
    str_value =list_read[0]
    rhyme_set =list_read[1]
    word_set=form_word_list(str_value)
    dict_nary=form_dictionary(word_set)
    last_word_dictionary = form_last_word_dictionary(rhyme_set)
    initial_key = form_initial_key(word_set)
    markov_sonnett = form_sonnett_string(dict_nary,initial_key,markov_output_lines)
    n = shakespeare_sonnett(markov_sonnett,last_word_dictionary,rhyme_set)
    out_put_shakespeare_sonnett(n)
    return 


input_file="Sonnetts-large2.txt"
output_file="markov_sonnet.txt"
key_size=2
markov_output_lines=14
write_sonnett(input_file, output_file) 





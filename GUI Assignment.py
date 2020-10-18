##Gavin Swiger
##October 18th 2020
## Module 6 | SDLC Assignment

##Submit your .java files for the application, and a couple of screen shots of your program in action.
##Submit a screen shot of the top 20 words in the following file (a poem): https://www.gutenberg.org/files/1065/1065-h/1065-h.htm
##Submit to your GIT hub repository and provide the link


import re
import tkinter as tk


def clean_the_poem(poem):
    ##Clean the poem string variable
    poem = poem.replace(',',' ')
    poem = poem.replace('â€',' ') ##Was used as online line continuation character.
    poem = re.sub('[\W_]+', ' ', poem)
    poem = poem.lower()##Changes the string to all lower case.
    poem = poem.split()
    return poem;

def get_most_common_words():

    ##Open and store the file as a string.
    with open("Module 2 Poem.txt", "r") as file:
        poem = file.read().replace('\n', ' ')

    poem = clean_the_poem(poem);


    ##Make a list of all the different words in the poem.
    unique_words = []

    for word in poem:
        if word not in unique_words:
            unique_words.append(word)


    ##Make a dictionary with words as "keys" and occurrance rate as "values"

    unique_word_dict = {}
    for word in unique_words:
        item = {word: poem.count(word)}
        unique_word_dict.update(item)

    ##Make a new dictionary with words sorted by occurrance rate.
    ##This sorts into accending order.
    sorted_unique_word_dict = sorted(unique_word_dict.items(), key=lambda x: x[1])
    sorted_unique_word_dict_decending = {}
    sorted_unique_word_dict_decending_short = {}
    j = 0


    ##Loop through dictionary backwards printing value and key.
    i = len(sorted_unique_word_dict) - 1

    while(i != -1):
        if j < 10:
            sorted_unique_word_dict_decending_short[j] = sorted_unique_word_dict[i]
        if j < 20:
            sorted_unique_word_dict_decending[j] = sorted_unique_word_dict[i]
        j = j + 1
        i = i-1

    return sorted_unique_word_dict_decending_short, sorted_unique_word_dict_decending


# Tkinter GUI-------------------------------------------

def print_twenty_most_common_words():

    top_twenty_words = ''
    i = 0;
    while (i != 20):
        top_twenty_words = top_twenty_words + sorted_poem_words[i][0] + ", "
        i = i + 1
    my_label.config(text=top_twenty_words)


def print_ten_most_common_words():

    top_ten_words = ''
    i = 0;
    while (i != 10):
        #print(sorted_poem_words[i][0])
        top_ten_words = top_ten_words + sorted_poem_words[i][0] + ", "
        i = i+1
    my_label.config(text=top_ten_words)



window = tk.Tk()


window.geometry("600x80")
window.title('The Raven Word Occurrence Counter')


ten_button = tk.Button(window, text ="Top 10 Words in the Poem", command = print_ten_most_common_words)
ten_button.pack(side= tk.TOP, anchor= tk.W, fill= tk.X, expand= tk.YES)


twenty_button = tk.Button(window, text="Top 20 Words in the Poem", command = print_twenty_most_common_words)
twenty_button.pack(side= tk.TOP, anchor= tk.W, fill= tk.X, expand= tk.YES)


my_label = tk.Label(window, bg="white", text="")
my_label.pack(side= tk.BOTTOM, anchor= tk.W, fill= tk.X, expand= tk.YES)


sorted_poem_words_short, sorted_poem_words = get_most_common_words()
window.mainloop()










    




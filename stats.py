def count_words(the_book):
    word_list = the_book.split()
    return len(word_list)

def count_chars(the_book_text):
    formated_book = the_book_text.lower()
    list_of_chars = list(formated_book)
    finished_list_of_unique = {}
    for chara in list_of_chars:
        if chara in finished_list_of_unique:
            finished_list_of_unique[chara] += 1
        else:
            finished_list_of_unique[chara] = 1
    return finished_list_of_unique

def clean_print(dic_of_chars):
    unsorted_list = []
    for key in dic_of_chars:
        unsorted_list.append({"char": key, "num": dic_of_chars[key]})
    unsorted_list.sort(reverse=True, key=helper_print)
    return unsorted_list
    
def helper_print(dic_to_sort_num):
    return dic_to_sort_num["num"]
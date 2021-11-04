from typing import List
import random
import string


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    I Love op
    """
    list_of_game_letters = []
    timed_list = []
    letters = [j for j in string.ascii_lowercase]
    for i in range(9):
        timed_list.append(random.choice(letters))
        if len(timed_list) == 3:
            list_of_game_letters.append(timed_list)
            timed_list = []
    return list_of_game_letters


game_letters = generate_grid()
list_of_letters = []
for i in game_letters:
    for j in i:
        list_of_letters += j


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    forbidden_letters = [i for i in string.ascii_lowercase]
    for i in letters:
        try:
            forbidden_letters.remove(i)
        except:
            pass
    words_file = open(f)
    word_list = []
    letstr = ""
    for i in letters:
        letstr += i
    for word in words_file:
        word = word[:-1].lower()
        if len(word) >= 4:
            count = 0
            for let in word:
                if let in forbidden_letters:
                    count += 1
                if word.count(let) > letstr.count(let):
                    count += 1
            if letters[4] not in word:
                count += 1
            if count == 0:
                word_list.append(word)
    return word_list


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = input()
    user_words = user_words.split()
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    unknown_words = []
    for wordd in user_words:
        if wordd not in words_from_dict:
            unknown_words.append(wordd)
    forbidden_letters = [i for i in string.ascii_lowercase]
    for i in letters:
        try:
            forbidden_letters.remove(i)
        except:
            pass
    word_list = []
    letstr = ""
    for i in letters:
        letstr += i
    for word in unknown_words:
        if len(word) >= 4 and len(word) <= 9:
            count = 0
            for let in word:
                if let in forbidden_letters:
                    count += 1
                if word.count(let) > letstr.count(let):
                    count += 1
            if letters[4] not in word:
                count += 1
            if count == 0:
                word_list.append(word)
    return word_list


def results():
    gridd = generate_grid()
    grid = []
    for lst in gridd:
        for let in lst:
            grid.append(let)
    user_words = get_user_words()
    dict_of_words = get_words('en', grid)
    pure_user_words = get_pure_user_words(user_words, list_of_letters, dict_of_words)
    with open("results.txt", "w", encoding="utf-8") as result:
        dictionary = ",".join(dict_of_words)
        user_words = ",".join(user_words)
        result.write(dictionary)
        result.write((user_words))


# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())

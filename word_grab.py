import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"


def two_word_name():
    response = requests.get(word_site)

    print(type(response.content))
    print(response.text)
    words = response.text
    words = words.splitlines()

    rand_name = ' '.join([words[random.randint(0, len(words))] for i in range(2)])
    return rand_name

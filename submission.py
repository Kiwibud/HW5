# ---------------------------------------------------------------------
# Name: Homework 5
# Purpose:
# Author: Kiwibud
# ---------------------------------------------------------------------
"""
Application of generator expression, lambda expression and decorator

Find the length of each word in a string
Compute geometric sum of the given number
Find the string with the most number of words
Find n cities with lowest average temperatures
Decorator to convert strings to uppercase in a secret language
"""
import string


def word_lengths(input_string):
    """
    Find the length of each word in a string
    :param input_string: (string) given string
    :return: (dictionary) string and its length
    """
    return {word: len(word) for word in
            set(input_string.lower().strip(string.punctuation).split())}


def geometric_sum(n):
    """
    Compute geometric sum of the given number
    :param n: (number) given number
    :return: (number) geometric sum of integer n
    """
    return sum(1 / (2 ** x) for x in range(1, n + 1))


def most_words(*args):
    """
    Find the string with the most number of words
    :param args: (tuple) an arbitrary number of strings
    :return: (string) the string with the most number of words
    """
    return None if len(args) == 0 else max(args, key=lambda s: len(s.split()))


def coolest(cities, n=3) -> list:
    """
    Find n cities with lowest average temperatures
    :param cities: (dictionary) dictionary of arbitrary represent cities
    :param n: (number) requested number of cities defaults to 3
    :return: (list) list of n cities with lowest average temperature
    """
    return sorted(cities,
                  key=lambda name: sum(cities[name]) / len(cities[name]))[:n]


def secret(func):
    """
    Decorator to convert strings to uppercase in a secret language
    :param func: (function) function that uses the secret decorator
    :return: (function) the decorator function
    """
    vowel_list = list('AEIOU')

    def wrapper(first, *args):
        # Get the string return from the function using decorator
        input_str = func(first, *args).upper()
        # The list of words changed by the logic
        secret_list = [word + 'PIN' if word[0] in vowel_list
                       else word[1:] + word[0] + 'IP' for word in
                       input_str.split()]
        # Join all the words into a string
        secret_str = ' '.join(word for word in secret_list)
        return secret_str

    return wrapper


@secret
def greet(name):
    """
        Return a personalized hello message.
        :param name: (string)
        :return: (string)
        """
    return f'Hello {name}'


@secret
def repeat(phrase, n):
    """
        Repeat the specified string n times
        with a space character in between.
        :param phrase: (string)
        :param n: number of times the phrase will be repeated
        :return:
        """
    words = phrase.split()
    return ' '.join(n * words)


def main():
    print('Testing word_lengths function')
    phrase = '''Simple is better than     complex, and flat 
             IS BETTER than nested!?!'''
    print(word_lengths(phrase))
    print(word_lengths(''))
    print('Testing geometric_sum function')
    print(geometric_sum(-5))  # 0
    print(geometric_sum(0))  # 0
    print(geometric_sum(1))  # 0.5
    print(geometric_sum(2))  # 0.75
    print(geometric_sum(3))  # 0.875
    print(geometric_sum(4))  # 0.9375
    print(geometric_sum(30))  # 0.9999999990686774
    print('Testing most_words')
    print(most_words())
    print(most_words('pneumonoultramicroscopicsilicovolcanoconiosis',
                     'Go Spartans!', 'Are you     ready?'))
    norcal = {'Fresno': [77, 68, 80], 'Napa': [74, 89, 92, 55],
              'Palo Alto': [70, 78, 62], 'Sacramento': [75, 91, 92, 89],
              'San Francisco': [64, 59, 78], 'San Jose': [73, 85, 89],
              'Oakland': [67, 68, 61], 'Los Altos': [91, 58],
              'Mountain View': [72, 85, 90]}

    no_cities = {}

    print(coolest(no_cities, 100))  # []
    print(coolest(norcal))  # ['Oakland', 'San Francisco', 'Palo Alto']
    print(coolest(norcal,
                  5))  # ['Oakland', 'San Francisco',
    # 'Palo Alto', 'Los Altos', 'Fresno']
    print(coolest(norcal,
                  10))  # ['Oakland', 'San Francisco', 'Palo Alto',
    # 'Los Altos', 'Fresno', 'Napa', 'San Jose', 'Mountain View', 'Sacramento']
    print(norcal)  # unchanged
    print(no_cities)  # {}

    print(greet('Universe'))  # ELLOHIP UNIVERSEPIN
    print(repeat('Explicit is better than implicit',
                 2))  # EXPLICITPIN ISPIN ETTERBIP HANTIP IMPLICITPIN
    # EXPLICITPIN ISPIN ETTERBIP HANTIP IMPLICITPIN


if __name__ == '__main__':
    main()

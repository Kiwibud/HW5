# ---------------------------------------------------------------------
# Name: Homework 5
# Purpose:
# Author: Kiwibud
# ---------------------------------------------------------------------
"""
Docstring here
"""


# word_length(string): -> dictionary(string: len of string)
# single statement
def word_lengths(input_string):
    import string
    return {s: len(s) for s in
            set(input_string.lower().strip(string.punctuation).split())}


# Geometric_sum(integer n): ->sum
# using generator expression
def geometric_sum(n):
    return 0 if n <= 0 else sum(1 / (2 ** x) for x in range(1, n + 1))


# Most_words(number of string)
# using lambda expression
def most_words(*args):
    return None if len(args) == 0 else max(args, key=lambda s: len(s.split()))


# Not modify the original dictionary
# lambda expression
# Single statement
def coolest(cities, n=3) -> list:
    return sorted(cities,
                  key=lambda name: sum(cities[name]) / len(cities[name]))[:n]


def secret(func):
    def wrapper(first, *args):
        input_str = func(first, *args).upper()
        new_str = ''
        for i in input_str.split():
            if is_vowel(i[0]):
                new_str += i + 'PIN '
            else:
                new_str += i[1:] + i[0] + 'IP '
        return new_str
    return wrapper


def is_vowel(char):
    vowel_list = list('AEIOU')
    return True if char in vowel_list else False


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

# ----------------------------------------------------------------------
# Name:     HW5
# Purpose:  Applications of unpacking, and generator expression
#
# Author:   Kiwibud
# ----------------------------------------------------------------------
"""

"""
import string


def main():
    # Q1
    phrase = '''Simple is better than     complex, and flat 
                 IS BETTER than nested!?!'''
    print(word_lengths(''))
    print(word_lengths(phrase))
    # Q2
    print(geometric_sum(-5))  # 0
    print(geometric_sum(0))  # 0
    print(geometric_sum(1))  # 0.5
    print(geometric_sum(2))  # 0.75
    print(geometric_sum(3))  # 0.875
    print(geometric_sum(4))  # 0.9375
    print(geometric_sum(30))  # 0.9999999990686774
    # Q3
    # most_words()
    print(most_words('pneumonoultramicroscopicsilicovolcanoconiosis',

                     'Go Spartans!', 'Are you     ready?'))
    # Q4
    norcal = {'Fresno': [77, 68, 80], 'Napa': [74, 89, 92, 55],
              'Palo Alto': [70, 78, 62], 'Sacramento': [75, 91, 92, 89],
              'San Francisco': [64, 59, 78], 'San Jose': [73, 85, 89],
              'Oakland': [67, 68, 61], 'Los Altos': [91, 58],
              'Mountain View': [72, 85, 90]}

    no_cities = {}

    print(coolest(no_cities, 100))  # []
    print(coolest(norcal))  # ['Oakland', 'San Francisco', 'Palo Alto']
    print(coolest(norcal,
                  5))  # ['Oakland', 'San Francisco', 'Palo Alto', 'Los Altos', 'Fresno']
    print(coolest(norcal,
                  10))  # ['Oakland', 'San Francisco', 'Palo Alto', 'Los Altos', 'Fresno', 'Napa', 'San Jose', 'Mountain View', 'Sacramento']
    print(norcal)  # unchanged
    print(no_cities)  # {}
    # Q5
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

    print(greet('Universe')) # ELLOHIP UNIVERSEPIN
    print(repeat('Explicit is better than implicit', 2)) # EXPLICITPIN ISPIN ETTERBIP HANTIP IMPLICITPIN EXPLICITPIN ISPIN ETTERBIP HANTIP IMPLICITPIN


def word_lengths(phrase):
    words = {key.strip(string.punctuation): len(key.strip(string.punctuation))
             for key in phrase.lower().split()}
    return words


# generator expression.
def geometric_sum(n):
    result = sum((1 / 2) ** x for x in range(1, n + 1))
    return result


#  a single statement and uses a lambda expression
def most_words(*args):
    return max(args, key=lambda phrase: len(phrase.split()))


def coolest(cities, n=3) -> list:
    return sorted(cities, key=lambda x: sum(cities[x]) / len(cities[x]))[:n]


# built-in capabilities.
def secret(function):
    vowels = 'AEIOU'
    def wrapper(*args):

        result = function(*args)  # invoke the decorate function
        return result
    return wrapper

if __name__ == "__main__":
    main()

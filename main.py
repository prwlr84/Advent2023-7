from input import data
from collections import Counter


cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def sort_hand(hand):
    return ''.join(sorted(list(hand), key=lambda x: cards.index(x)))


def parse_input(string):
    string_list = string.split()
    return [[sort_hand(string_list[i]), int(string_list[i+1])] for i in range(0, len(string_list), 2)]


def score(hand):
    counter = Counter(hand)

    if 5 in counter.values():
        return 7
    elif 4 in counter.values():
        return 6
    elif 3 in counter.values() and 2 in counter.values():
        return 5
    elif 3 in counter.values():
        return 4
    elif 2 == list(counter.values()).count(2):
        return 3
    elif 2 in counter.values():
        return 2


def find_higher_card(first, second):
    if cards.index(first) == cards.index(second):
        return 'x'
    elif cards.index(first) < cards.index(second):
        return 1
    elif cards.index(first) > cards.index(second):
        return 2


def camel_poker(string):
    hands = parse_input(string)
    print([hand + [score(hand[0])] for hand in hands])


if __name__ == '__main__':
    camel_poker(data)

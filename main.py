from functools import cmp_to_key
from itertools import product
import re
from input import data
from collections import Counter


cards_1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def card_value(card, joker=False):
    if joker:
        return cards_2.index(card)
    else:
        return cards_1.index(card)


def custom_sort(item):
    primary = -item[2]
    secondary = tuple(card_value(char) for char in item[0] if char in cards_1)

    return tuple((primary, secondary))


def custom_sort_joker(item):
    primary = -item[2]
    secondary = tuple(card_value(char, True) for char in item[0] if char in cards_2)

    return tuple((primary, secondary))


def sort_hands(hands, joker=False):
    sort = custom_sort_joker if joker else custom_sort
    return sorted(list(hands), key=sort)


def parse_input(string):
    string_list = string.split()
    return [[string_list[i], int(string_list[i+1])] for i in range(0, len(string_list), 2)]


def score_card(hand):
    counter = Counter(hand)

    if 5 in counter.values():
        return 7
    elif 4 in counter.values():
        return 6
    elif 3 in counter.values() and 2 in counter.values():
        return 5
    elif 3 in counter.values():
        return 4
    elif list(counter.values()).count(2) == 2:
        return 3
    elif 2 in counter.values():
        return 2
    else:
        return 1


def use_joker(hand):
    if 'J' not in hand[0]:
        return hand + [score_card(hand[0])]

    score = score_card(hand[0])

    positions = [i for i, card in enumerate(hand[0]) if card == 'J']
    replacements = product(cards_2[:-1], repeat=len(positions))

    for replacement in replacements:
        new_hand = list(hand[0])
        for pos, rep in zip(positions, replacement):
            new_hand[pos] = rep
        new_string = ''.join(new_hand)
        if score_card(new_string) > score:
            score = score_card(new_string)

    return hand + [score]


def camel_poker_part_1(string):
    hands = parse_input(string)
    scored_hands = [hand + [score_card(hand[0])] for hand in hands]
    sorted_hands = sort_hands(scored_hands)
    positioned_hands = [hand + [len(sorted_hands) - i] for i, hand in enumerate(sorted_hands)]

    print(sum([hand[1] * hand[3] for hand in positioned_hands]))
    print(positioned_hands[::-1])


def camel_poker_part_2(string):
    hands = parse_input(string)
    scored_hands = [use_joker(hand) for hand in hands]
    sorted_hands = sort_hands(scored_hands, True)
    positioned_hands = [hand + [len(sorted_hands) - i] for i, hand in enumerate(sorted_hands)]

    print(sum([hand[1] * hand[3] for hand in positioned_hands]))
    print(positioned_hands)


if __name__ == '__main__':
    camel_poker_part_1(data)
    camel_poker_part_2(data)

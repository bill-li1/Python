import random
import math

def get_answer(player_hand, house_hand):
    house = calculate_hand_value(house_hand, True)
    if get_card_value(player_hand[0]) == get_card_value(player_hand[1]):
        pair = get_card_value(player_hand[0])
        if pair == 11 or pair == 8:
            return 4
        if pair == 9 and (house >= 2 and house <= 9 and house != 7):
            return 4
        if pair == 7 and (house >= 2 and house <= 7):
            return 4
        if pair == 6 and (house >= 2 and house <= 6):
            return 4
        if pair == 4 and (house == 5 or house == 6):
            return 4
        if pair == 3 and (house >= 2 and house <= 7):
            return 4
        if pair == 2 and (house >= 2 and house <= 7):
            return 4
    if player_hand[0] == "A" or player_hand[1] == "A":
        other = player_hand[0] if player_hand[0] != "A" else player_hand[1]
        if other == 9:
            return 1

    print("test")

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def create_deck(num_decks, shuffled):
    suits = ['S', 'H', 'C', 'D']
    suits = ['♠', '♥', '♣', '♦']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [value + suit for suit in suits for value in values] * num_decks
    if shuffled:
        return shuffle_deck(deck)
    return deck

def draw_card(deck):
    if deck:
        return deck.pop()
    else:
        return None

def get_card_value(card):
    value = card[:-1]
    if value in ["J", "Q", "K"]:
        return 10
    elif value == "A":
        return 11
    else:
        return int(value)

def calculate_hand_value(hand, hide_first = False):
    value = 0
    aces = 0
    for card in (hand[1:] if hide_first else hand):
        card_value = card[:-1]
        if card_value in ["J", "Q", "K"]:
            value += 10
        elif card_value == "A":
            aces += 1
        else:
            value += int(card_value)

    for _ in range(aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value

def generate_string_array(hand, skip_first = False):
    strings = []
    strings.append("*************")
    if skip_first:
        strings.append("*    XX     *")
    for card in (hand[1:] if skip_first else hand):
        str = "*    "
        str += card
        str += "    *" if len(card) == 3 else "     *"
        strings.append(str)
    strings.append("*************")
    return strings


def print_hands(player_hand, house_hand):
    player_hand_value = calculate_hand_value(player_hand)
    house_hand_value = calculate_hand_value(house_hand, True)
    player_strings = generate_string_array(player_hand)
    player_strings.insert(0, f"   YOU: {player_hand_value}" + ("   " if player_hand_value > 10 else "    "))
    house_strings = generate_string_array(house_hand, True)
    house_strings.insert(0, f"  HOUSE: {house_hand_value}")
    for i in range(max(len(player_strings), len(house_strings))):
        str = ""
        if i < len(player_strings):
            str += player_strings[i] + "   "
        if i < len(house_strings):
            str += house_strings[i]
        print(str)

def print_text(text):
    border = "*****************************"
    print(border)
    temp_string = "*"
    before_space = math.ceil((len(border) - 2 - len(text)) / 2)
    after_space = math.floor((len(border) - 2 - len(text)) / 2)
    for _ in range(before_space):
        temp_string += " "
    temp_string += text
    for _ in range(after_space):
        temp_string += " "
    temp_string += "*"
    print(temp_string)
    print(border)
    for _ in range(2):
        print("\n")

def get_input(hand):
    print("1. Hit")
    print("2. Stay")
    print("3. Double")
    if get_card_value(hand[0]) == get_card_value(hand[1]):
        print("4. Split")
    print("\n")
    while(True):
        user_action = input("Action: ")
        if(user_action.isdigit()):
            return int(user_action)

def black_jack():
    print("\n")
    while(True):
        deck = create_deck(1, True)
        player_hand = []
        house_hand = []
        for _ in range(2):
            player_hand.append(draw_card(deck))
            house_hand.append(draw_card(deck))
        print_hands(player_hand, house_hand)
        print("\n")
        user_action = get_input(player_hand)
        if user_action == 1:
            print_text("STAND")
        elif user_action == 2:
            print_text("STAY")
        elif user_action == 3:
            print_text("DOUBLE")
        elif user_action == 4:
            print_text("SPLIT")
        print_hands(player_hand, house_hand)

black_jack()



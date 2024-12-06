# Creating a Blackjack game

import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def computer_play(computer_hand):
    while calculate_score(computer_hand) < 16:
        computer_hand.append(draw_card())
    return computer_hand


def determine_winner(player_score, computer_score):
    if player_score == 21:
        return "Blackjack! You win!"
    elif player_score > 21:
        return "You went over. You lose :("
    elif computer_score > 21:
        return "The computer went over. You win!"
    elif player_score > computer_score:
        return "You win!"
    elif player_score < computer_score:
        return "You lose!"
    else:
        return "It's a tie!"


def play_blackjack():
    print(logo)
    player_hand = [draw_card(), draw_card()]
    computer_hand = [draw_card()]

    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {computer_hand[0]}")

    if player_score == 21:
        print("Blackjack! You win!")
        return

    game_over = False
    while not game_over:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            player_hand.append(draw_card())
            player_score = calculate_score(player_hand)
            print(f"Your cards: {player_hand}, current score: {player_score}")
            if player_score > 21:
                game_over = True
        else:
            game_over = True

    computer_hand = computer_play(computer_hand)
    computer_score = calculate_score(computer_hand)
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(determine_winner(player_score, computer_score))


def initialize_game():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == "y":
        play_blackjack()
    elif start == "n":
        print("Goodbye!")
    else:
        print("Invalid input. Please restart the game.")


initialize_game()

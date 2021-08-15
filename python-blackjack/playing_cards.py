#!/usr/bin/env python3

from enum import Enum
from enum import IntEnum
from random import *
import time

full_deck = []
partial_deck = []
player1_cards = []
player2_cards = []
player1_wins = 0
player2_wins = 0
war_count = 0

class Card(IntEnum):

  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8
  NINE = 9
  TEN = 10
  JACK = 11
  QUEEN = 12
  KING = 13
  ACE = 1

class Suit(Enum):
  CLUBS = 'clubs'
  HEARTS = 'hearts'
  SPADES = 'spades'
  DIAMONDS = 'diamonds'

class PlayingCard:
  def __init__(self, card_value, card_suit):
    self.card = card_value
    self.suit = card_suit

def Create_deck():
  for suit in Suit:
    for card in Card:
      full_deck.append(PlayingCard(Card(card), Suit(suit)))
  return full_deck

def draw_card(deck):
  rand_card = randint(0, len(deck) -1)
  return deck.pop(rand_card)

def deal_war():
  while(len(partial_deck) > 0):
    player1_cards.append(draw_card(partial_deck))
    player2_cards.append(draw_card(partial_deck))

Create_deck()
partial_deck = list(full_deck)
deal_war()

for i in range(0, len(player1_cards)):
  if (player1_cards[i].card > player2_cards[i].card):
    player1_wins += 1
    print("Player 1 wins the hand with: ", player1_cards[i].card, player1_cards[i].suit)
    print("Player 2 loses the hand with: ", player2_cards[i].card, player2_cards[i].suit)
    print("Player 1 wins = ", player1_wins, "vs Player 2 wins = ", player2_wins)
    time.sleep(0.2)
  if (player1_cards[i].card < player2_cards[i].card):
    player2_wins += 1
    print("Player 1 the loses hand with: ", player1_cards[i].card, player1_cards[i].suit)
    print("Player 2 wins the hand with: ", player2_cards[i].card, player2_cards[i].suit)
    print("Player 2 wins = ", player2_wins, "vs Player 1 wins = ", player1_wins)
    time.sleep(0.2)
  else:
    war_count += 1
    print("WAR", war_count)
    time.sleep(0.4)

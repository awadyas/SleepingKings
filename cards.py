"""
Cards
by Yasmeen Awad
3/13/18

This module contains classes of objects containing and relating to the cards used in the 
game Sleeping Kings.
"""

import random
from graphics import Point

class Card:
    """The class for cards. itype is a string. If the card is a King, ivalue signifies its point 
    value. Otherwise ivalue will be None."""
    
    def __init__(self, itype, ivalue):
        self.type = itype
        self.value = ivalue
    
    
    """Returns the type of the card (a string)"""
    def getType(self):
        return self.type
    
    
    """Returns the value of the card (an integer)"""
    def getValue(self):
        return self.value

    
class Deck:
    """Includes all cards in the deck besides Kings"""
    
    def __init__(self):
        self.cards = []
        
        # Adds 8 Queens, 4 Dragons, and 12 Cow cards to the Deck
        for i in range(8):
            self.cards.append(Card("queen", None))
        for j in range(4):
            self.cards.append(Card("dragon", None))
        for k in range(8):
            self.cards.append(Card("cow", None))
            
            
    """Adds the inputted card to the deck"""
    def addCard(self, card):
        self.cards.append(card)
        
        
    """Randomly selects a card from the deck and returns it"""
    def removeCard(self):
        idx = random.randint(1, len(self.cards) - 1)
        rand_card = self.cards[idx]
        return rand_card
    
    
class KingDeck:
    """Contains all of the King cards and will be spread in an array in the center of interface"""
    
    def __init__(self):
        self.kings = []
        
        # Adds 2 Kings with 5 points, 2 with 10 points, 3 with 15 points, and 1 with 20 points
        for i in range(2):
            self.kings.append(Card("king", 5))
            self.kings.append(Card("king", 10))
        for j in range(3):
            self.kings.append(Card("king", 15))
        self.kings.append(Card("king", 20))
    
    
    """Uses a given index (idx) to allow player to "draw" their chosen King, returns the King card"""
    def removeKing(self, idx):
        # Get card at specified index and replace it with None
        card, self.kings[idx] = self.kings[idx], None
        return card
    
    
    """This strategy function returns the center point of the first King that still exists the King
    Deck. Since the King Deck is shuffled each game, there is no way for the computer to really
    make a more intelligent decision because there is no way for the computer to know where the 
    highest value King is.""" 
    def computerGetKing(self):
        # Loop through the list of kings to find one that exists
        for idx in range(len(self.kings)):
            # Once it finds one that exists, it will return
            if self.kings[idx] != None:
                if idx == 0:
                    return Point(20, 43)
                elif idx == 1:
                    return Point(29, 43)
                elif idx == 2:
                    return Point(51, 43)
                elif idx == 3:
                    return Point(60, 43)
                elif idx == 4:
                    return Point(20, 32)
                elif idx == 5:
                    return Point(29, 32)
                elif idx == 6:
                    return Point(51, 32)
                else:
                    return Point(60, 32)
    
    
    """This function randomly orders the list of kings. This function is only really needed in the 
    King Deck (rather than in Deck) because in Deck, the order of cards doesn't matter, as they are
    randomly selected when drawn. In the King Deck, the order matters, so a shuffle function is 
    needed."""
    def shuffle(self):
        new_kings = []
        # Randomly generates indecies from the list of kings and adds them to a new, random list,
        # then removes them from the list of kings
        for i in range(len(self.kings)):
            idx = random.randint(0, len(self.kings) - 1)
            new_kings.append(self.kings[idx])
            del self.kings[idx]
        # Restores the list to its location as an attribute of the class
        self.kings = new_kings
        

class Hand:
    """Contains all of the cards that a player currently has access to, including their kings"""
    
    def __init__(self):
        self.cards = []
    
    
    """Returns a list of all the cards of type King in the user's hand"""
    def getKings(self):
        kings = []
        for card in self.cards:
            card_type = card.getType()
            if card_type == "king":
                kings.append(card)
        return kings        
    
    
    """Returns a list of all non-King cards"""
    def getCards(self):
        cards = []
        for card in self.cards:
            card_type = card.getType()
            if card_type != "king":
                cards.append(card)
        return cards
    
    
    """Deletes the inputted card from the hand"""
    def removeCard(self, card):
        idx = self.cards.index(card)
        del self.cards[idx]
        
        
    """Appends the inputted card to the hand"""
    def addCard(self, card):
        self.cards.append(card)
        
        
    """A function used for computer intelligence only which returns the first instance of a certain
    type of card (inputted as a string, card_type) in the computer's hand. If none of that type 
    exist in the hand, it returns None."""
    def computerCheck(self, card_type):
        # card_type should be a string.
        for card in self.cards:
            type = card.getType()
            if type == card_type:
                return card
        return None
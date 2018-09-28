"""
Sleeping Kings
by Yasmeen Awad
3/13/18

The functions for a simulation based on the card game Sleeping Queens.
"""

import cards
import game_board
import graphics

class Game:
    """The class Game sets up the Sleeping Queens game and allows users to interact with it"""
    
    def __init__(self):
        self.board = game_board.Interface()
        self.win = self.board.getWindow()
        self.deck = cards.Deck()
        self.king_deck = cards.KingDeck()
        self.king_deck.shuffle()
        self.user_hand = cards.Hand()
        self.computer_hand = cards.Hand()
        
        
    """This function "plays" a Queen by allowing player to obtain a King."""
    def playQueen(self, queen_card, hand):
        # If the computer is playing a Queen, use stragety function to choose which King it draws
        if hand == self.computer_hand:
            click = self.king_deck.computerGetKing()
        # Otherwise prompt user to pick a King to draw
        else:
            self.board.showMessage("Click on a King \nto awaken it!")
            # Get user's mouse click
            click =  self.win.getMouse()
        x = click.getX()
        y = click.getY()
        # Make sure that click was in a valid area, and if not, allow user to click again
        while x < 15 or x > 65 or y < 26 or y > 49:
            self.board.showMessage("ERROR: Click invalid. \nClick on a King \nto awaken it!")
            click = self.win.getMouse()
            x = click.getX()
            y = click.getY()
        # Determine which King was chosen and "undraw" King on the board
        if x > 15 and x < 25 and y > 37 and y < 49:
            idx = 0
            self.board.undrawCard(20, 43)
        elif x > 24 and x < 34 and y > 37 and y < 49:
            idx = 1
            self.board.undrawCard(29, 43)
        elif x > 46 and x < 56 and y > 37 and y < 49:
            idx = 2
            self.board.undrawCard(51, 43)
        elif x > 55 and x < 65 and y > 37 and y < 49:
            idx = 3
            self.board.undrawCard(60, 43)
        elif x > 15 and x < 25 and y > 26 and y < 38:
            idx = 4
            self.board.undrawCard(20, 32)
        elif x > 24 and x < 34 and y > 26 and y < 38:
            idx = 5
            self.board.undrawCard(29, 32)
        elif x > 46 and x < 56 and y > 26 and y < 38:
            idx = 6
            self.board.undrawCard(51, 32)
        else:
            idx = 7
            self.board.undrawCard(60, 32)
        # Remove king from King Deck
        card = self.king_deck.removeKing(idx)
        # Append king to hand
        hand.addCard(card)
        self.board.showUserKings(self.user_hand)
        self.board.showComputerKings(self.computer_hand)
        # Transfer card from hand to deck
        hand.removeCard(queen_card)
        self.deck.addCard(queen_card)

        
    """This function "plays" a Dragon by allowing player to steal a King from their opponent."""
    def playDragon(self, dragon_card, hand, opponent_hand):
        # The Dragon is powerless if the opponent doesn't have any kings
        if opponent_hand.getKings() != []:
            # If the computer is playing, use strategy function to have the computer choose the
            # king with the highest value to steal
            if hand == self.computer_hand:
                x = self.computerStealKing(self.user_hand.getKings())
            # Otherwise prompt user to select a King to steal
            else:
                self.board.showMessage("Click on an \nopponent's king \n to steal!")
                # Get which king they want to steal
                click = self.win.getMouse()
                x = click.getX()
            if x > 30 and x < 40:
                idx = 0
                self.board.undrawCard(35, 55)
            elif x > 40 and x < 50:
                idx = 1
                self.board.undrawCard(45, 55)
            elif x > 50 and x < 60:
                idx = 2
                self.board.undrawCard(55, 55)
            elif x > 20 and x < 30:
                idx = 3
                self.board.undrawCard(25, 55)
            elif x > 60 and x < 70:
                idx = 4
                self.board.undrawCard(65, 55)
            elif x > 10 and x < 20:
                idx = 5
                self.board.undrawCard(15, 55)
            elif x > 70 and x < 80:
                idx = 6
                self.board.undrawCard(75, 55)
            elif x < 10 and x > 1:
                idx = 7
                self.board.undrawCard(5, 55)
            # Based on the click, determine which King to remove and remove it from the hand
            king = opponent_hand.getKings()[idx]
            opponent_hand.removeCard(king)
            # Add the king to hand and update interface
            hand.addCard(king)
            self.board.showUserKings(self.user_hand)
            self.board.showComputerKings(self.computer_hand)
        # Transfer card from hand to deck
        hand.removeCard(dragon_card)
        self.deck.addCard(dragon_card)


    """This function "plays" the inputted card by allowing player to remove it from the hand"""
    def playCow(self, cow_card, hand):
        # Transfer card from hand to deck
        hand.removeCard(cow_card)
        self.deck.addCard(cow_card)

        
    """This function transfers four cards from the deck to the inputted hand"""
    def deal(self, hand):
        for i in range(4):
            card = self.deck.removeCard()
            hand.addCard(card)

            
    """This function allows the user to take a turn"""
    def userTurn(self):
        # Prompt user to pick a card
        self.board.showMessage("Choose one of your \ncards to play.")
        click = self.win.getMouse()
        x = click.getX()
        y = click.getY()
        # Get a list of the cards that exist in the hand
        cards = self.user_hand.getCards()
        # Make sure that the click was valid, and if not, continue to prompt user to click
        while x > 60 or x < 20 or y > 10:
            self.board.showMessage("ERROR: Click invalid. \nChoose one of your \n cards to play.")
            click = self.win.getMouse()
            x = click.getX()
            y = click.getY()
        # Determine which card the user clicked on and "undraw" it on the interface
        if x > 20 and x < 30 and y < 10:
            chosen_card = cards[0]
            self.board.undrawCard(25, 6)
        elif x > 30 and x < 40 and y < 10:
            chosen_card = cards[1]
            self.board.undrawCard(35, 6)
        elif x > 40 and x < 50 and y < 10:
            chosen_card = cards[2]
            self.board.undrawCard(45, 6)
        elif x > 50 and x < 60 and y < 10:
            chosen_card = cards[3]
            self.board.undrawCard(55, 6)

        card_type = chosen_card.getType()

        # Determine the type of card and play accordingly
        if card_type == "queen":
            self.playQueen(chosen_card, self.user_hand)
            # Check to see if there are any Kings left in center, and if not, return
            if len(self.user_hand.getKings() + self.computer_hand.getKings()) >= 8:
                return
        elif card_type == "dragon":
            self.playDragon(chosen_card, self.user_hand, self.computer_hand)
        else:
            self.playCow(chosen_card, self.user_hand)
        # Prompt user to draw a new card
        self.board.showMessage("Click on the deck \nto draw a new card")
        self.win.getMouse()
        # Add new card to user's hand
        self.user_hand.addCard(self.deck.removeCard())
        self.board.showUserCards(self.user_hand)
        # Prompt user to continue
        self.board.showMessage("Click anywhere to \ncontinue to \nthe Computer's turn")
        self.win.getMouse()

        
    """Allows computer to take a turn"""
    def computerTurn(self):
        # Uses computer intelligence to optimize gain for the given cards

        # First priority is to play a queen, if there is one in the computer's hand
        card = self.computer_hand.computerCheck("queen")
        if card != None:
            self.playQueen(card, self.computer_hand)
            
        # Second priority is to play a Dragon, but only if the user has a King
        else:
            card = self.computer_hand.computerCheck("dragon")
            if self.user_hand.getKings() != [] and card != None:
                self.playDragon(card, self.computer_hand, self.user_hand)
            
            # Playing a Cow would be the next best option
            else:
                card = self.computer_hand.computerCheck("cow")
                if card != None:
                    self.playCow(card, self.computer_hand)
                
                # Worst case scenario: computer plays a Dragon and is unable to steal a king
                else:
                    card = self.computer_hand.computerCheck("dragon")
                    self.playDragon(card, self.computer_hand, self.user_hand)
            
        # Computer draws a new card
        new_card = self.deck.removeCard()
        self.computer_hand.addCard(new_card)
        
        # Update the user on what the computer did during its turn
        self.board.showMessage("The Computer played \na " + str(card.getType()) + ". Click \n" +
                              "anywhere to continue.")
        self.win.getMouse()
    
    
    """For an inputted list of kings, this function totals their values and returns the total"""
    def getTotal(self, king_list):
        total = 0
        for king in king_list:
            value = king.getValue()
            total += value
        return total
    
    
    """Examines inputted king list and determines which one has the highest point value and returns
    a number which corresponds to the index of that card (see playDragon function)"""
    def computerStealKing(self, user_king_list):
        # Function is only called in instances in which there are Kings in the user's king list
        
        # Loop through list and to get the index of the King with the highest value
        high_idx = 0
        for idx in range(1, len(user_king_list) - 1):
            if user_king_list[idx].getValue() > user_king_list[high_idx].getValue():
                high_idx = idx
        # Correspond the index of the high-value king with it's x-position on the interface
        if high_idx <= 2:
            x = (high_idx + 1)*10 + 25
        elif high_idx == 3:
            x = 25
        elif high_idx == 4:
            x = 65
        elif high_idx == 5:
            x = 15
        elif high_idx == 6:
            x = 75
        elif high_idx == 7:
            x = 5
        return x
    
    
    """Brings everything together and allows user to actually play the game"""
    def playGame(self):
        # Starts up the welcome interface with instructions, etc.
        welcome = game_board.WelcomeInterface()
        welcome.welcome()
        welcome.close()
        
        # Sets up the board - dealing cards, displaying them to the interface
        self.deal(self.user_hand)
        self.deal(self.computer_hand)
        self.board.showUserCards(self.user_hand)
        
        # Loops the game while there are still Kings in the center of the board
        x = 0
        while x < 8:
            self.userTurn()
            x = len(self.user_hand.getKings() + self.computer_hand.getKings())
            # Checks again if there are still Kings in the center of the board
            if x < 8:
                self.computerTurn()
                x = len(self.user_hand.getKings() + self.computer_hand.getKings())
        
        # Computes who has won the game and displays accordingly
        user_total = self.getTotal(self.user_hand.getKings())
        computer_total = self.getTotal(self.computer_hand.getKings())
        if user_total > computer_total:
            self.board.showMessage("YOU WIN!!! \nCONGRATULATIONS! \n(click to exit)")
        elif computer_total > user_total:
            self.board.showMessage("Computer Wins!! \nBetter luck next time! \n(click to exit)")
        elif computer_total == user_total:
            self.board.showMessage("IT'S A TIE!! \n(click to exit)")
        self.win.getMouse()

        
"""Main function creates an instance of the game and plays it"""
def main():
    g = Game()
    g.playGame()
    
    
if __name__ == '__main__':
    main()
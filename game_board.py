"""
Game Board
by Yasmeen Awad
3/13/18

This module contains functions that create interfaces for the game Sleeping Kings.
"""

import graphics

class Interface:
    """The graphical interface for Sleeping Kings"""
    
    def __init__(self):
        # Set up window
        self.win = graphics.GraphWin("Sleeping Kings", 800, 600)
        self.win.setCoords(0, 0, 80, 60)
        self.win.setBackground(graphics.color_rgb(86, 114, 144))
        
        # Set up king cards and deck
        self.king0 = graphics.Rectangle(graphics.Point(16, 38), graphics.Point(24, 48))
        self.king0.setFill(graphics.color_rgb(0, 93, 115))
        self.king0.draw(self.win)
        self.king1 = graphics.Rectangle(graphics.Point(25, 38), graphics.Point(33, 48))
        self.king1.setFill(graphics.color_rgb(0, 93, 115))
        self.king1.draw(self.win)
        self.king2 = graphics.Rectangle(graphics.Point(47, 38), graphics.Point(55, 48))
        self.king2.setFill(graphics.color_rgb(0, 93, 115))
        self.king2.draw(self.win)
        self.king3 = graphics.Rectangle(graphics.Point(56, 38), graphics.Point(64, 48))
        self.king3.setFill(graphics.color_rgb(0, 93, 115))
        self.king3.draw(self.win)
        self.king4 = graphics.Rectangle(graphics.Point(16, 27), graphics.Point(24, 37))
        self.king4.setFill(graphics.color_rgb(0, 93, 115))
        self.king4.draw(self.win)
        self.king5 = graphics.Rectangle(graphics.Point(25, 27), graphics.Point(33, 37))
        self.king5.setFill(graphics.color_rgb(0, 93, 115))
        self.king5.draw(self.win)
        self.king6 = graphics.Rectangle(graphics.Point(47, 27), graphics.Point(55, 37))
        self.king6.setFill(graphics.color_rgb(0, 93, 115))
        self.king6.draw(self.win)
        self.king7 = graphics.Rectangle(graphics.Point(56, 27), graphics.Point(64, 37))
        self.king7.setFill(graphics.color_rgb(0, 93, 115))
        self.king7.draw(self.win)
        self.deck = graphics.Rectangle(graphics.Point(35, 34), graphics.Point(45, 42))
        self.deck.setFill(graphics.color_rgb(100, 40, 64))
        self.deck.draw(self.win)
        self.deck_text = graphics.Text(graphics.Point(40, 38), "DECK")
        self.deck_text.setSize(24)
        self.deck_text.setFill("white")
        self.deck_text.setFace("helvetica")
        self.deck_text.draw(self.win)
        
        # Create divider
        self.divider = graphics.Rectangle(graphics.Point(1, 13), graphics.Point(79, 14))
        self.divider.setFill("gray")
        self.divider.draw(self.win)
        self.divider_text = graphics.Text(graphics.Point(10, 6), "Your cards:")
        self.divider_text.setStyle("bold")
        self.divider_text.setFill("white")
        self.divider_text.draw(self.win)
        
        # Write "king" on each of the King cards
        self.t1 = graphics.Text(graphics.Point(20, 45), "King")
        self.t1.draw(self.win)
        self.t2 = graphics.Text(graphics.Point(29, 45), "King")
        self.t2.draw(self.win)
        self.t3 = graphics.Text(graphics.Point(51, 45), "King")
        self.t3.draw(self.win)
        self.t4 = graphics.Text(graphics.Point(60, 45), "King")
        self.t4.draw(self.win)
        self.t5 = graphics.Text(graphics.Point(20, 34), "King")
        self.t5.draw(self.win)
        self.t6 = graphics.Text(graphics.Point(29, 34), "King")
        self.t6.draw(self.win)
        self.t7 = graphics.Text(graphics.Point(51, 34), "King")
        self.t7.draw(self.win)
        self.t8 = graphics.Text(graphics.Point(60, 34), "King")
        self.t8.draw(self.win)
        
        # Create a reminder box with the functions of each card written out
        self.box = graphics.Rectangle(graphics.Point(1, 33), graphics.Point(15, 47))
        self.box.setFill(graphics.color_rgb(154, 154, 154))
        self.box.draw(self.win)
        self.box_text = graphics.Text(graphics.Point(8, 40), "Remember... \n\n\nQUEENS...wake up"
                                      + "Kings \n\nDRAGONS...steal Kings \n\nCOWS...do nothing")
        self.box_text.setFill("black")
        self.box_text.draw(self.win)
        
        # Create text that says "Prompt:"
        self.prompt = graphics.Text(graphics.Point(72, 43), "Prompt:")
        self.prompt.draw(self.win)
        
        
    """Returns the window of the interface"""
    def getWindow(self):
        return self.win
        
        
    """Makes a card centered at (x, y) appear to be "undrawn" by putting a blue box over it"""
    def undrawCard(self, x, y):
        graphics.Image(graphics.Point(x, y), "blue.gif").draw(self.win)
    
    
    """Makes an image of a "card_type" type of card appear, centered at (x, y)"""
    def showCard(self, x, y, card_type):
        if card_type == "queen":
            graphics.Image(graphics.Point(x, y), "queen.gif").draw(self.win)
        elif card_type == "dragon":
            graphics.Image(graphics.Point(x, y), "dragon.gif").draw(self.win)
        else:
            graphics.Image(graphics.Point(x, y), "cow.gif").draw(self.win)
        
        
    """Makes an image of a King card of point value "value" appear on the interface, centered 
    at (x, y)"""
    def showKing(self, x, y, value):
        graphics.Image(graphics.Point(x, y), str(value) + "king.gif").draw(self.win)
        
        
    """Makes a message with containg the string "words" appear on the interface in a gray box to 
    the right of the cards on the board"""
    def showMessage(self, words):
        box = graphics.Rectangle(graphics.Point(66, 36), graphics.Point(78, 42))
        box.setFill("gray")
        box.draw(self.win)
        m = graphics.Text(graphics.Point(72, 39), words)
        m.setFill("white")
        m.draw(self.win)
        
        
    """Makes user's Kings appear on the interface by covering up the Kings that are already existed
    on the interface with a blue box and drawing the Kings that currently exist in their place. 
    Takes parameter user_hand which should be an object of type Hand representing the user"""
    def showUserKings(self, user_hand):
        # Clear out any remaining kings with a blue rectangle
        cover = graphics.Image(graphics.Point(40, 20), "long.gif")
        cover.draw(self.win)
        # Display the user's kings below main cards
        user_kings = user_hand.getKings()
        if len(user_kings) >= 1:
            self.showKing(35, 20, user_kings[0].getValue())
        if len(user_kings) >= 2:
            self.showKing(45, 20, user_kings[1].getValue())
        if len(user_kings) >= 3:
            self.showKing(55, 20, user_kings[2].getValue())
        if len(user_kings) >= 4:
            self.showKing(25, 20, user_kings[3].getValue())
        if len(user_kings) >= 5:
            self.showKing(65, 20, user_kings[4].getValue())
        if len(user_kings) >= 6:
            self.showKing(15, 20, user_kings[5].getValue())
        if len(user_kings) >= 7:
            self.showKing(75, 20, user_kings[6].getValue())
        if len(user_kings) >= 8:
            self.showKing(5, 20, user_kings[7].getValue())
          
        
    """Makes computer's Kings appear on the interface by covering up Kings that already existed on
    the interface with a blue box and drawing the Kings that currently exist in their place. Takes
    parameter computer_hand which should be an object of type Hand representing the computer"""
    def showComputerKings(self, computer_hand):
        # Clear out any remaining kings with a blue rectangle
        cover = graphics.Image(graphics.Point(40, 55), "long.gif")
        cover.draw(self.win)
        # Display computer's kings above main cards
        comp_kings = computer_hand.getKings()
        if len(comp_kings) >= 1:
            self.showKing(35, 55, comp_kings[0].getValue())
        if len(comp_kings) >= 2:
            self.showKing(45, 55, comp_kings[1].getValue())
        if len(comp_kings) >= 3:
            self.showKing(55, 55, comp_kings[2].getValue())
        if len(comp_kings) >= 4:
            self.showKing(25, 55, comp_kings[3].getValue())
        if len(comp_kings) >= 5:
            self.showKing(65, 55, comp_kings[4].getValue())
        if len(comp_kings) >= 6:
            self.showKing(15, 55, comp_kings[5].getValue())
        if len(comp_kings) >= 7:
            self.showKing(75, 55, comp_kings[6].getValue())
        if len(comp_kings) >= 8:
            self.showKing(5, 55, comp_kings[7].getValue())
        
        
    """Makes user's cards appear on the interface"""
    def showUserCards(self, user_hand):
        # Clear out previous cards with a blue rectangle
        cover = graphics.Image(graphics.Point(40, 6), "cropped.gif")
        cover.draw(self.win)
        # Display the user's cards to user
        user_cards = user_hand.getCards()
        self.showCard(25, 6, user_cards[0].getType())
        self.showCard(35, 6, user_cards[1].getType())
        self.showCard(45, 6, user_cards[2].getType())
        self.showCard(55, 6, user_cards[3].getType())
        
        
    """Closes the window of the interface"""
    def close(self):
        self.win.close()
        
        
class WelcomeInterface:
    """Initial interface that greets users and explains instructions of Sleeping Queens"""
    
    def __init__(self):
        self.win = graphics.GraphWin("Welcome to Sleeping Kings!", 500, 500)
        self.win.setBackground(graphics.color_rgb(100, 0, 100))
        
        
    """Welcomes the user with various text-based instructions, allows user to click through"""
    def welcome(self):
        # First message
        self.t1 = graphics.Text(graphics.Point(250, 250), "Welcome to Sleeping Kings! \n\n(Click "
                                + "anywhere to continue)")
        self.t1.setFill("white")
        self.t1.setSize(36)
        self.t1.draw(self.win)
        self.win.getMouse()
        self.t1.undraw()
        
        # Second message
        self.t2 = graphics.Text(graphics.Point(250, 265), "INSTRUCTIONS: \n\n\n\n\nQUEENS can " +
                                "awaken KINGS\n\n\nDRAGONS let you steal your opponent's KINGS \n"
                                + "\n\nCOWS...have no power :( \n\n (just follow the prompts!)\n"
                                + "\n\n\n\n(Click to continue)")
        self.t2.setFill("white")
        self.t2.setSize(17)
        self.t2.draw(self.win)
        self.queen = graphics.Image(graphics.Point(140, 120), "queen.gif")
        self.queen.draw(self.win)
        self.dragon = graphics.Image(graphics.Point(60, 180), "dragon.gif")
        self.dragon.draw(self.win)
        self.cow = graphics.Image(graphics.Point(105, 325), "cow.gif")
        self.cow.draw(self.win)
        self.win.getMouse()
        self.t2.undraw()
        self.queen.undraw()
        self.dragon.undraw()
        self.cow.undraw()
        
        # Third message
        self.t3 = graphics.Text(graphics.Point(250, 250), "Kings give you points. Once all the "
                               + "Kings are \nremoved from the center, the game is over \nand the "
                               + "player with the most points wins!! \n\n Good Luck! \n\n (Click"
                               + " anywhere to play)")
        self.t3.setSize(22)
        self.t3.setFill("white")
        self.t3.draw(self.win)
        self.win.getMouse()
    
    
    """Closes window of the interface"""
    def close(self):
        self.win.close()
        
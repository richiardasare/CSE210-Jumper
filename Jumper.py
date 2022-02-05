import string

class Director: 
    '''Class that directs the game. Initiates game play
    and makes it flow the way it should.'''
    def __init__(self):
        self.is_playing = True
        self._word = Word()
        self._guesser = Guesser()
        self._terminal_service = TerminalService()

    def start_game(self):
        '''During game play the director does inputs, updates, and outputs.'''
        while self.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        '''Reads letter.'''
        new_letter = self._terminal_service.read_letter("/nGuess a letter [a-z]: ")
        '''What here?'''
    
    def _do_updates(self):
        '''Keeps track of guesses'''
        
    def _do_outputs(self):
        hint = self._word.letter_check



class Word:

    def __init__(self):
        pass

    
    def letter_check(self):
        '''Compares letter guess to random word.'''
        pass

class Guesser:
    def __init__():
        pass

class GameBoard:
    def __init__():
        pass

class TerminalService():
    def __init__():
        pass


class WordArray:
    def __init__(self):

    def Array():
        self.array = ["Hello", "Shire", "Bring", "Acorn", "Please", "Close", "Front", "Frame", "Zebra", "Libra", "Speed", "Creed", "Anime", "Silly", "Smart", "Crazy", "Learn", "Stern", "Koala", "Brand", "Stand",  "Happy", "Style", "Miles", "Arrow", "Drama", "Allow", "Apply", "Child", "Crime", "Dress", "Dream", "Drink", "Enemy", "Entry", "Focus", "Fruit", "Glass", "Green", "Group", "Heart", "Guide", "Jones", "Judge", "Knife", "Layer", "March", "Major", "Metal", "Money", "Month", "Motor", "Music", "Panel", "Owner", "North", "Night", "Plane", "Plant", "Point", "Power", "Reply", "River", "Round", "Route", "Rugby", "Scale", "Scene", "Shape", "Smoke", "Sound", "South", "Space", "Sport", "Stock"]

    
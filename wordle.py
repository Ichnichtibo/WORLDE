from letter_state import LetterState


class Wordle():
    
    MAX_ATTEMPTS = 6
    WORD_LENGHT = 5

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attemps = []

    def attempt(self, word:str):
        self.attemps.append(word)
        
    def guess(self, word: str):
        word = word.upper()
        result = []
        
        for i in range(self.WORD_LENGHT):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character in self.secret[i]
            result.append(letter)
        return result


    @property
    def is_Solved(self):
        return len(self.attemps) > 0 and self.attemps[-1] == self.secret

    @property
    def remaining_attemps(self):
        return self.MAX_ATTEMPTS - len(self.attemps)

    @property
    def can_attempt(self):
        return self.remaining_attemps > 0 and not self.is_Solved
       
    
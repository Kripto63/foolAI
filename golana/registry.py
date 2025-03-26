from .word import WORD

class REGISTRY():
    
    def __init__(self):
        self.registry = []

    def add_element(self, word, link_before, link_after):
        new_word = WORD(word, link_before=link_before, 
             link_after=link_after)
        self.registry.append(new_word)

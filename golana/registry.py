from .word import WORD

class REGISTRY():
    
    def __init__(self):
        self.registry = [] 
        ouroboros = WORD('.', 
                         link_after=self.pointer, link_before=self.pointer)
        self.registry.append(ouroboros)

    def add_element(self, word):
        new_word = WORD(word, link_before=self.pointer, 
             link_after=self.__ouroboros)
        self.pointer.link_after = new_word
        self.pointer = new_word
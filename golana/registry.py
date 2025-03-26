from .word import WORD

class REGISTRY():
    def __init__(self):
        self.registry = []
        
    def add_element(self, word, link):
        element = WORD(word, link)
        self.registry.append(element)
        return element

    def get_registry(self):
        return self.registry

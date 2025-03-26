from .registry import REGISTRY

class QUEUE():
    
    def __init__(self):
        self.registry = REGISTRY()
        ouroboros = self.registry.add_element(word=".", link_before=self.registry, link_after=self.registry)

    def get_element(self):
        return self.registry.registry
    
    def get_link(self):
        return self.registry.registry[0].link
    
    def add_element(self, new_word):
        for i in self.get_element():
            if i.word == new_word and i.word != '.':
                break
        new_registry = REGISTRY()
        self.registry.registry.word
        new_registry.add_element(word=new_word,
                                 link_after=self.registry, link_before=new_registry)
        self.registry = new_registry
        
        
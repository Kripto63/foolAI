from .word import WORD, OUROBOROS

class QUEUE():
    
    def __init__(self):
        ouroboros = OUROBOROS('.')
        self.__ouroboros = ouroboros
        self.pointer = ouroboros

    def get_pointer(self):
        return self.pointer.word
    
    def move_ouroboros(self):
        self.pointer = self.__ouroboros
        
    def next_element(self):
        self.pointer = self.pointer.link_after
        
    def add_line(self, line) -> str:
        self.move_ouroboros()
        for word in line.split():
            self.add_element(word=word)
        
        self.move_ouroboros()
        
        return "add line"  
        
        
class OUROBOROS():
    def __init__(self, word):
        
        self.word = word
        self.link = self
        self.link_after = self
        self.link_before = self
        

class WORD():

    def __init__(self, word, 
                 link_after, link_before):
        self.word = word
        self.link = self
        self.link_after = link_after
        self.link_before = link_before
        
    def get_word(self):
        return self.word
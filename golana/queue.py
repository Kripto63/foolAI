from .registry import REGISTRY


class QUEUE():    
    def __init__(self):
        self.registry = REGISTRY()
        self.__ouroboros = self.__add_element_ouroboros(new_word="(*_*)", new_link=self.registry)
        self.pointer = self.registry
        
    def __add_element_ouroboros(self, new_word, new_link):
        ouroboros = self.registry.add_element(word=new_word, link=new_link)
        return ouroboros
    
    def __add_registry(self):
        new_registry = REGISTRY()
        self.pointer = new_registry
    
    def get_data_registry(self):
        return self.pointer.get_registry()

    def beginning(self):
        self.pointer = self.__ouroboros.link
        
    def next_pointer(self, pointer):
        self.pointer = pointer        
        
    def add_line(self, line):
        self.beginning()
        list_word = line.split()
        for i in range(len(list_word)):
            print(i)
            for word_registry in self.get_data_registry():
                if list_word[i] == word_registry.word:
                    break
            if len(list_word) != i+1:
                tmp = self.pointer
                self.__add_registry()
                tmp.add_element(list_word[i], self.pointer)
                
                
            elif len(list_word) == i+1:
                self.pointer.add_element(list_word[i], self.__ouroboros)
                self.beginning()
        
        
    
        

        
        
from golana.queue import QUEUE


if __name__=="__main__":
    data = 'with not and tot'
    
    bd = QUEUE()
    
    print(bd.get_element()[0])
    test = bd.get_link()
    print(test.word)
    bd.add_element('test')
    print(bd.get_element()[0].word)

    
        
    
from golana.queue import QUEUE


if __name__=="__main__":
    data = 'with not and tot'
    
    bd = QUEUE()
    print(bd.pointer)
    print(bd.get_data_registry())
    bd.add_line(data)
    print(bd.get_data_registry())
    bd.beginning()
    print(bd.get_data_registry()[0].link)
    print(bd.get_data_registry()[1].link)
    pointer = bd.get_data_registry()[1].link
    bd.next_pointer(pointer)
    print(bd.get_data_registry()[0].link)
    print(bd.get_data_registry()[0].word)

    
        
    
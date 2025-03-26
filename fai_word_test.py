from golana.queue import QUEUE


if __name__=="__main__":
    data1 = 'with not and tot'
    data2 = 'bob cry with pay'
    data3 = 'with ll pp dd'
    
    bd = QUEUE()
    print(bd.pointer)
    print(bd.get_data_registry())
    bd.add_line(data1)
    print(bd.get_data_registry())
    bd.beginning()
    print(bd.get_data_registry()[0].link)
    print(bd.get_data_registry()[1].link)
    pointer = bd.get_data_registry()[1].link
    bd.next_pointer(pointer)
    print(bd.get_data_registry()[0].link)
    print(bd.get_data_registry()[0].word)

    bd.add_line(data2)
    bd.add_line(data3)
    bd.beginning()
    print(bd.get_data_registry()[0].link)
    print(bd.get_data_registry()[0].word)
    print(bd.get_data_registry()[1].link)
    print(bd.get_data_registry()[1].word)
    print(bd.get_data_registry()[2].link)
    print(bd.get_data_registry()[2].word)
    
    print(bd.get_data_registry())
    print(bd.get_data_registry()[3].link)
    print(bd.get_data_registry()[3].word)
    
        
    
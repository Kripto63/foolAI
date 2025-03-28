from golana.queue import QUEUE


if __name__=="__main__":
    data1 = 'with not and tot'
    data2 = 'bob cry with pay'
    data3 = 'with ll pp dd'
    
    bd = QUEUE()
    print(bd.get_data_registry()[0].word)
    bd.add_line(data1)
    bd.add_line(data2)
    bd.add_line(data3)
    print(bd.pointer)
    for i in bd.get_data_registry():
        print(i.word)
        print(i.link)
    
    # with open('./Xorg.0.log', 'r') as f:
    #     for i in f.readlines():
    #         bd.add_line(i)
            
        
    # for i in bd.get_data_registry():
    #     print(i.word)
    
        
    
from golana.queue import QUEUE


if __name__=="__main__":
    data = 'with not and tot'
    
    bd = QUEUE()
    
    bd.add_line(data)
    
    for i in range(100):
        print(bd.get_pointer())
        bd.next_element()

    
        
    
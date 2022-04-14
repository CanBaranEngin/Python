def unique_in_order(iterable):
    list=[]
    result_list=[]
    
    for i in iterable:
        
        list.append(i)
    
    for v in range(len(list)-1):
        
        if list[v]!=list[v+1]:
            result_list.append(list[v])
            
    result_list.append(list[len(list)-1])
                
                
    return result_list

    
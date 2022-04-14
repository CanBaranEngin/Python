def get_count(sentence):
    
    sentence=list(sentence)
    last_list=[]
    
    for i in sentence:
        
        if i in ('a','e','i','o','u') :
            last_list.append(i)
            
        
    if 'y' in last_list:
        last_list.remove('y')
        
    count=len(last_list)
    
    return count
def accum(s):

    value=""
        
    s=s.lower()
    
    for a in range(len(s)):
        value+=s[a]*(a+1)+"-"
        
    return value[0:-1].title()

print(accum("abcd"))
def end_check(phrase):
    
    max_length = len(phrase) // 2
    
    for i in range(max_length, 0, -1):
        
        if phrase[:i] == phrase[-i:]:
            return(phrase[:i])
    
    return ""

assert end_check("test") == "t"
assert end_check("testing") == ""  
assert end_check("123test123") == "123"
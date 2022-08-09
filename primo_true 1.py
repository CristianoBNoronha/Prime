def primos(p):
    primo = True    
    x = 2
    if p == 2:
        return primo
    else:
        while x < p / 2:
            while primo == False:
                if p % x == 0:
                    return primo == False        
            return primo
            x = x + 1

def hackerstr(lenght):
    from random import choice
    symbols = ['a','b','c','d','e','i','g']
    hackerstr = ''
    for i in range(0,int(lenght)):
        hackerstr+=choice(symbols)
    return hackerstr
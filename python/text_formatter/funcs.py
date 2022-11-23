def uppercase(text):
    return str(text).upper()

def lowercase(text):
    return str(text).lower()

def capitalize(text):
    return str(text).capitalize()

def ladder(text):
    slicer = len(text)
    steps = []
    for i in range(slicer):
        steps.append(str(text)[:slicer])
        slicer-=1
    return steps

def ladder2(text):
    steps = ladder(text)
    steps2 = ladder(text)[::-1]
    steps.pop(len(steps)-1)
    return steps+steps2


def replace(text,what,new):
    return str(text).replace(what,new)
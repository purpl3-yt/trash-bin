import funcs

modes_dict = {}


for fun in dir(funcs):
    if not '_' in fun:
        try:
            exec(f'var = funcs.{fun}("{fun}");modes_dict["{fun}"] = [var,funcs.{fun}]')
        except TypeError:
            exec(f'modes_dict["{fun}"] = ["{fun}",funcs.{fun}]')

def get_dialog():
    index = 1
    messages = []
    for key,mode in list(modes_dict.items()):
        try:
            messages.append(str(index)+') '+mode[1](key))
        except TypeError:
            messages.append(str(index)+') '+str(key).capitalize())
        index+=1
    return messages
print('\n'.join(get_dialog()))
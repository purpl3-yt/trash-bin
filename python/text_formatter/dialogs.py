import funcs

modes_list = []

for fun in dir(funcs):
    if not '_' in fun:
        modes_list.append(fun)

def generate_help():
    help = ', '.join(modes_list)
    return help
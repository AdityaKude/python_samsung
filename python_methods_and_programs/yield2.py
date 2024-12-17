def my_range(*args):
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            yield i
            i += 1
    elif len(args) == 3 and args[2] > 0:
        i = args[0]
        while i < args[1]:
            yield i
            i += args[2]
    elif len(args) == 3 and args[2] < 0:
        i = args[0]
        while i > args[1]:
            yield i
            i += args[2]

for i in my_range(27, 2, -3):
    print('i = ', i)
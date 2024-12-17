def my_function(*args):
    print(args)
    print(type(args))
    print(args[0])
    print(type(args[0]))

my_function(2, 3, 5, 7, 11, 13, 17, 19)
my_function([2, 5, 7, 9])
#my_function(10)
#my_function(2, 3, 5)

#my_function()
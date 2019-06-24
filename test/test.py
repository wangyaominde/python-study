'''def one(func):
    print("this is func one")
    def abc(*args):
        print(*args)
        func()
    return abc

@one
def two():
    print("this is func two")


two(1,2)'''

def a(func):
    print("this is func one")
    def abc():
        func()
    return abc

def c(func):
    print("this is func three")
    def abc():
        func()
    return abc

@c
@a
def b():
    print("this is func two")



b()

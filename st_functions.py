# **********************************************************************************************************************
# **********************************************************************************************************************
# *****Lesson 26 'Functions part 1'
print('**************************************************************************************************************')


def hello(name, word):
    print('Hello, ' + name + '. Say ' + word)


hello('John', 'hi')
hello('Katy', 'hello')

print('**************************************************************************************************************')


def get_sum(a, b):
    print(a + b)


x = 2
y = 5
get_sum(1, 3)
get_sum(x, y)

print('**************************************************************************************************************')
print(len('Hello'))

print('**************************************************************************************************************')


def get_sum(a, b):
    return a + b


print(get_sum(1, 2))

print('**************************************************************************************************************')


def hi():
    print('Hi')


hi()

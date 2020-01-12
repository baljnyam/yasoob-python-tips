def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('enkhbat', 'python', 'eggs', 'test')


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

import pdb


def make_bread():
    pdb.set_trace()
    return "I don't have time"


print(make_bread())

def generator_fucntion():
    for i in range(10):
        yield i


for item in generator_fucntion():
    print(item)

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in fibon(1000000):
    print(x)

def generator_function():
    for i in range(3):
        yield i


gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))

my_string = "Enkhbat"
my_iter = iter(my_string)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

def multiply(x):
    return (x*x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

a_set = {'red', 'blue', 'green'}
print(type(a_set))

is_nice = True
state = "nice" if is_nice else "not nice"

print(state)

nice = True
personality = ("mean", "nice")[nice]
print("The cat is ",personality)

condition = True
print(2 if condition else 1/0)

print(1/0, 2)[condition]
def hi(name="enkhbat"):
    return "hi " + name


print(hi())
greet = hi
print(greet())

del hi
print(greet())

def hi(name="enkhbat"):
    print("now you are inside the hi( function")

    def greet():
        return "now you are in the greet( function"

    def welcome():
        return "now you are in the welcome function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()

def hi(name="Enkhbat"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "Enkhbat":
        return greet
    else:
        return welcome


a = hi()
print(a)

print(a())

def hi():
    return "hi enkhat"


def doSomethingBeforeHi(func):
    print("I am doing some borin work before executing hi()")
    print(func())


doSomethingBeforeHi(hi)

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(
    a_function_requiring_decoration)

a_function_requiring_decoration()

from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("i am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")


print(a_function_requiring_decoration.__name__)

from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated


@decorator_name
def func():
    return("Function is running")


can_run = True
print(func())

can_run = False
print(func())


import inspect
from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)

def add(value1, value2):
    global result
    result = value2 + value2


add(3, 5)
print(result)

def profile():
    name = "Danny"
    age = 30
    return name, age


profile_name, profile_age = profile()
print(profile_name)
# Output: Danny
print(profile_age)
# Output: 30

from collections import namedtuple


def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)


p = profile()
print(p, type(p))
print(p.name)
print(p.age)
p = profile()
print(p[0])
print(p[1])
name, age = profile()
print(name)
print(age)

foo = ['hi']
print(foo)

bar = foo
bar += ['bye']
print(foo)

def add_to(num, target=[]):
    target.append(num)
    return target


print(add_to(1))
print(add_to(2))
print(add_to(3))

from collections import defaultdict

colours = (
    ('Enkhbat', 'Yellow'),
    ('Zaya', 'Brown'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver')
)

favourite_color = defaultdict(list)

for name, colour in colours:
    favourite_color[name].append(colour)

print(favourite_color)

from collections import OrderedDict

colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)

from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

from collections import deque
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# Output: '3'

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=30, type="cat")

print(perry)

print(perry.name)

from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # The list goes on and on...

    # But we don't really care about age, so we can use an alias.
    kitten = 1
    puppy = 2


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie.type == tom.type)


print(charlie.type)
some_list = [1, 2, 3, 4, 5]
for counter, value in enumerate(some_list):
    print(counter, value)
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

my_list = [1, 2, 3]
print(dir(my_list))

name = "Yasoob"
print(id(name))

print(inspect.getmembers(str))

squared = [x**2 for x in range(10)]
print(squared)

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

print(mcase_frequency)

# squared = {x**2 for x in [1, 1, 2]}
# print(squared)
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
    print(x)
    # Outputs numbers

squared = {x**2 for x in [1, 1, 2]}
print(squared)

multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
    print(x)
    # Outputs numbers

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))

try:
    file = open('test.txt', 'rb')
except Exception as e:
    raise e

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

Output: An IOError occurred. No such file or directory
This would be printed whether or not an exception occurred!

try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

class Cal(object):
    pi = 3.142

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)


a = Cal(32)
print(a.area())

class SuperClass(object):
    superpowers = []

    def __init__(self, name):
        self.name = name

    def add_superpower(self, power):
        self.superpowers.append(power)


foo = SuperClass('foo')
bar = SuperClass('bar')

print(foo.name, foo.add_superpower('go'), foo.superpowers)

class OldClass():
    def __init__(self):
        print('I am an old class')


class NewClass(object):
    def __init__(self):
        print('I am a jazzy new class')


old = OldClass()
# Output: I am an old class

new = NewClass()

class GetTest(object):
    def __init__(self):
        print('Greetings!!')

    def another_method(self):
        print('I am another method which is not automatically called')


a = GetTest()

a.another_method()

class GetTest(object):
    def __init__(self, name):
        print('Greetings!! {0}'.format(name))

    def another_method(self):
        print('I am another method which is not automitically')


a = GetTest('Enkhbat')
b = GetTest()


class GetTest(object):
    def __init__(self):
        self.info = {
            'name': 'Yasoob',
            'country': 'Pakistan',
            'number': 12345812
        }

    def __getitem__(self, i):
        return self.info[i]


foo = GetTest()

print(foo['name'])

print(foo['number'])

def add(x, y): return x + y


print(add(3, 5))

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)
Output: [(13, -3), (4, 1), (1, 2), (9, 10)]


from pprint import pprint
my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
print(dir(my_dict))
pprint(dir(my_dict))
import itertools

a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
print(list(itertools.chain(*a_list)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor

include <stdio.h>

from functools import lru_cache


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(10)])


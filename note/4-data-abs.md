# 12 - list
# 13 - tree
# 31 - iterator

# Reducing a Sequence to a Value

E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).

reduce(pow, [1, 2, 3, 4], 2)

# 31

A container can provide an iterator that provides access to its elements in order

iter(iterable):
  Return an iterator over the elementsof an iterable value

next(iterator):
  Return the next element in an iterator

>>> s = [3, 4, 5]
>>> t = iter(s)
>>> next(t)
3
>>> next(t)
4

# Dictionary Iteration

A dictionary, its keys, its values, and its items are all iterable values

  The order of items in a dictionary is the order in which they were added (Python 3.6+)

  Historically, items appeared in an arbitrary order (Python 3.5 and earlier)

>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d['zero'] = 0
>>> k = iter(d.keys())  # or iter(d)
>>> next(k)

>>> v = iter(d.values())
>>> i = iter(d.items())

# For Statements

for i in iter(a):

# Built-In Iterator Functions

## return iterators

map(func, iterable):
filter(func, iterable):
zip(first_iter, second_iter):
reversed(sequence):

### map

>>> bcd = ['b', 'c', 'd']
>>> [x.upper() for x in bcd]
['B', 'C', 'D']
>>> map(lambda x: x.upper(), bcd)
<map object at 0x10237aef0>
>>> m = map(lambda x: x.upper(), bcd)
>>> next(m)

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

>>> map(double, [3, 5, 7])
>>> m = map(double, [3, 5, 7])
>>> next(m)
*** 3 => 6 ***
6
>>> next(m)
*** 5 => 10 ***
8
>>> list(m)
*** 7 => 14 ***
[14]

### filter

>>> m = map(double, range(3, 7))
>>> f = lambda y: y >= 10
>>> t = filter(f, m)
>>> next(t)
*** 3 ==> 6 ***
*** 4 ==> 8 ***
*** 5 ==> 10 ***
10
>>> next(t)
*** 6 ==> 12 ***
12
>>> list(t)
[]
>>> list(filter(f, map(double, range(3, 7))))
*** 3 ==> 6 ***
*** 4 ==> 8 ***
*** 5 ==> 10 ***
*** 6 ==> 12 ***
[10, 12]

### reversed

>>> t = [1, 2, 3, 2, 1]
>>> reversed(t) == t
False
>>> list(reversed(t)) == t
True

### zip

>>> items = zip(d.keys(), d.values()) # Call next(items)
>>> next(items)
('b', 2)
>>> next(items)
('a', 1)

###

## place the resulting elements into a container

list(iterable):
tuple(iterable):
sorted(iterable):

# Generators

A generator function is a function that yields values instead of returning them

A normal function returns once; a generator function can yield multiple times

A generator is an iterator created automatically by calling a generator function

When a generator function is called, it returns a generator that iterates over its yields

>>> def plus_minus(x):
...     yield x
...     yield -x

>>> t = plus_minus(3)
>>> next(t)
3
>>> next(t)
-3
>>> t
<generator object plus_minus ...>

# Generators can Yield from Iterators

A yield from statement yields all values from an iterator or iterable (Python 3.3)

def a_then_b(a, b):
    yield from a
    yield from b

>>> list(countdown(5))
[5, 4, 3, 2, 1]

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)

        def evens(start, end):
            """A generator function that returns even numbers.

            "DEMO5"

>>> list(evens(2, 10))
[2, 4, 6, 8]
>>> list(evens(1, 10))
[2, 4, 6, 8]
"""
even = start + (start % 2)
while even < end:
    yield even
    even += 2

def prefixes(s):
    """Yield all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s

        def substrings(s):
            """Yield all substrings of s.

>>> list(substrings('tops'))
['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
"""
if s:
    yield from prefixes(s)
    yield from substrings(s[1:])

# 32 - streams

def sum_primes(a, b):
    return sum(filter(is_prime, range(a, b)))

## list

digits = [1, 8, 2, 8]
[2, 7] + digits * 2

sum([[2,3],[4]],[])
[2, 3, 4]

[[2, 7],[3]] + [3]
  [[2, 7], [3], 3]

# 23-data example

s = [1,2]
t = [3,4]
s[0] = t
s
Out[7]:
  [[3, 4], 2]

## slice assignment

s = [1,2]
s[0:0]=t
s
  Out[10]:
  [3, 4, 1, 2]

s[3:]=t
s
  Out[13]:
  [3, 4, 1, 3, 4]

s.append(x)
s.extend(listx)
t=list(s)

## Lists in Lists in Lists in Environment Diagrams

t = [1, 2, 3]
t[1:3] = [t]
t
  Out[23]:
  [1, [...]]
t.extend(t)
t
  Out[25]:
  [1, [...], 1, [...]]

t = [[1, 2], [3, 4]]
t[0].append(t[1:2])

## sum

Hint: If you sum a list of lists, you get a list containing the elements of those lists

sum([[2, 7],[3]],[3])
  [3, 2, 7, 3]

sum([ [1], [2, 3], [4] ], [])
  [1, 2, 3, 4]

sum([ [1] ], [])
  [1]

sum([ [[1]], [2] ], [])
  [[1], 2]
  因为第一个list的第一个元素list的元素是[1]

sum([[2],[3]])
  TypeError: unsupported operand type(s) for +: 'int' and 'list'

sum([[2],[3]],[])
  [2, 3]

## containers

not(5 in digits)

## sequence iteration

for i in digits:
  print(i)

## Sequence Unpacking in For Statements

pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0
for x, y in pairs:
  print(x,y)

## The Range Type

A range is a sequence of consecutive integers.*

```py
range(2,5)

list(range(5,8))
len(range(5,8))
[2,3,4]

length: end - start

range(4)
range(0,4)

for i in range(3):
  print(i)

for _ in range(3):
    print('hello')

max(range(10))
max(range(10), key=lambda x: 7 - (x-2)*(x-4))
```

## List Comprehensions

[letters[i] for i in [3, 4, 6, 8]]
返回一个list

[<map exp> for <name> in <iter exp> if <filter exp>]
[<map exp> for <name> in <iter exp>]

List是一个<iter exp>

## Strings are an Abstraction

f = 'curry = lambda f: lambda x: lambda y: f(x, y)'
exec(f)

from operator import add
curry(add)(2)(1)

单引号、双引号，等价
\ escape
\n

words = ['apple', 'banana', 'cherry']
max(words)

max(words, key=len)
max(words, key=lambda word: word[1])

# Dictionary

restriction
- A key of a dictionary cannot be a list or a dictionary (or any mutable type)
- Two keys cannot be equal; There can be at most one value for a given key

```py
numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['X']
numerals[10]

'X' in numerals
10 in numerals

numerals.keys()

numerals.get('X', 0)
numerals.get('X-ray', 0)

```
get(key, value)

  key - key to be searched in the dictionary value (optional) - Value to be returned if the key is not found. The default value is None.

```py
numerals.values()
list(numerals.values())
sum(numerals.values())

numerals.items()
pairs = numerals.items()
dict(pairs)

{x: x*x for x in range(3,6)}
```

sum({3:9,5:25})

## Box-and-Pointer Notation

closure property if:  The result of combination can itself be combined using the same method
Closure is powerful because it permits us to create hierarchical structures
Hierarchical structures are made up of parts, which themselves are made up of parts, and so on

# Slicing Creates New Values

# Processing Container Values

Sequence Aggregation

Several built-in functions take iterable arguments and aggregate them into a value

sum(iterable[, start]) -> value

  Return the sum of an iterable (not of strings) plus the valueof parameter 'start' (which defaults to 0).  

  When the iterable isempty, return start.

max(iterable[, key=func]) -> value
max(a, b, c, ...[, key=func]) -> value

  With a single iterable argument, return its largest item.

  With two or more arguments, return the largest argument.

all(iterable) -> bool

Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True.

# Tree Abstraction

root label

def branches(tree):
  return tree[1:]

def label(tree):
  return tree[0]

def tree(label, branches=[]):
  return [label] + list(branches)

[3, [1], [2, [1], [1]]]
包括三个值

def is_tree(tree):
  if type(tree) != list or len(tree)<1:
    return False
  for branch in branches(tree):
    if not is_tree(branch):
      return False
  return True

def is_leaf(tree):
    return not branches(tree)

node
label
parent/child

# Tree Processing Uses Recursion

leaf is the base

def count_leaves(t):
  if is_leaf(t):
      return 1
  else:
      return sum([count_leaves(x) for x in branches(t)])

def leaves(t):
  if is_leaf(t):
      return [label(t)]
  else:
      return sum([leaves(x) for x in branches(t)],[])

def print_tree(tree, indent=0):

  print('  ' * indent, label(tree))
  [print_tree(x, indent + 1) for x in branches(tree)]

def fib_tree(n):

    if n <= 1:
      return tree(n)
    else:
      left = fib_tree(n-1)
      right = fib_tree(n-2)
      return tree(label(left)+label(right), [left, right])

## bool

bool(5)
bool(True)
bool(False)
bool(0)
bool('hello')
bool('')

# all, any

all([x < 5 for x in range(5)])
perfect_square = lambda x: x == round(x ** 0.5) ** 2
any([perfect_square(x) for x in range(50, 60)]) # Try ,65)

# partition options

```py
def partition_options(total, bignum):
  if total == 0:
    return [[]]
  elif total < 0:
    return []
  elif bignum == 0:
    return []
  else:
    with_big = partition_options(total-bignum,bignum-1)
    without_big = partition_options(total,bignum-1)
    with_big = [[x,bignum] for x in with_big]
    return with_big + without_big
```

#

C语言中有三元条件表达式，如 a>b?a:b，Python中没有三目运算符(?:)

x if x > 1 else "that"

h = "变量1" if a>b else "变量2"

h = a-b if a>b else a+b

#

1
  2
    3
      6
      1
      2

[1, [2, [3, [6], [1], [2]]]]

# zip

zip() in Python
The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as set
mapped = set(mapped)

# printing resultant values  
print ("The zipped result is : ",end="")
print (mapped)
Output:

The zipped result is : {('Shambhavi', 3, 60), ('Astha', 2, 70),
('Manjeet', 4, 40), ('Nikhil', 1, 50)}

# unzip
mapped = list(mapped)

# unzipping values
```py
namz, roll_noz, marksz = zip(*mapped)
```

# type
type(m) == list

# Higher order functions

Sec. 1.6
http://composingprograms.com/pages/16-higher-order-functions.html

## ppt

design functions
- domain: input
- range: output values
- behavior: relationship between input and output

generalization

higher-order function

summation(5,cube)

func as return Values

lambda expression

## py

assert r > 0, "r should be positive"

## disc02

(lambda y: y + 5)(4)

(lambda f, x: f(x))(lambda y: y + 1, 10)

### curry

def curry2(h):
  def f(x):
      def g(y):
        return h(x, y)
      return g
  return f

make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)

# 06

process_digits

# 07

happy number example
graph
sound

# 08

ppt
- sound demo
- test driven dev
- curry
- decorator

https://en.wikipedia.org/wiki/Triangle_wave

https://en.wikipedia.org/wiki/Sampling_(signal_processing)

seen = set()
if n not in seen:
  seen.add(n)

str(n)

# 08

ppt
- sound demo
- test driven dev
- curry
- decorator

```py
open_close(lambda sample: sample)

for sample in L:
    out.writeframes(encode(mapper(sample)))

# 幅度
open_close(lambda sample: sample/4)

# 翻转
for sample in L[::-1]:
    out.writeframes(encode(mapper(sample)))

# 重复
for sample in L:
    out.writeframes(encode(mapper(sample)))
    out.writeframes(encode(mapper(sample)))

# 采样
everyother = False
for sample in L:
    if everyother:
        out.writeframes(encode(mapper(sample)))
    everyother = not everyother
```

# Abstraction

如何命名

# Test-Driven Development

Write the test of a function before you write the function.

Develop incrementally and test each piece before moving on.

Bonus idea: Run your code interactively.

Currying

## Decorators

The main decorator marks the function that starts a program. For example,

def trace(fn):

    """A decorator that prints a function's name, its arguments, and its return
    values each time the function is called. For example,

```py
import code
import functools
import inspect
import re
import signal
import sys

@main
def my_run_function():
    # function body

# 相当于：

def my_run_function():
    # function body
my_run_function = main(my_run_function)

repr(e)
a.items()
'{0}({1})'.format(x,y)
', '.join()

[repr(k) + '=' + repr(v) for k, v in kwds.items()]

try:
  xx
exception Exception as e:
  xx
  raise

re.sub('\n', '\n' + _PREFIX, message)

log('File "{f[1]}", line {f[2]}, in {f[3]}'.format(f=frame))

def handler(signum, frame):
    print()
    exit(0)
signal.signal(signal.SIGINT, handler)

curry2 = lambda f: lambda x: lambda y: f(x,y)

def trace1(fn):
    """Return a function equivalent to fn that also prints trace output.

    fn -- a function of one argument.
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

#@trace1
def square(x):
    return x*x

#@trace1
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total

def split(n):
    """Split positive n into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
```

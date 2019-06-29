
Section 2.4 (http://composingprograms.com/pages/24-mutable-data.html)
Section 2.5 (http://composingprograms.com/pages/25-object-oriented-programming.html)
Section 4.2 (http://composingprograms.com/pages/42-implicit-sequences.html)

# 14 - Mutable Values
- object
- string object
- mutation
- tuple
- identity
- func default parameter

# 15 - mutable function
- nonlocal变量定义

# 16 - objects
- 除了绑定info和behavior，还是一个分布式状态（这个原来没有注意）
- 每个object有它的本地状态
- method是对象之间传递的message

# 17 - inheritance

# 18 - representations 

# lab06

Car.drive(garcias_car)

# 16 - objects

class描述instance的一般行为
构造函数
  __init__(self, argu)
判断相同
  c is not a
  c is a
Method
  def a(self, amount):
  Method通过self访问object的属性（状态）
a.method()自动提供self这个参数给method
  相当于给对象a一个这个method的message
access attributes
  getattr(obj,'balance') 相当于 obj.balance
  hasattr(obj,'balance')

class Account:

   interest = 0.02   # A class attribute

   def __init__(self, account_holder):
       self.balance = 0
       self.holder = account_holder

   # Additional methods would be defined here

dan_account = Account('Dan')
gibbes_account = Account('Gibbes')
gibbes_account.interest
dan_account.interest

构造完object的instance后（就是init
bound methods

## attribute assignment

instance的属性如果没有被设过，就用的Class的属性。因此，如果class属性变了，这些instance的属性会随着也变。

如果instance属性被设过了，就不会再跟着class属性变化而变化了。

## inheritance
account.withdraw(self,10)
或者
super().withdraw(10)
等价的

## OOD（设计）

is-a 关系：（账户 - 支票账户），用继承
has-a 关系：（银行 - 账户），用composition，属性attribute。银行有一个属性是账号列表

## 多元继承

supers = [c.__name__ for c in AsSeenOnTVAccount.mro()]

# 15 - mutable function

## non-local assignment

允许函数行为变化（非常有意思）

是把函数的本地state移到了它的parent里。

persistent loal state using environment
函数里面套一个函数。这个函数里有nonlocal变量，会绑定到non-local frame

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

a = make_withdraw(100)
a(10)

## mutable值没有nonlocal定义也可以被改变

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

这种方法也挺好

## 表达式 referentially transparent

用值替换这个表达式，不会改变程序的意义。
但mutation操作会改变环境

# 14 - mutable

objects
  class
    attributes
    methods

    today = date.today()
    date(2019,5,14)
    str(final - today)
    today.year
    today.strftime('%A, %B %d')
    type(today)

string objects
    ascii: 7 bit
    unicode:

    s.upper()
    s.lower()
    s.swapcase()

    ord('a')
    hex(ord('a'))
    print('1\n2\n3')
    print('\a')

    b = lookup('BASKETBALL AND HOOP')
    len(b)
    b.encode()
    print(b)

mutation operation
    only mutable object can change: list, dict
    function can change the inputted or global mutable objects

    list
      s[2:] = []
      a.pop(), a.remove('a'), a.append('b'), a.extend(['a','b'])

    dictionary
      a['b'] = 10
      a.pop('b')
      a = {1: [2]}
      a = {(1, 2): 3}
      a
        Out[53]:
          {(1, 2): 3}
      a[(1,2)]
        Out[54]:
          3

Tuple
  immutable
  (1,2,3)
  immutable里包括mutable，这个mutable还是可以改变
  s = ([1,2],3)
  s[0] = 4
  s[0][0] = 4

  a = 3,4,5,6
  a
    Out[29]:
    (3, 4, 5, 6)
  a = (4,5)
  a = tuple()
  a = tuple([1,2,3])
  (2,)
  (3, 4) + (5, 6)
    Out[45]:
    (3, 4, 5, 6)
  (3, 4, 5) * 2
    Out[46]:
    (3, 4, 5, 3, 4, 5)
  5 in (3, 4, 5)

  tuple虽然a=b了，但并不像list那样捆绑到一起。把b的值改了后，就不是is关系了
  a = 1,2,3
  a = b
  a is b
  b = 4,5
  a is b

Mutation
  >>> a = [10]
  >>> b = a
  >>> a == b
  True
  >>> a.append(20)
  >>> a
  [10, 20]
  >>> b
  [10, 20]
  >>> a == b
  True

Identity Operator
  is
  ==

Mutable default argument are dangerous
  默认参数属于函数
  每次函数调用，会bound到同一个值

  >>> def f(s=[]):
  ...     s.append(3)
  ...     return len(s)
  ...
  >>> f()
  1
  >>> f()
  2
  >>> f()
  3

  pythontutor.com/composingprograms.html#code=def%20f%28s%3D[]%29%3A%0A%20%20%20%20s.append%283%29%0A%20%20%20%20return%20len%28s%29%0A%20%20%20%20%0Af%28%29%0Af%28%29%0Af%28%29&mode=display&origin=composingprograms.js&cumulative=true&py=3&rawInputLstJSON=[]&curInstr=0

  # 18 representations
  - string representations
  - Polymorphic Functions
  - Interface

  # string表征

  all object有两个string的表征
  - str：给人看
  - repr：给解释器看

  ## repr

  repr(object) -> string
  eval(repr(object)) == object

  python interactive session打印出来的就是repr

  >>> repr(min)
  '<built-in function min>'

  >>> 12e12
  12000000000000.0
  >>> print(repr(12e12))
  12000000000000.0

  ## str

  print出来的就是str

  >>> from fractions import Fraction
  >>> half = Fraction(1, 2)
  >>> repr(half)
  'Fraction(1, 2)'
  >>> str(half)
  '1/2'

  ## Polymorphic Functions

  能够用各种object作为输入

  >>> half.__repr__()
  'Fraction(1, 2)'

  >>> half.__str__()
  '1/2'

  ## Interface

  不同object可以共用一个message名字
  __repr__()就是。各种object用这一个接口

  ## 特别的Method名

  built-in behavior
  总是用__开始和结束
  __init__
  __repr__
  __add__
  __bool__
  __float__

  http://getpython3.com/diveintopython3/special-method-names.html

  http://docs.python.org/py3k/reference/datamodel.html#special-method-names

  __add__ or __radd__

  ## generic函数

  Type Dispatching:
    Inspect the type of an argument in order to select behavior

  Type Coercion:
    Convert one value to match the type of another

    >>> from math import pi
    >>> Ratio(1, 3) + pi
    3.4749259869231266

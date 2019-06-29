# 19 Growth（复杂度）
# 20 linked lists
# 21 Ordered_Sets
# 22 Tree_Sets
# 23 trees
# 24 trees

# 21 Ordered_Sets

## containers
- {}
- 随机顺序

- duplicated自动移走
>>> s = {'one', 'two', 'three', 'four', 'four'}
>>> s
{'three', 'one', 'four', 'two'}

>>> 'three' in s
True
>>> len(s)
4

- union, intersection，adjoin
不改变s，而是返回一个set
>>> s.union({'one', 'five'})
{'three', 'five', 'one', 'four', 'two'}
>>> s.intersection({'six', 'five', 'four', 'three'})
{'three', 'four'}
>>> s
{'three', 'one', 'four', 'two'}

## Implementing Sets

Sets as Linked Lists

## Sets as Unordered Sequences

empty, contains, adjoin,intersect, union

def contains(s, v):
    """Return whether set s contains value v.

    >>> s = Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    """

def empty(s):
    return s is Link.empty

def adjoin(s, v):
    if contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect(s, t):
    if s is Link.empty:
        return Link.empty
    rest = ____intersect(s.rest, t)_____
    if contains(t, s.first):
        return ____Link(s.first, rest)_____
    else:
        return rest

## Sets as Ordered Linked Lists

first, rest, <, >, ==

## Set Operations

def intersect(s, t):
    if empty(s) or empty(t):
        return Link.empty
    else:
        e1, e2 = s.first, t.first
        if e1 == e2:
            return Link(e1, intersect(s.rest, t.rest))
        elif e1 < e2:
            return intersect(s.rest, t)
        elif e2 < e1:
            return intersect(s, t.rest)

## Set Mutation

Adding to a Set Represented as an Ordered List

def add(s, v):
    """Add v to a set s, returning modified s.”””

    assert s is not List.empty
    if s.first > v:
        s.first, s.rest = __________________________ , _____________________________
    elif s.first < v and empty(s.rest):
        s.rest = ___________________________________________________________________
    elif s.first < v:
        ____________________________________________________________________________
    return s

# 22 Tree_Sets

## Binary Trees

class BTree(Tree):
    empty = Tree(None)

    def __init__(self, label, left=empty, right=empty):
        Tree.__init__(self, label, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

t = BTree(3, BTree(1),
             BTree(7, BTree(5),
                      BTree(9, BTree.empty,
                               BTree(11))))

## Binary Search Trees

折半搜索

tree上节点的值总大于左边，小于右边

找最大的元素

def largest(t):
    if _________________________:
        return _________________
    else:
        return _________________

找第二大的元素

def second(t):
    if t.is_leaf():
        return None
    elif _______________________:
        return _________________
    elif _______________________:
        return t.label
    else:
        return _________________

## Sets as Binary Search Trees

def contains(s, v):
    if s is BTree.empty:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return contains(s.right, v)
    elif s.label > v:
        return contains(s.left, v)

order of growth:
  sita(log(n))
  和深度成正比

Adjoining to a Tree Set

## fib tree

def fib_tree(n):
    """Fibonacci binary tree.

    >>> fib_tree(3)
    BTree(2, BTree(1), BTree(1, BTree(0), BTree(1)))
    """
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return BTree(fib_n, left, right)

非常适合递归

def balanced_bst(values):
    """Create a balanced binary search tree from a sorted list.

    >>> balanced_bst([1, 3, 5, 7, 9, 11, 13])
    BTree(7, BTree(3, BTree(1), BTree(5)), BTree(11, BTree(9), BTree(13)))
    """
    if not values:
        return BTree.empty
    mid = len(values) // 2
    left = balanced_bst(values[:mid])
    right = balanced_bst(values[mid+1:])
    return BTree(values[mid], left, right)

# 19 Growth

  - Memoization

# Growth

## Memoization

记住，就不用算很多次了。
从2万次，降到21次

>>> counted_fib = count(fib)
>>> fib  = memo(counted_fib)

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        print(cache)
        return cache[n]
    return memoized

a = memo(round)
a(1.1)

# count函数，可以进行time计数

使用方法：
  fib=count(fib)
  fib(20)
  fib.call_count

```py
def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

a = count(round)
a(10)
    Out[40]:
    10
a.call_count
    Out[41]:
    1
a(20)
    Out[42]:
    20
a(20.1)
    Out[43]:
    20
a.call_count
    Out[44]:
    3

```


## space consumption

## time

## Order of Growth
资源增长
n：problem size
R(n)：time或者space的测量

对所有大于m的n，k1*f(n) <= R(n) <= k2*f(n), k1,k2是常数

## 指数

用square

# Properties of Orders of Growth

- constant
- log
- nesting（嵌套：乘）
- lower-order terms

## plot

```py
def plot_times(name, xs, order=None, n=25, pct=0.1):
    f = lambda x: name + '(' + str(x) + ')'
    g = globals()

    samples = []
    for _ in range(n):
        times = lambda x: repeat(f(x), globals=g, number=1, repeat=n)
        samples.append([median(times(x)) for x in xs])
    ys = [10e6 * median(sample) for sample in zip(*samples)]

    plots.figure(figsize=(8, 8))
    plots.plot(xs, ys)

    if order:
        slopes = [y / order(x) for (x, y) in zip(xs, ys)]
        for slope in (percentile(slopes, pct), percentile(slopes, 100-pct)):
            plots.plot(xs, [slope * order(x) for x in xs], linewidth=3)
```

# 20 linked lists

Link(3, Link(4, Link(5, Link.empty)))

class Link:

  empty = ()

  def __init__(self, first, rest=empty):
      assert rest is Link.empty or isinstance(rest, Link)
      self.first = first
      self.rest = rest

>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest.rest.rest.first

class C:
     def __str__(self):
         print('hi')
         return 'hihi'
     def __repr__(self):
         print('hihihi')
         return 'hihihihi'

# 属性方法

instance属性值：按需计算

@property decorator
当查找这个属性的时候，调这个method

>>> s = Link(3, Link(4, Link(5)))
>>> s.second
4
>>> s.second = 6
>>> s.second
6
>>> s
Link(3, Link(6, Link(5)))

@<attribute>.setter decorator
当assign的时候，调这个method

# tree class

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

# Tree Mutation

def prune(t, n):

    """Prune sub-trees whose label value is n."""

    t.branches = [______________ for b in t.branches if _____________________]

    for b in t.branches:

        prune(_______________________________, _______________________________)

## 23 tree Morse

```py
def decode(signals, tree):
    """Decode signals into a letter.

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.branches if b.label == signal][0]
    leaves = [b for b in tree.branches if b.is_leaf()]
    assert len(leaves) == 1
    return leaves[0].label
```

## 24 tree-structured data

A tree can contains other trees:
[5, [6, 7], 8, [[9], 10]]
(+ 5 (- 6 7) 8 (* (- 9) 10))
(S
  (NP (JJ Short) (NNS cuts))
  (VP (VBP make)
      (NP (JJ long) (NNS delays)))
  (. .))
<ul>
  <li>Midterm <b>1</b></li>
  <li>Midterm <b>2</b></li>
</ul>
Tree processing often involves recursive calls on subtrees

## remember sth
## Recursive Accumulation

Implement bigs, which takes a Tree instance t containing integer labels. It returns the number of nodes in t whose labels are larger than any labels of their ancestor nodes.

def bigs(t):
    """Return the number of nodes in t that are larger than all their ancestors.

    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4
    """
    def f(a, x):

        if __________a.label > x____________________________:

            return 1 + _________________________________________

        else:

            return _____________________________________________

    return _____________________________________________________

# How to Design Programs

- From Problem Analysis to Data Definitions

Identify the information that must be represented and how it is represented in the chosen programming language. Formulate data definitions and illustrate them with examples.

- Signature, Purpose Statement, Header

State what kind of data the desired function consumes and produces. Formulate a concise answer to the question what the function computes. Define a stub that lives up to the signature.

- Functional Examples

Work through examples that illustrate the function’s purpose.

- Function Template

Translate the data definitions into an outline of the function.

- Function Definition

Fill in the gaps in the function template. Exploit the purpose statement and the examples.

- Testing

Articulate the examples as tests and ensure that the function passes all. Doing so discovers mistakes. Tests also supplement examples in that they help others read and understand the definition when the need arises—and it will arise for any serious program.

https://htdp.org/2018-01-06/Book/

## design a function

def smalls(t):
    """Return the non-leaf nodes in t that are smaller than all their descendants.

    >>> a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]

    """
    result = []
    def process(t):
      xxx
    process(t)
    return result

def process(t):
  if t.is_leaf():
      return __________________________________________
  else:
      smallest = ______________________________________
      if ______________________________________________:
          _____________________________________________
      return min(smallest, t.label)

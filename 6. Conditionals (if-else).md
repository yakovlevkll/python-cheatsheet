# Conditionals

## Logic operations

Every logic operation gives boolean as a result

```python
a = 5
b = 7
c = 3

equal = a == b  # >>> False
not_equal = a != b  # >>> True (another approach is 'not a == b')
more_than = a > b  # >>> False
less_than = a < b  # >>> True
more_or_equal = a >= b  # >>> False
less_or_equal = a <= b  # >>> True
```

>> NB! `=` is very different from `==`

We can chain logic operations by `and` and `or` operators. Also we can use `not` word

```python
and_statement = a != b and not b == c
# >>> True (5 != 7 and 7 not == 3)

or_statement = a > b or c < b
# >>> True (5 > 7 or 3 < 7, 3 is less than 7)
```

Truth tables for `not`, `and` and `or` operators are below, where 1 means `True` and 0 means `False`

| `a` | `not a` |
| --- | ------- |
| 0   | 1       |
| 1   | 0       |

| `a` | `b` | `a or b` |
| --- | --- | -------- |
| 0   | 0   | 0        |
| 0   | 1   | 1        |
| 1   | 0   | 1        |
| 1   | 1   | 1        |

| `a` | `b` | `a and b` |
| --- | --- | --------- |
| 0   | 0   | 0         |
| 0   | 1   | 0         |
| 1   | 0   | 0         |
| 1   | 1   | 1         |

### Strings

Comparison of strings may seem to be weird, but main principle is based on ASCII (or Unicode) code of every symbol

```python
"3A" > "31"  # >>> True (letter wins)
"12 " > "99"  # >>> True (longer wins)
"239" > "30"  # >>> True (bigger wins)
```


## If ... else

`if`, `else` and `elif` conditionals are used to perform different actions based on given statements.

The `if` conditional will execute code if statement is `True`

```python
age = 30

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')
```

>> Pay attention to indentations. Whitespaces is used to group blocks of code in Python. Use the same number of proceeding spaces for every code block

If you want to check for multiple statements, use as much `elif`'s as you need. Keep in mind that after first "true" statement it will stop and won't check statements that follow.

So if we write this

```python
if age >= 16:
    print('You are old enough to drive a car')
elif age >= 21:
    print('You are old enough to drive a tractor trailer')
else:
    print('You are not old enough to drive')
```

instead of this

```python
if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')
```

it would never let user to drive a tractor trailer.

We can combine statements with `and`, `or` or `not`

We can fix a program above

```python
if age >= 16 and age < 21:
    print('You are old enough to drive a car')
elif age >= 21:
    print('You are old enough to drive a tractor trailer')
else:
    print('You are not old enough to drive')
```

But do we really need it?

### Assignment

Sometimes you will face situations like this one

```python
if a > 5:
    b = 'Nice'
else:
    b = 'Sweet'
```

You can easily rewrite it this way

```python
b = 'Nice' if a > 5 else 'Sweet'
```

This magic is called ternary operator. It's nice and short but try to not overuse it.
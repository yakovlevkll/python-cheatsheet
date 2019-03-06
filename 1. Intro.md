# Intro

## Comments

We can easily exclude pieces of code from execution by commenting it

```python
# There is one-line comment

'''
There is
multi-line
comment
'''
```

Another important application of comments is to leave some notes for older yourself or other coders.

## Variables

A variable name can contain letters, numbers, or _, but can't start with a number or be one of reserved words - `int`, `if`, `def` etc. All of these words are highlighted by VS Code, Sublime text or other code editors

```python
number = 42
string = "text here"
boolean = True
```

One important concept - below two variables contains different information

```python
num1 = 23
str1 = '23'
```

First is a number and we can make math operation on it (such as addition, subtraction etc.). But if we try to make such operations on second one, we will have unexpected result. We will discuss this concept later.

Multi-word variable names can be written like this

```python
bigNumber = 10000000000000  # Camel case
big_number = 10000000000000  # Snake case
```

How to choose good name for variable? Well, try to choose such names, that don't need comments to describe their meaning.

## Typification

Python is a language with dynamic typification, so any type of data can be stored in the same variable in any time of program execution.

```python
type(big_number)  # >>> <class 'int'> (type of data in the variable)
new_int = int('23')  # >>> 23 (converts  into integer)
new_float = float('42.23')  # >>> 42.23 (converts into float number)
new_str = str(True)  # >>> 'True' (converts into string)
```

Python data types are:

- Numbers (integers (+ booleans), floating point numbers, complex numbers)
- Sequences (strings, lists, tuples, bytes, byte arrays)
- Sets
- Dictionaries

## Outputing data

```python
print('Hello, Python!')  # >>> Hello, Python!
```

Printing several variables

```python
num_1 = 42
str_1 = "hi there"
bool_1 = False

print(num_1, str_1, bool_1, sep='?|?', end='*!*!*') # >>> 42?|?hi there?|?False*!*!*
```

To keep from printing newlines use `end=""`

```python
print("I don't like ", end="")
print("newlines")
```

## Reading data

Read date from terminal (console)

```python
user_num = input("Enter your number: ")
```

But then, if we check data type of `user_num`, we will see this

```python
type(user_num)  # >>> <class 'str'>
```

So, user input will always be a string. If we want to handle it like a number, we need to convert it

```python
user_num = int(user_num)
```

But be careful: if user will try to enter something different from numbers, it will break your program. We will learn to handle these situations later.

>> If we need to keep program window opened after execution, we can just write `input()` in the end of our file.
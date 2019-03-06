# Strings

String is a series of characters surrounded by `'` or `"`

```python
quote = 'brevity is '
multi_line_quote = '''the
soul of'''
```

If you use a `"` or `'` between the same quote, escape it with `\`

```python
hamlet_quote = "\"To be or not to be, that is the question\""
```

Or just use different quotation marks

```python
hamlet_quote = '"To be or not to be, that is the question"'
```

## Formatting

Concatenation is a weird programistic word to denote glueing of word strings.

```python
full_quote = quote + multi_line_quote + ' wit'
# >>> 'brevity is the soul of wit'
```

We can obtain same result but saved in `quote` variable

```python
quote += multi_line_quote + ' wit.'
# >>> 'brevity is the soul of wit'
```

Tricky things

```python
text = 'word'
text *= 3  # >>> 'wordwordword'
```

But when we have many strings to glue it becomes a mess. For those situations we have more powerful tool for formating in Python

```python
chemistry_fact = 'Carbohydrates consist of {0}, {1}, and {oxygen}.'.format('C', 'H', oxygen='O')
# >>> Carbohydrates consists of C, H, and O.
```

## Substrings

We can pick substrings this way

```python
quote = 'Brevity is the soul of wit'
text = "wordwordword"

quote[1]  # >>> 'r' (Second letter in 'Brevity', start counting from 0 index)
quote[:7]  # >>> 'brevity' (first 6 characters)
quote[-3:]  # >>> 'wit' (last 3 characters)
quote[:-4]  # >>> 'Brevity is the soul of' (everything up to the last 4 characters)
new_quote = "In the beginning was the " + text[:4]  # (concatenation)
```

There are even more tricks, read the docs.

```python
sample = 'abcdefghi'
every_third = sample[0:9:3] # 'adg'
```

But we can't do such things

```python
quote[5] = 'z'  # >>> ERROR
```

## Length

```python
len(quote)  # >>> 26 (string length)
```

## Check and search

Simple check

```python
quote = 'Brevity is the soul of wit.'
search = 'wit' in quote  # >>> True
```

Finding position of one string into another (case-sensitive)

```python
quote.find("wit")  # >>> 23
quote.find("Wit")  # >>> -1 (no 'Wit' in the quote)
```

Another useful check methods

```python
quote.isalpha()  # (True if all characters in 'quote' are letters)
quote.isdigit()  # (True if there is any character and all characters are numbers)
```

## Modification

```python
string = "what is HIP?!"
string.capitalize()  # >>> 'What is hip?!'
string.lower()  # >>> 'what is hip?!'
string.upper()  # >>> 'WHAT IS HIP?!'

string.replace("HIP", "HOP")  # >>> "what is HOP?!"
```

## Cleaning

```python
string = "  Ha-ha, you      "
string.strip()  # >>> 'Ha-ha, you'
string.lstrip()  # >>> "Ha-ha, you      "
string.rstrip()  # >>> "  Ha-ha, you"
```

## Unicode

At some point you may need to get byte values of a letters.

```python
chr(65)  # >>> 'A' (character from unicode)
ord('A')  # >>> 65 (unicode of character)
```

## Making lists

We can obtain list from string this way

```python
quote = 'Brevity is the soul of wit.'
new_list = quote.split(" ")
# >>> ['Brevity', 'is', 'the', 'soul', 'of', 'wit.']
```

Read more about lists in corresponding file.
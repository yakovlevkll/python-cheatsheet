# Dictionaries

Made up of values with a unique key for each value.

```python
super_villains = {
    'Fiddler': 'Isaac Bowin',
    'Captain Cold': 'Leonard Snart',
    'Weather Wizard': 'Mark Mardon',
    'Mirror Master': 'Sam Scudder',
    'Pied Piper': 'Thomas Peterson'
}
```

We can access and rewrite values almost like with list. The only difference is that we need to pass key instead of index

```python
super_villains['Captain Cold']

super_villains['Pied Piper'] = 'Hartley Rathaway'
```

## Basic operations

Delete an entry

```python
del super_villains['Fiddler'] # Delete an entry
# >>>
```

Print the number of items in the dictionary

```python
len(super_villains)
# >>>
```

Get a list of dictionary keys

```python
super_villains.keys()
# >>>
```

Get a list of dictionary values

```python
super_villains.values()
# >>>
```

We can merge several dicts like so

```python
dict2 = {**dict3, **dict2}
# >>>
```

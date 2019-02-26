# Numbers

## Basic operations

Order of operations is similar to mathematical **BODMAS**

- **B**rackets
- **O**rders (exponents)
- **D**ivision
- **M**ultiplication
- **A**ddition
- **S**ubtraction

```python
num = 9

add_res = num + 2  # >>> 11
subtr_res_ = num - 2  # >>> 7
mult_res_ = num * 2  # >>> 18
div_res_ = num / 2  # >>> 4.5
exp_res_ = num ** 2  # >>> 81
```

Other useful operations

```python
num = 15

modulo_res = num % 4  # >>> 3 (remainder after division)
floor_div_res = num // 2  # >>> 7 (whole part after division)
negative_num = -num  # >>> -15
abs_value = abs(negative_num)  #  >>> 15 (absolute value)
rounded_val = round(9.12356, 3)  #  >>> 9.124 (3 is a number of digits after point)
```

We can change the value of variable and assign the result to the same variable like this

```python
num = 8
num = num + 3  # num = 8 + 3 = 11
num = num ** 2  # num = 11 ** 2 = 121
```

Same with other operations. Or we can use short syntax

```python
num += 3  # means num = num + 3
num -= 5
num *= 3
```

and so on.

## Import

One of the main powers of Python belongs to its packages, that can be downloaded using terminal (console) and `pip` command

For Windows users

```cmd
pip install %package_name%
```

For Linux users

```bash
sudo pip3 install %package_name%
```

Feel free to search packages in your favorite search engine.

Then you can easily add packages to your files

```python
import math  # additional math functions

sqrt_res = math.sqrt(64)  # >>> 8 (alternative is 8 ** 0.5)

radius = 5
circle_area = math.pi * radius ** 2  # math.pi = 3.14....

floored_val = math.floor(7.321)  # >>> 7 (alternative is 7.321 // 1)
```

As you can see, we use modules as `%module_name%.%method_name%`

```python
import random  # generating random numbers etc.

# Generate random number between 0 and 10
random_num = random.Random().randrange(0, 10)
```

Other useful functions (not all) from math package

```python
math.e  # >>> 2.71....
math.exp(num)  # means math.e ** num
math.log(num, base)  # if base is not defined, base will be equal to e
math.factorial(num)  # num! = 1 * 2 * 3 ... * num
math.degrees(num)  # converts radians to degrees
math.radians(num)  # converts degrees to radians
math.sin(num)  # num must be in radians
```

## Limitations

There is some kind of limitations in programming languages. Computers handle numbers in binary code. So without using specific libraries you can get some "weird" results

```python
a = 0.2 + 0.1  # >>> 0.30000000000000004
```

There is no worry about, your computer is OK. But in some situations it's better to remember such things.
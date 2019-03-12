# FUNCTIONS -------------
# Functions allow you to reuse and write readable code
# Type def (define), function name and parameters it receives
# return is used to return something to the caller of the function


def addNumbers(fNum, sNum):
    sumNum = fNum + sNum
    return sumNum


print(addNumbers(1, 4))

# Can't get the value of rNum because it was created in a function
# It is said to be out of scope
# print(sumNum)

# If you define a variable outside of the function it works every place
newNum = 0


def subNumbers(fNum, sNum):
    newNum = fNum - sNum
    return newNum


print(subNumbers(1, 4))


def get_square(x: int):
    """
    Description here.

    x (number) : number from 10 to 100
    """
    return x*x

# the dimension of an array is defined as the number
# of indices needed to select an element. (e.g. [] has 1
# dimension, [[1]] has 2, [[2], [2, [3]]]) has 3 dimensions).
# The programming language you are using doesn't implement this as
# part of its standard library. Implement a method that determines
# the dimensionality of a given array. How performant is this function?

# this is essentially finding the depth of a BST, so we can treat it as
# such. If the current "node" is not an array, then we are at the deepest
# point of that "tree" and thus return 0. Otherwise recurse through it.

def dimensionality(array):
    # the dimensionality of anything but an array is 0
    if not isinstance(array, list):
        return 0
    # the dimensionality of an empty array is 1
    elif not array:
        return 1
    # recurse through the array
    else:
        return 1 + max(dimensionality(item) for item in array)


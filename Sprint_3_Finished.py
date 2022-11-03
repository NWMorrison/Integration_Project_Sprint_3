"""Sprint 3 (Optional)"""
import numpy as np


# Sprint 3 will just be everything added in on its own
# to understand the material.

# Bitwise Operators
# Can only be used on integers.
# Used to perform bitwise calculations.
# First converted into binary and then operations are performed bit-by-bit.
# The result is returned in decimal format.


def bitwise_operator():
    """Function to showcase Bitwise Operators."""

    n = 2
    m = 8
    print("These are all examples of bitwise operators.",
          "\nn & m =", n & m,  # Returns 1 if both the bits are 1 or else it returns a 0.
          "\nn | m =", n | m,  # Returns 1 if EITHER of the bits are 1 or else it returns a 0.
          "\n~n =", ~n,  # Returns the compliment of a number.
          "\n~m =", ~m,
          "\nn ^ m =", n ^ m,  # Returns 1 if one of the bits is 1 and the other is 0  or returns false.
          "\nn >> 1 =", n >> 1,  # Right Shift Bitwise Operator.
          "\nm >> 1 =", m >> 1,  # Left Shift Bitwise Operator.
          "\nn << 1 =", n << 1,
          "\nm << 1 =", m << 1, )
    return


# https://www.geeksforgeeks.org/how-to-create-a-vector-in-python-using-numpy/
# Must import NumPy. I already have it imported in PyCharm.

"""Simple Lists/Lists In Detail"""


def constructing_vectors():

    """A function to showcase vectors.(Import Numpy)"""

    print("\nNow we are going to construct vectors from lists, then add and subtract them.")
    list1, list2 = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
    print(list1,
          list2)

    vector1, vector2 = np.array(list1), np.array(list2)
    vector_add, vector_subtract = vector1 + vector2, vector1 - vector2

    print("\nAdding the two vectors: ", vector_add,
          "\nSubtracting the two vectors: ", vector_subtract)
    return


def simple_lists():

    """How to Index, Slice, Append, Insert, Delete, Sort, Find Length, Copy & Clone a list"""

    list1, list2, list3 = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], ["Peach", "Apple", "Strawberry", "Blueberry", "Pear"]

    print("\nThese are our lists.",
          "\n", list1,
          "\n", list2,
          "\n", list3)

    print("\nIndexing A List.",
          "\n", list1[3],
          "\n", list2[-1],
          "\n", list3[0],
          "\n", list3[-2])

    print("\nSlicing a list.",
          "\n", list1[1:3],
          "\n", list2[:-1],
          "\n", list2[0:4],
          "\n", list3[2:4],
          "\n", list3[:-2])

    print("\nLength of a list.",
          "\n", len(list1),
          "\n", len(list1 + list2),
          "\n", len(list3))

    print("\nAppending a list.",
          "\n", list1,
          "\n", list2,
          "\n", list3)

    list1.append(6),
    list2.append(11),
    list3.append("Tangerine")

    print("\nThe Appended list.",
          "\n", list1,
          "\n", list2,
          "\n", list3)

    print("\nInsert a new object to a list.",
          "\n", list1,
          "\n", list2,
          "\n", list3)

    list1.insert(0, 0),
    list2.insert(0, 5),
    list3.insert(3, "Kiwi")

    print("\nNew objects inserted.",
          "\n", list1,
          "\n", list2,
          "\n", list3)

    print("\nDeleting items from a list.",
          "\n", list1,
          "\n", list2,
          "\n", list3)

    list1.remove(6)
    list2.remove(5)
    list3.remove("Tangerine")

    print("\nDeleted items from different lists.",
          "\n", list1,
          "\n", list2,
          "\n", list3)

    print("\nSorting list_3 by alphabetical order.",
          "\n", list3)
    list3.sort()
    print("\nNewly Sorted.",
          "\n", list3)

    print("\nCopying a list.")
    list_new = list3.copy()
    print("\nNewly copied list in a new variable",
          "\n", list_new)

    print("\nAn if statement looking for a specific item in a list (Peach).")
    if "Peach" in list3:
        print("Yes, Peach is in the list.")
    else:
        print("\nThat is not in the list.")
    return


"""Lists in Lists"""


def matrix():

    """Function showcasing a Matrix and a cube function"""

    matrix_a = [[-1, 5, 24, 78],
                [101, 203, 476, 500],
                [600, 700, 800, 900]]

    print("\nThe following is a made matrix",
          "\n", matrix_a, "\n",
          "\nBelow is locating certain data inside of a matrix.",
          "\n", matrix_a[0],
          "\n", matrix_a[1],
          "\n", matrix_a[0][-1],
          "\n", matrix_a[2][1:3])
    return


def cube(x):

    """Writing a function to cube an array."""

    it = np.nditer([x, None])
    for a, b in it:
        b[...] = a * a * a
    return it.operands[1]


"""Tuples"""

# Ordered/Immutable/Unchangeable.
# May convert to a list then convert back to a tuple.
# May establish a variable as a tuple and add that variable into the tuple.


def my_tuple():

    """A function showcasing a tuple."""

    list1 = ["Peach", "Apple", "Strawberry", "Blueberry", "Pear"]
    tuple1 = (list1, "Laptop", "Desktop", "Printer", "Monitor", "USB-Drive")
    list2 = [tuple1, "Red", "Blue", "Green", "Black"]

    print("Indexing a tuple.",
          "\n", tuple1[2])

    print("\nSlicing a tuple.",
          "\n", tuple1[1:4])

    print("\nBuilding into a tuple.")
    ssd = ("Solid-State-Drive",)
    tuple1 += ssd
    print(tuple1)

    print("\nTuple inside a list.",
          "\n", tuple1, "\n")

    print("List inside a tuple",
          "\n", list2)
    return


"""Dictionary"""


def dictionary1():

    """A function showcasing a dictionary"""

    dictionary_1 = {"Brand": "Sony",
                    "Model": "Playstation 5",
                    "Year": "2020"}

    print("\nNow for a dictionary",
          "\n", dictionary_1)

    print("\nIndexing a dictionary.",
          "\n", dictionary_1["Brand"],
          "\n", dictionary_1["Model"])

    print("\nFinding the keys of a dictionary.",
          "\n", dictionary_1.keys())

    print("\nFinding the values of a dictionary.",
          "\n", dictionary_1.values())

    print("\nFinding items in a dictionary.",
          "\n", dictionary_1.items())

    print("\nIf a key exists in a dictionary (Model).")
    if "Model" in dictionary_1:
        print("Yes, Model is in this dictionary.")
    else:
        print("\nNo, this item is not in this dictionary.")

    print("\nAdding an item to a dictionary.")
    dictionary_1["Color"] = "White"
    print(dictionary_1)
    return

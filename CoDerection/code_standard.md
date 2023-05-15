# CoDerection Code Standard
Or CCS for short.
## Basic Information
### How to Use this Guide
* This guide is to be followed along with [Python Enhancement Proposal 8](https://peps.python.org/pep-0008/) (PEP 8).
* If there is something that isn't specified in this guide, then follow PEP 8 for guidance.
* If someone does not follow this guide, then kindly let them know and help then correct the code if necessary.
* Examples will be provided where necessary.
### System Requirements
* Due to requirements of the project, you must use Python 3. The version used will be the lastest available version.
* You can tell the latest version from the [Python website](https://www.python.org/).
* You will also need the latest version of PyGame. You can get the latest version easily if you have Python installed. Run the command `pip install pygame` in Command Prompt or Terminal.
* While not a requirement, it is strongly recommended to use a linter while programming. It just makes things so much nicer.
## Commenting Code
### Variable Declarations
* Instead of using comments to state variable data types, use type annotations. Not only do these make the data type clear to humans, but to the computer as well. The code completion in many IDEs likes it that way too, so it can lead to faster development.
* Don't import a new module just to do this though.
* Try to be as specific as possible without violating the rule above. The intention of `myNumbers: list[int]` is much clearer than `myNumbers: list`.
* Don't annotate `self` or `cls`, the interpreter knows what you mean already.
### Documentation
* Always give public modules, classes and functions a docstring.
* It's much easier if you write the function's signature, including any type annotations, first.
* Methods decorated with the `property` class are considered fields for this, no docstring is required.
* Docstrings do not have to be detailed, as long as it can get the message accross.
* Use the Google style of docstrings, it's compact and packed with all the details needed.
* _autoDocstring - Python Docstring Generator_ is a VS code extension that does this magically for you.
* The summary for `__init__` methods should match that of the class. The method docstring should still include arguments, return values etc. The class docstring should not include those.
### Example
Insertion sort (overcomplicated to show all the rules in action):
```python
"""A custom insertion sort."""

class SortTypeError(TypeError):
    """An error happened while sorting."""
    pass

class Sorter:
    """Sorts a list."""
    def __init__(self, lst: list[int]) -> None:
        """Sorts a list.

        Args:
            lst (list[int]): The list to sort.
        """
        self.lst = lst
    
    def insertionSort(self, sortAsc: bool = True) -> list[int]:
        """Uses an insertion sort to sort self.lst. self.lst is not modified in the process.

        Args:
            sortAsc (bool, optional): Whether or not to sort in ascending order. Defaults to True.

        Returns:
            list[int]: The sorted version of the list.
        """
        def compare(x: int, y: int, sortAsc_: bool) -> bool:
            """Compare two objects (allows easy switch from ascending to descending).

            Args:
                x (int): First object to compare.
                y (int): Second object to compare.
                sortAsc_ (bool): Whether or not to sort in ascending order.

            Raises:
                SortTypeError: If the comparison types aren't compatible.

            Returns:
                bool: The result of the comparison.
            """
            try:
                return x < y if sortAsc_ else x > y
            except TypeError:
                raise SortTypeError
        lst: list[int] = self.lst.copy()
        for i in range(1, len(lst)):
            key: int = lst[i]
            while i > 0 and compare(key, lst[i - 1], sortAsc):
                lst[i] = lst[i - 1]
                i -= 1
            lst[i] = key
        return lst

sorter: Sorter = Sorter([1, 6, 5, 6, 3, 8, 9, 6, 4, 7, 6, 3])
print(sorter.insertionSort())
print(sorter.insertionSort(sortAsc=False))
print(sorter.lst)

```
## Indentation and Continuation
### Indentation
* Use 4 spaces per indentation level as per PEP 8.
* For continuation lines, use hanging indents as opposed to Python's implicit line joining.
* For multiline constructs, place the closing parenthesis/bracket/brace on the same indenation level as the start of the construct.
* Alghough PEP 8 prefers spaces, tabs are often more convenient.
### Line Length and Continuation
* Lines should not be longer than 120 columns (this is longer than PEP 8, to allow for a bit more flexability).
* Use a backslash to continue on the next line if a line is too long, and there are no parentheses already involved.
* The continued line should get one more level of indentation.
* For long expressions involving binary operators, make sure to line break before the operator.
* Make sure line breaks are in logical places, such as before a binary operator.
### Example
```python
from random import randint

fourDimensionalArray: list[list[list[list[int]]]] = [  # Nothing follows this bracket on this line.
    [[[randint(0, 100) for l in range(5)] for k in range(10)] for j in range(20)] for i in range(30)
]  # Closing bracket is not indented.

# Line break before the binary operator.
if fourDimensionalArray[1][2][3][4] == 0\
    and fourDimensionalArray[4][3][2][1] == 100\
    and fourDimensionalArray[2][2][3][3] == 50\
    and fourDimensionalArray[3][3][2][2] == 50:
    print('What a coincidence.')

# Another way to express the long condition, note that the bracket rules apply here.
# This way is actually preferrd in this case.
if (
    fourDimensionalArray[1][2][3][4] == 0
    and fourDimensionalArray[4][3][2][1] == 100
    and fourDimensionalArray[2][2][3][3] == 50
    and fourDimensionalArray[3][3][2][2] == 50
):
    print('What a coincidence.')
```
## Imports
* Import only the functions you need, an exception to this is if you are importing a module from within this project, and all of the module is needed, then `from <module> import *` can be accepted, but under no other circumstances.
* For all standard library modules or pip installed modules, use `from <module> import <needed_things>`.
```python
from random import randint
from sys import stdout

from numpy import array
from sklearn import MLPClassifier

from ..classes.grid import Grid
from ..classes.vector import *

```
## Strings
* Use single quotes in strings, unless the character `'` appears in the string, in that case, use double quotes.
* For multi-line strings (especially in an indented block), don't use triple quotes. Instead use single quotes on all the lines like the example below. This gives a nice, clean output without all those indents. If the string requires indentents, then use spaces inside the quotes to create this.
```python
choice: int = int(input(
    'Menu structure:\n'
    '    Chose 1 to add a record\n'
    '    Chose 2 to read a record\n'
    '    Chose 3 to edit a record\n'
    '    Chose 4 to remove a record\n'
    '    Chose 5 to sort all records\n'
    '    Chose 6 to clear all records\n'
    'Enter choice: '
))

```
## Naming
Mostly consistent with PEP 8, but use camelCase for functions, to easily tell them from variables.
|Identifier for|Naming Convention|
|-|-|
|Modules and packages|oneword|
|Classes, type variables, records and enums|PascalCase|
|Functions and methods (excluding properties)|camelCase|
|Variables (excluding type variables), arguments, fields and properties|snake_case|
|Constants and enum values|ALL_CAPS|
|First argument of any instance method|`self`|
|First argument of a class method|`cls`|
|Any non-public identifier|`_` + conventional name|\

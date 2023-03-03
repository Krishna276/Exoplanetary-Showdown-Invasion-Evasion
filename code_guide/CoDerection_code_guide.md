# CoDerection Code Guide
Or CCG for short.
## Basic Information
* This guide is to be followed along with [Python Enhancement Proposal 8](https://peps.python.org/pep-0008/) (PEP 8).
* If there is something that isn't specified in this guide, then follow PEP 8 for guidance.
* If someone does not follow this guide, then kindly let them know and help then correct the code if necessary.
* The timsort.py file is here for an example.
## Language
* Due to requirements of the project, you must use Python 3. The version used will be the lastest available version.
* You can tell the latest version from the [Python website](https://www.python.org/).
## Variable declarations
* Instead of using comments to state variable data types, use type annotations. Not only do these make the data type clear to humans, but to the computer as well. The code completion in many IDEs likes it that way too, so it can lead to faster development.
* Don't import a new module just to do this though.
* Try to be as specific as possible without violating the rule above. The intention of `myNumbers: list[int]` is much clearer than `myNumbers: list`.
* Don't annotate `self` or `cls`, the interpreter knows what you mean already.
## Indentation
* Use 4 spaces per indentation level as per PEP 8.
* For continuation lines, use hanging indents as opposed to Python's implicit line joining.
* For multiline constructs, place the closing parenthesis/bracket/brace on the same indenation level as the start of the construct.
* Alghough PEP 8 prefers spaces, tabs are often more convenient.
## Line Length and Continuation
* Lines should not be longer than 120 columns (this is longer than PEP 8, to allow for a bit more flexability).
* Use a backslash to continue on the next line if a line is too long (and there are no parentheses already involved).
* The continued line should get one more level of indentation.
## Imports
* Import only the functions you need, an exception to this is if you are importing a module from within this project, and all of the module is needed, then `from <module> import *` can be accepted, but under no other circumstances.
* For all standard library modules or pip installed modules, use `from <module> import <needed_things>`.
## Strings
* Use single quotes in strings, unless the character `'` appears in the string, in that case, use double quotes.
* Use a constant for a multi line string (in the first level of indentation of the file). This makes these strings in indented blocks easier to read and look nicer.
## Documentation
* Always give public modules, classes and functions a docstring. PEP 8 recommends using the style in [PEP 257](https://peps.python.org/pep-0257/).
* It's much easier if you write the function's signature (including any type annotations) first.
* Methods decorated with the `property` class are considered fields for this, no docstring is required.
## Naming
Mostly consistent with PEP 8, but use camelCase for functions, to easily tell them from variables.
|Identifier Type|Convention|
|-|-|
|Module name|snake_case|
|Class name|PascalCase|
|Function name|camelCase|
|Variable name|snake_case|
|Constant name|ALL_CAPS|
|First method argument|`self` for instance methods, `cls` for class methods|
|Anything non-public|Prefix with `_`|
* Methods decorated with the `property` class are considered fields for this, and should follow variable name conventions.

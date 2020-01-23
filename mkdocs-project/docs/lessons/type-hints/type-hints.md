# Python / Lesson / Type Hints #

This lesson provides information about Python type hints,
which are used to implement a stronger level of typing for an otherwise loosely-typed language.

* [Introduction](#introduction)
* [Generics](#generics)
* [Useful Type Hint Examples](#useful-type-hint-examples)
	+ [Class Constructor Return Value](#class-constructor-return-value)
	+ [Function Variable that May be None](#function-variable-that-may-be-none)
	+ [Function Variable that May Have Multiple Types](#function-variable-that-may-have-multiple-types)
	+ [Function that May Return a Type or None](#function-that-may-return-a-type-or-none)
	+ [Assigning a Class Variable to None](#assigning-a-class-variable-to-none)
	+ [Using Type Hint with `file` Type](#using-type-hint-with-file-type)
	+ [Using Type Hint with Function as Argument](#using-type-hint-with-function-as-argument)
	+ [Using Type Hint with Enumeration](#using-type-hint-with-enumeration)
* [Toubleshooting and Pitfalls](#toubleshooting-and-pitfalls)
	+ [Accidentally Resetting Global Data](#accidentally-resetting-global-data)
	+ [Circular Imports](#circular-imports)

---

## Introduction ##

One of the benefits of Python, at least for some applications, is that the language is loosely typed.
This means a variable can be assigned to values having different types, for example:

```python
   # Assign to a string
   a = 'a string'
   # Then re-assign to an integer
   a = 1
```

This is possible because internally all Python variables have a base type of `object`
and dictionaries of objects are used for object attributes, function parameters, etc.
Consequently, the type of a variable is defined only when the variable is assigned.
Similarly, functions can be defined with arguments without indication of the argument type,
allowing different variable types to be passed to the function.

Python provides the `isinstance()` function and `type()` functions to evaluate types.
These can be used in code to examine a variable's type in order to properly handle a variable.
See the following information.

* `isinstance()`
	+ [Python specification](https://docs.python.org/3/library/functions.html#isinstance)
	+ [W3 Schools](https://www.w3schools.com/python/ref_func_isinstance.asp)
* `type()`
	+ [Python specification](https://docs.python.org/3/library/functions.html#type)
	+ [W3 Schools](https://www.w3schools.com/python/ref_func_type.asp)

Loose typing makes it easy to write code, but presents challenges when writing
complex software that expects variables of a certain type.
Incompatible variable types may only be found at run-time, which is an issue in production software
and requires sufficient testing to ensure software quality.
Programmers might infer types based on variable names (e.g., an iterator `i` is likely an integer)
function documentation, or inline documentation.
However, this is only as robust as the care taken by previous programmers to make types obvious.

Other programming languages such as C and Java that are strongly-typed require variable types to be declared in the
code and the code will not compile into executable form until type issues are fixed.

An intermediate solution is that Integrated Development Environment (IDE) tools such as PyCharm
can benefit from type information to help programmers.
IDEs may use well-formed function documentation to assume function argument types.
To implement this solution, "type hints" were implemented in Python 3.5.

* See:  [Python Typing](https://docs.python.org/3/library/typing.html)

The above information provides quite a few examples.
See the remainder of this documentation for additional examples that may be useful.

## Generics ##

Using "generics" in a programming language is a technique that allows
code to be written in a generic way, without requiring a specific type.

* See:  [Generic Programming (Wikipedia)](https://en.wikipedia.org/wiki/Generic_programming)
* See:  [Python Type Hints for Generics](https://docs.python.org/3/library/typing.html#generics)

For example, generic code may be written to sort items in a list.
Such code does not care what specifically is in the list as long as there is a way to
compare one item in the list to another and indicate which is larger.

Generics are supported by Python type hints and are important because they provide
a generic way to implement reusable code.
However, it takes effort to write such code, typically in classes, and short of that effort,
using basic type hints as described in this documentation is often used.

## Useful Type Hint Examples ##

The Python specification for type hints provides many examples.
Additionally, the following lessons have been learned through experience.

### Class Constructor Return Value ###

A class constructor `__init()__` function should have a return value of `None` as follows:

```python
class SomeClass(object):
    def __init__(self) -> None:
```

### Function Variable that May be None ###

Python functions can accept optional parameters.
An `Optional` type hint can be used to indicate that a function parameter is optionally `None`,
as in the following example that accepts a list of `str` or `None` as input:

```python
   def some_function(required_arg: str, optional_arg: Optional[List[str]] = None) -> int):
       """
       Args:
          required_arg: a required `str` argument
          optional_arg: an optional [str] argument that defaults to None.
       """
``` 

### Function Variable that May Have Multiple Types ###

It is often the case in Python that a function variable may have more than one type,
depending on how the function is called.
An example is when a function that processes file path may accept a `str`, or a newer `Path`,
as shown in the following example:

```python
from pathlib import Path  # for Path

def some_function(filepath: str or Path) -> None:
    """
    Function that operates on the path to a file.
    """
    pass
```

In the above example, it is clear that the `filepath` argument can be a `str` or a `Path`,
rather than the programmer needing to guess at what is allowed.
An alternate syntax uses a `Union`, which requires an additional import:

```python
from pathlib import Path  # for Path
from typing import Union

def some_function(filepath: Union[str, Path]) -> None:
   """
   Function that operates on the path to a file.
   """
   pass
```

If the function argument can have any type, use `Any`.

### Function that May Return a Type or None ###

It is often the case that a function will return a value, or `None` if input was also `None`, etc.
If the function return type indicated by the type hint only indicates the `str` type,
then an IDE might complain with a message like `expecting str but None is returned`.
The following example illustrates how to avoid the warning by specifying multiple return types:

```python
def some_function(somearg1, somearg2) -> str or None:
    if something:
        return 'a string'
    else:
        return None
```

### Assigning a Class Variable to None ###

If using a class, it is typical to define the class' data in the `__init()__` function.
Not doing so may result in warnings from an IDE similar to `instance attribute x defined outside __init__`.
However, if the attribute is defined in `__init()__` and set to an initial value of `None`,
a warning may result because `None` does not match the type defined for the variable.
The following example illustrates how to allow initialization to `None`.

```python
class SomeClass(object):
    def __init__(self) -> None:

        # Initialize class data

        # The following will result in a warning
        self.x: float = None

        # The following will not result in a warning
        self.x: float or None = None
```

### Using Type Hint with `file` Type ###

The build-in `file` type in Python requires the following type hint:

```python
from typing import TextIO

def some_function(text_file_pointer: TypeIO) -> None:
    """
    Example of passing a `file` type.
    """
    pass
```

### Using Type Hint with Function as Argument ###

Python allows passing a function name as an argument to a function.
An example is an application with a user interface that uses events to communicate
between software components.  In this case, the type hint can indicate that a function type is being passed,
as in the following example:

```python
from typing import Callable

def add_listener(listener: Callable[..., None]) -> None:
    """
    Args:
        listener:  Function to be called when the UI state changes.
    """
```

In the above, the `listener` variable is a function (not a `str` function name, but the function reference)
that has a variable number of arguments and returns `None`.

### Using Type Hint with Enumeration ###

Using type hints with enumerations requires relying on a future
language feature that will be part of Python 4, as follows.
Without the `__future__` import, the enumeration will have an error 
using its own type, for example in the `get_command_phase_types()` function.

```python
# The following is needed to allow type hinting -> GeoLayer, and requires Python 3.7+
# See:  https://stackoverflow.com/questions/33533148/
#         how-do-i-specify-that-the-return-type-of-a-method-is-the-same-as-the-class-itsel
from __future__ import annotations

from enum import Enum


class CommandPhaseType(Enum):
    """
    Enumeration for command phase type.

    String representation is uppercase because it is mainly used internally:

    INITIALIZATION:  Creation and initialization of the command.
    DISCOVERY:  Run the command in discovery mode.
    RUN:  Run the command completely.

    Numerical values are ordered in logical order of command phases.
    """
    INITIALIZATION = 1
    DISCOVERY = 2
    RUN = 3

    @classmethod
    def get_command_phase_types(cls, sort: bool = False) -> [CommandPhaseType]:
        """
        Return the list of valid command phases.

        Args:
            sort:  If True, sort alphabetically.  If False, return in order of execution (default).

        Returns:
            The list of phase types, for example for use in command parameter choice.

        """
        if sort:
            # Sort alphabetically
            return [CommandPhaseType.DISCOVERY, CommandPhaseType.INITIALIZATION, CommandPhaseType.RUN]
        else:
            # Return in order of processing order.
            return [CommandPhaseType.INITIALIZATION, CommandPhaseType.DISCOVERY, CommandPhaseType.RUN]

    def __str__(self) -> str:
        """
        Format the enumeration value as a string - just return the name.

        Returns:

        """
        return self.name
```

## Toubleshooting and Pitfalls ##

Type hints can greatly increase code readability and improve programming efficiency.
However, there are a few pitfalls that may result and require troubleshooting,
as described below.

### Accidentally Resetting Global Data ###

Because attributes of objects in Python are public, a simple typo
can wreak havoc on code in unexpected ways.
For example, attempting to use type hints with bad syntax can reset data, as shown in the following:

```python
from SomeLibraryClass import SomeLibraryClass

class SomeClass(object):
    def __init__(self) -> None:

        # Initialize class data

        # The following is correct
        self.x: SomeLibraryClass or None = None

        # The following reassigns library code to None,
        # resulting in errors when trying to use later
        # - note that instead of using a colon for the type hint,
        #   an equal sign was used
        self.x = SomeLibraryClass = None
```

### Circular Imports ###

Python can handle circular imports when types are not specified.
For example, the following code works.

The following code is in file `GroupClass.py`.

```python
from InstanceClass import InstanceClass

class GroupClass(object):

    def __init__(self) -> None:
        # List of InstanceClass
        self.list_of_instances: [InstanceClass] = []

    def add_instance(self, an_instance) -> None:
```

The following code is in file `InstanceClass.py`.


```
# Note no import of GroupClass
# from GroupClass import GroupClass

class InstanceClass(object):

    def __init__(self, group) -> None:
        # Reference to GroupClass
        self.group_ref = group
```

The above works because the `InstanceClass` does not import `GroupClass` (no typing for the class).
In contrast, the following code does not work because
a circular dependency issue arises due to importing `GroupClass` in `InstanceClass`.
Python does not handle these cases well without advanced programming to dynamically load classes. 
The basic fix is to not use type hints that would result in circular dependencies (use code as shown above).

```python
from InstanceClass import InstanceClass

class GroupClass(object):

    def __init__(self) -> None:
        # List of InstanceClass
        self.list_of_instances: [InstanceClass] = []

    def add_instance(self, an_instance) -> None:
```

The following code is in file `InstanceClass.py`.


```
# The following results in a circular import issue
from GroupClass import GroupClass

class InstanceClass(object):

    def __init__(self, group: GroupClass) -> None:
        # Reference to GroupClass
        # - results in circular 
        self.group_ref: GroupClass = group
```

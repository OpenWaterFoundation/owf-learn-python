# Python / Lesson / Style Guide #

This lesson provides information about the
[PEP 8 - Python Style Guide](https://www.python.org/dev/peps/pep-0008/),
which provides guidance for Python code.

* [Introduction](#introduction)
* [Pythonic Code](#pythonic-code)
* [Summary of Python Style Guide Conventions](#summary-of-python-style-guide-conventions)
* [Using an IDE to Check Code](#using-an-ide-to-check-code)
	+ [Too Broad Exception](#too-broad-exception)
	+ [PEP 8 Naming](#pep-8-naming)
	+ [Unresolved Reference](#unresolved-reference)

----

## Introduction ##

All software code should generally follow some standard style,
regardless of programming language,
in order to promote consistency, readability, and maintainability.
Consistency is important within a software product development team and any third-party
code submissions should ideally be made consistent with the product's code.

The Python language has some built-in conventions that arise from the language itself.
For example, the convention of using tabs or spaces (preferably 4 spaces)
to indent code levels and use of colon to indicate code blocks.
Consequently, where in other language there may be debates about where to put
curly braces ( `{  }` ) to delineate code blocks,
some coding conventions are clearly defined by the Python language.

Code should generally follow the
[PEP 8 - Python Style Guide](https://www.python.org/dev/peps/pep-0008/).
However, there are cases where the Python Style Guide is difficult to follow,
including examples later in this documentation.

## Pythonic Code ##

The general term "pythonic" refers to the "Python way" of programming.
This refers to style and also the approach taken because of Python's language elements.
Quite often a programmer that uses other languages may create Python code that is not pythonic
because the programmer uses the conventions of the other language.
In some cases code written as for other languages is "ugly" and should be rewritten in a pythonic way.
In other cases, the code is perfectly fine but is perhaps not as pythonic as Python purists might write.
See the following early opinion on [What is Pythonic?](https://blog.startifact.com/posts/older/what-is-pythonic.html).

Sometimes pythonic code can be overly terse and programmers should take care not to create
code that is difficult to understand.
At a minimum, add inline comments to explain code that may not be obvious to other programmers.
Of course, if a programmer is not familiar with multiple languages,
it can be difficult to recognize code syntax that may be difficult to understand,
which is why learning multiple programming languages is helpful.

## Summary of Python Style Guide Conventions ##

The
[PEP 8 - Python Style Guide](https://www.python.org/dev/peps/pep-0008/) provides guidance for Python code.
The following provides recommendations and lessons learned for important topics.

**<p style="text-align: center;">
Summary of Important Style Guide Items
</p>**

| **Programming Topic** | **PEP 8 Recommendation** | **Comments** |
| -- | -- | -- |
| variable names | Should be `lower_case` with underscores. | This is generally simple to accomplish for most code. |
| function names | Should be `lower_case` with underscores. | This is generally simple to accomplish for most code. |
| class names | Can be `ClassName` using mixed case. | A recommended approach is to name classes `ClassName` with matching file name `ClassName.py`, which is similar to other object-oriented languages. |
| general formatting | Specific style recommendations are provided for spaces, blank lines, and indentations. | Use an IDE such as PyCharm to check, and change code accordingly. |
| indentation | Should use 4 spaces. | This is a reasonable standard and should be followed.  Don't use tabs. |
| type hinting | Recommendations are provided to indicate type information using type hints (since Python 3.5) to help code readability and programming tools. | See the [Type Hinting lesson](../type-hinting/type-hinting.md). |

## Using an IDE to Check Code ##

Editing Python code in a text editor and running a Python program on the command line will not result
in warnings about Python style issues.
However, an Integrated Development Environment (IDE), such as PyCharm,
will indicate style violations because the IDE inspects code and tries to help the programmer
produce better quality and warning-free code.
Therefore, it is recommended that an IDE be used where possible, especially for complex products.

In the case of PyCharm, it can be irritating if code cannot be changed to match the Python Style Guide,
and style and other warnings continue to be displayed.
It is possible to globally disable warnings of specific type.
However, this will disable all warnings of a type, which will ignore valid warnings that should be addressed.
Instead, specific warnings can be disabled case by case by using a `# noinspection xxxx` comment immediately before the issue.

* See the [PyCharm `noinspection` list](https://www.jetbrains.com/help/pycharm/disabling-and-enabling-inspections.html)

The following are examples of common cases where warnings may need to be disabled.

### Too Broad Exception ###

The Python Style Guide recommends against using generic `except Exception` syntax,
instead encouraging catching specific exception types.
However, because Python programming tools may not alert programmers to exception types that are thrown by called code,
it can be difficult to know what exception types to catch
(a determination may be made by reading documentation or experiencing an exception by running code).
To ensure that code gracefully handles deep code levels, it is often helpful to catch `Exception` as the last
exception type.
However, this will often cause an IDE to complain about a "too broad" exception.
The following example illustrates how to disable the warning.

```python
# noinspection PyBroadException
try:
    # some code here
    pass
except SomeExceptionType:
    # Handle the exception type here
    pass
except Exception:
    # Handle fall-through case that might occur
    # some code here
    pass
```

### PEP 8 Naming ###

The Python Style Guide recommends using `lower_case` naming for variables and functions,
and an IDE will warn about violations to the style.
In most cases, it is possible to change code to follow the style guide.
However, there are cases where using alternate style, such as `MixedCase` or `camelCase` makes sense,
for example when trying to maintain consistency with code ported from another language or
when trying to match references to a library.
For example, user interface code that uses Qt may benefit from using variable and function names that
match Qt names (e.g., `something_QPushButton`).
The following code illustrates how to disable the warning,
in this case for a variable that matches user input.

```python
    # noinspection PyPep8Naming
    pv_LogFile = self.get_parameter_value('LogFile')
    # Unfortunately, the same comment must be inserted before each assignment.
    # noinspection PyPep8Naming
    pv_LogFile = "another assignment"
```

If the comment is used with a Python annotation, the comment should be used before the annotation,
for example:

```python
    # noinspection PyPep8Naming
    @classmethod
    def some_UpperCaseFunction() -> None
        pass
```

### Unresolved Reference ###

There are cases where an IDE such as PyCharm cannot determine whether called code exists.
The following example is for Qt user interface code.
It is OK to disable specific warnings because otherwise the IDE warning list may be overwhelming
and make it difficult to focus on warnings that are important.

```python
    # Use the following because connect() is shown as unresolved reference in PyCharm
    # noinspection PyUnresolvedReferences
    self.Menu_File_New_CommandFile.triggered.connect(self.ui_action_new_command_file)
```

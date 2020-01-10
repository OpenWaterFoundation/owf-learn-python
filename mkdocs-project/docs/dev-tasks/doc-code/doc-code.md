# Development Task / Documenting Python Code

Code documentation is important to memorialize the knowledge about the code.
Code that is not documented is more difficult to understand when maintaining and enhancing the code.

This documentation contains the following sections:

* [Inline Comments](#inline-comments)
* [Multi-line Quoted Commments](#multi-line-quoted-commments)
* [Module/Function/Class/Method Comments Using Docstrings](#modulefunctionclassmethod-comments-using-docstrings)
* [Automating Code API Document Creation Using Sphinx](#automating-code-api-document-creation-using-sphinx)

## Inline Comments

Inline comments are simply comments in the code to document logic, explain variables, etc.
These comments should be used to annotate code so that the Python syntax is understandable.
One form of the comments is using the hash (`#`) character, for example:

```python
# Can use to provide a multi-line comment
# or place comment after a statement as shown below.
a = 1 # Initialize a to first index
```

## Multi-line Quoted Commments

Multi-line comments can also be specified using three single or double quotes surrounding the commented text.
The surrounding quotes must match.  For example:

```python
'''
This module prints a random number to the screen.
The range of values is -1.0 to 1.0.
'''
```

## Module/Function/Class/Method Comments Using Docstrings

A Docstring can be used to document a module, function, class, or method.
The Python interpreter sets the `__doc__` special attribute for the object to the Docstring and can therefore be used in 
interactive development environment tools to display fundtion usage.
See the official specification: [https://www.python.org/dev/peps/pep-0257/](https://www.python.org/dev/peps/pep-0257/).
The following illustrates a simple example:

```python
def max(a,b):
  '''
  Return the maximum of two numbers.

  a -- the first number
  b -- the second number
  
  '''
```

## Automating Code API Document Creation Using Sphinx

The Docstring specification, although useful, is basic.  It is often desirable to have more extensive documentation.
The Sphinx software ([http://www.sphinx-doc.org/en/stable](http://www.sphinx-doc.org/en/stable)) is a tool to automate creation of HTML navigable documentation from code comments.

More guidance will be added later to explain how to use Sphinx.

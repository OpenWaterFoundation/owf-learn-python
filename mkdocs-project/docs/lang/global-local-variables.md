# Global Versus Local Variables

Programmers often make the mistake of using global variables for data management.
Although this may make sense in a simple program, global data will generally lead to maintenance issues as a program becomes more complex.

This documentation contains the following sections:

* [The Concept of Scope](#the-concept-of-scope)
* [Global Variables](#global-variables)
* [Local Variables](#local-variables)
* [Best Practices](#best-practices)

## The Concept of Scope

Scope means the extent within a program that a variable is recognized.
A global variable is recognized throughout the entire program.
A variable that has scope within a function is only recognized in the function.
The extent of the scope depends on where and how a variable is declared.

## Global Variables

A global variable in Python is declared at the top level of a module and not within any function.
The global variable will only be global within the module and not across modules.
For example:

```
import datetime

# Global variable containing the current time
currentTime = datetime.datetime.now()

def printCurrentTime():
  '''Print the current time with default formatting.'''
  print("Current time: " + str(currentTime))
  return

# Now print the current time
printCurrentTime()
```

In the above example, the `currentTime` variable is recognized inside the `printCurrentTime` function because it has global scope, and the output is:

```
Current time : 2016-10-10 14:48:43.394564
```

It is often necessary to use global variables in programs to hold global state information such as the starting folder on the computer.
However, called functions should not rely on the global variable and should instead use variables declared within the function or passed to the function.

## Local Variables

Local variables are recognized in the scope that they were declared.  For example, the following illustrates how a local format string is used to format the current date.


```
import datetime

# 
currentDateTime = datetime.datetime.now()

def printCurrentDate(currentDateTime2):
  '''
  Print the current date using YYYY-MM-DD format.

  currentDateTime2 -- current date/time as Python datetime object.
  '''
  # Use the Python formatting features
  print("Current date: %s-%s-%s" % (currentDateTime2.year, currentDateTime2.month, currentDateTime2.day) )
  return

# Now print the current date
printCurrentDate(currentDateTime)
```

Output from the above is `Current date: 2016-10-10`.
Note that in the above example the global variable name `currentDateTime` is different than the name `currentDateTime2`in the function parameter list.
If they were the same, the local variable would take precedence.
If a new declaration of a variable in a function should refer to the local variable, declare it as follows (otherwise `a` will be local in the function).
However, use of `global` is discouraged.

```python
a = 0 # Global variable
def someFunction():
  gobal a # Use the global variable rather than declaring a new local variable
  a = 5
  print("a="+str(a))
```

## Best Practices

The following are some best practices related to global data:

* Try to minimize the use of global data.

* If global data do need to be used in a program, try to isolate to the main program, and then pass as parameters to functions.
An exception might be when command line parameters are passed, in which case the parse function may need to
override global variables with values that were specified on the command line.

* If global data are needed in library modules, for example to store data to improve performance, encapsulate the data
to minimize potential conflict with other code in the module.

* Minimize directly referencing global data in functions.  Pass the data into functions as parameters.
The exception is "setter" and "getter" functions that manipulate the global data.

* If extensive data need to be passed to functions, consider using a class to group the data into an object.

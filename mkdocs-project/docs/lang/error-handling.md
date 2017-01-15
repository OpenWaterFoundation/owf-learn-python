# Error Handling

Error handling is one of the most important concepts in software development.
Errors that are not handled will result in ungraceful software exits.
Errors that are gracefully handled also need to be logged or otherwise made known to the user so that corrective action can occur.
Corrections may include fixing bad program input or fixing a software bug.

This documentation contains the following sections:

* [Design Considerations](#design-considerations)
* [Function Return Status](#function-return-status)
* [Exceptions](#exceptions)
* [Logging Exceptions](#logging-exceptions)

## Design Considerations

Error handling can be implemented in various ways, with a few options described below.
The basic approach is to detect a problem, handle the problem, and return logic flow gracefully to calling code.
In some cases an error is fatal and the program should stop.
In other cases, the progam can continue, perhaps with notification to the user.
The degree of notification depends on whether the error is expected as normal behavior or is out of the range of normal conditions.
For example, it should be expected that code that processes files may encounter cases where files are missing.

Good code recognizes the potential for errors and handles gracefully.
This may mean that a significant amount of code is devoted to checking input and implementing error handling.
However, the alternative is unfriendly, unusable software.
For example, a function that processes a file should check for file existence and handle missing or mal-formatted files.
A function that performs math operations should detect and handle division by zero.
Leap years should be handled gracefully without generating errors in the first place, rather than having incomplete code that generates exceptions.
The programmer is not off the hook if they implement exception handling as described below - the error handling should provide useful feedback.

## Function Return Status

Basic error handling for functions includes using a return status to let calling code know whether the function was succesful.
This may be appropriate for basic functionality but is limited. Using exceptions as in the next section is generally more useful.

For example, a function might return an integer to indicate its status, with 0 meaning success and other values corresponding to error states.
A function to remove a file might return 0 if the remove is successful, 1 if file did not exist, 2 if permissions did not allow removing, etc.
This form of error handling can become complex because errors have to be coded and decoded, with corresponding messages.
Of course, a general message could be printed if the status is non-zero, but that may not be helpful.

This approach for error handling is often too limiting in many cases.  See the discussion of Exceptions for an alternative.
However, many programming languages do utilize an exit status from the main program because inter-language error handling must rely on simple concepts
like a numerical exit status or a printed status string.

## Exceptions

Exceptions are unexpected conditions that occur in the logic of a program.
Exception objects are "thrown" by the Python interpreter when an issue is detected, and have a specific type.
For example, trying to use a number variable type when a string is expected may generate a TypeError.
The Exception occurs at a point in the software and "travels up" to the main program.  This is the "Exception stack" or call sequence
that is printed when Python detects that it cannot continue.
Exceptions are "caught" by type, at which time an appropriate action can be taken.
If an Exception type is not caught in one level of code, it will continue to travel up the stack until it is caught or the Python interpreter catches at the main level.
Exceptions objects have the same parent object `Exception`, which allows a cascading sequence of catches culminating with catching the most generic type.
The following illustrates a simple case where an exception is generated (thrown) and caught using the default exception handler (no specific exception type is caught).

```
try:
  x = 1/0
except:
  print("Division by zero:)

```

The `try` block code can be nested (exception handling inside of exception handling), used in loops, etc.
The exception can be handled by continuing a loop, returning from a function, throwing another exception, etc.,
as appropriate for the code logic.  See the logging section below for guidance on error handling and logging approach.

For more information for Python 2, see:

* [Errors and Exception](https://docs.python.org/2/tutorial/errors.html).
* [Built-in exceptions](https://docs.python.org/2/library/exceptions.html).

For Python 3, see:

* [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

## Logging Exceptions

If logging is implemented for the program, then exceptions should be loggged as warning or error messages.
This is particularly useful to allow the log file to be provided software developers so they can debug an issue.
See the following for information about logging exceptions:  [https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/](https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/)

It is useful to print the exception stack trace.  See the following for information:

* Python 2 - [https://docs.python.org/2/library/traceback.html](https://docs.python.org/2/library/traceback.html)

* Python 3 - [https://docs.python.org/3/library/traceback.html](https://docs.python.org/3/library/traceback.html)

An example for how to print the exception stack trace is as follows
(see [http://stackoverflow.com/questions/5191830/best-way-to-log-a-python-exception](http://stackoverflow.com/questions/5191830/best-way-to-log-a-python-exception)):

```python
import logging
try:
    1/0
except Exception as e:
    logging.exception("Division by zero")
```

The above `logging.exception` call will print the stack trace whereas `logging.warning` and `logging.error` will print a simple message.

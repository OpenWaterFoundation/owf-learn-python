# Logging

Logging is an important feature of software and a practice of software developers that facilitates debugging and troubleshooting.

## Logging Overview

Logging is the practice of writing messages to one or more output streams to record program progress and issues.
Output streams include standard output (stdout, the output window, or console),
standard error (stderr, similar to standard output but used for errors), and output file.

Logging is implemented by utilizing the Python logging module, which collects messages from running code,
determines whether the messages should be logged (based on logging configuration), and then directs the log messages to the
proper output stream(s).

Logging is an alternative to the built-in `print()` function in Python, which prints to the console.
However, printing to the console may be sufficient in some cases.
One issue with printing to the console is that it can greatly slow down the program due to using graphical resources.
If extensive logging is printed to the console, the output may need to be redirected to a file anyway because it exceeds the window scroll buffer
(for example `python script.py > output.log`).
Consequently, if the output needs to be redirected to a file, then a log file may as well be used.

The Basic Logging Tutorial mentioned below provides guidance for implenting logging.

## Python 2 Logging

Logging in Python 2 occurs using the logging facility.  See the following:

* [Logging API reference](https://docs.python.org/2/library/logging.html)
* [Basic Tutorial](https://docs.python.org/2/howto/logging.html#logging-basic-tutorial)
* [Advanced Tutorial](https://docs.python.org/2/howto/logging.html#logging-advanced-tutorial)
* [Logging Cookbook](https://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook)

## Python 3 Logging

Logging in Python 3 occurs using the logging facility.  See the following:

* [Logging API reference](https://docs.python.org/3/library/logging.html)
* [Basic Tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
* [Advanced Tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
* [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)


# Logging #

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

Logging features are different for Python 2 and 3 - see the specific discussion for each.

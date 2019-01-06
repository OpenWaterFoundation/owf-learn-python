# Logging / Python 2 #

Logging in Python 2 occurs using the logging facility.  See the following:

* [Logging API reference](https://docs.python.org/2/library/logging.html)
* [Basic Tutorial](https://docs.python.org/2/howto/logging.html#logging-basic-tutorial)
* [Advanced Tutorial](https://docs.python.org/2/howto/logging.html#logging-advanced-tutorial)
* [Logging Cookbook](https://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook)

## Working Simple Example ##

In most cases, it is desirable to log a minimal number of messages to the console to indicate software progress,
and log more messages to a log file as an artifact of processing and to facilitate troubleshooting.
The log file will typically be created in the folder where a program was run,
or a pre-defined location consistent with some implemented standard process.
One option is to create the log file in a default location (current folder or some predefined folder) and provide
a command line parameter to override.

The following example builds on examples in the [Python 2 Logging HOWTO](https://docs.python.org/2/howto/logging.html#logging-basic-tutorial),
with some minor modifications.
The log file is restarted each time the program is run.

* [View main module code](example-logging2/example-logging2.py).
* [View library module code](example-logging2/mylib.py).

The resulting output is as follows:

```
2016-10-31 12:49:14,351 INFO: Started
2016-10-31 12:49:14,351 INFO: Doing something
2016-10-31 12:49:14,351 INFO: Finished
```

## Advanced Logging ##

The simple example above relies on defaults and simple logging behavior.
More advanced logging, such as control of levels for different modules, must implement advanced logging features of Python.
See the resources at the top of this page for more information.

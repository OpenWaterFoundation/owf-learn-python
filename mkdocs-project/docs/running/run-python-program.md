# Running a Python Program #

* [Specify Python Interpreter](#specify-python-interpreter)
* [Main Entry Point in Python Program](#main-entry-point-in-python-program)
* [Graceful Exit](#graceful-exit)
* [Create a Script to Run Python or a Python Program](#create-a-script-to-run-python-or-a-python-program)

----------------

## Specify Python Interpreter ##

Python programs with source code in files with .py extension
can be compiled, but for general purpose use and transparency are distributed as text in the original files.
A Python program is run by specifying the main Python program filename as the first command line parameter to the interpreter:

```bash
python hello-world.py
```

where the hello-world.py file contains:

```python
print("Hello world")
```

## Main Entry Point in Python Program ##

The interpreter will execute the Python program from top to bottom.  If the code does not contain any functions and simply 
contains Python commands, then those commands are executed in sequence.
This is appropriate for very simple programs or modules;
however, in most cases the program will be complex enough to require functions.

When the Python interpreter reads a source file, it defines a few special variables.  If the interpreter is running the program
as the main file (as specified on the command line when starting Python), the interpreter sets a special `__name__` variable
to have a value of "\_\_main\_\_".  If the module is imported and executed, then `__name__` is set to the module name.
This allows the following syntax to be used in the program file:


```code
def main():
	'''
	Main program...
	'''
	# The following are not required...just an example
	# Parse command line parameters
	parseArgs() 
	# Initialize for run
	initialize()
	# Insert some logic here if not handled in called function
	# Close down
	shutdown()
	return
	

if ( __name__ == "__main__" ):
	# Run the main function
	main()
```

## Graceful Exit ##

Need to discuss here graceful exit so that calling program can check the exit status for success or failure.

## Create a Script to Run Python or a Python Program ##

In many cases, Python scripts can be run using the default Python that is recognized for an operating system (often the last one that was installed
because the installation procedure will update the `PATH` environment variable).  However, it may be
appropriate to specify a different version for a task and in particular on Windows it may be necessary to use `py` to specify the Python version.

It often makes sense to create a script to use the correct Python version, specify the correct script to run, and provide
command line parameters.  This helps simplify command-line syntax for users.
The following environment variables control the Python execution environment and can also be configured,
for example to specify the location of custom modules:

* `PYTHONPATH` - tells the Python interpreter where to locate the module files imported into a Python program.
It should include the Python source library folder and the folders containing Python source code.  This variable may be set by the installer.

* `PYTHONSTARTUP` - specifies the path to an initialization file containing Python code that is executed every time the interpreter starts up.

It may be helpful to understand the startup environment.  Run the following Python program to print environment information.

```python
# Print PYTHONPATH folders
import sys
print sys.path
```

Example output from running `python` on Cygwin and executing the above is:

```
$ python
Python 2.7.10 (default, Jun  1 2015, 18:05:38)
[GCC 4.9.2] on cygwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print sys.path
['', '/usr/lib/python2.7/site-packages/logilab_common-0.62.0-py2.7.egg', '/usr/lib/python27.zip', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-cygwin', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/lib/python2.7/site-packages']
>>> quit()

```

From the above it can be seen that the supporting library files are installed in /usr/lib/python2.7.

A simple `bash` configuration/run script may be similar to the following.


```bash
#!/bin/bash
#
# Specify the Python interpreter to run
set PYTHON=/usr/sbin/python3
# Set the PYTHONPATH so that third party libraries can be found in the installation folder for the specific Python version:
set PYTHONPATH=/some/new/path:$PYTHONPATH
# Now run the python script and pass command line parameters
# - need to make sure file is found, perhaps by using absolute path or path from $HOME
%PYTHON% hello-world.py $*

```

where the hello-world.py file contains:

```python
print("Hello world")
```

or, to use built-in system functionality to run the python3 interpreter automatically, which may be appropriate for simple scripts:


```bash
#!/usr/bin/python3

print("Hello world")
```


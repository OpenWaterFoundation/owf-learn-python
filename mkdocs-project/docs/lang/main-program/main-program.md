# Python / Main Program and Working Directory #

* [Check `__name__` to Detect Main Program](#check-name-to-detect-main-program)
* [Determine Software and Working Directories](#determine-software-and-working-directories)
* [Exiting the Program](#exiting-the-program)

--------------

## Check `__name__` to Detect Main Program ##

The entry points into a Python program can be indicated by adding the following code to a Python file:

```python
   if __name__ == '__main__':
       # Main program
       print("In main program")
```

The `__name__` is set to `__main__` when the file is being run directly.
Otherwise, `__name__` is set to the module that was imported,
which gives an indication of the scope of the code.

## Determine Software and Working Directories ##

It is often important to understand the working directory (folder)
for an application (location where software was run)
and the installation location for software.
These folders are useful for locating log, input, and output files for software.

Use the following to determine the locations:

```python
# Simple program to illustrate getting important folders

import os

# Main program entry point
if __name__ == '__main__':
    print("")
    print("Current working directory = " + os.getcwd())

    current_file = __file__
    print("Software installation directory = " + os.path.realpath(current_file))
```

Running the script from the parent folder of the script using Cygwin prints:

```sh
$> python3 main-program/get-folders.py

Current working directory = /cygdrive/C/Users/sam/owf-dev/Learn-Python/git-repos/owf-learn-python/mkdocs-project/docs/lang
Software installation directory = /cygdrive/C/Users/sam/owf-dev/Learn-Python/git-repos/owf-learn-python/mkdocs-project/docs/lang/main-program/get-folders.py
```

## Exiting the Program ##

All programs should exit with an appropriate exit status,
which allows calling software (including the operating system) to know whether the program ran successfully.
The exit status (or exit code) is an integer.
A zero value indicates success, whereas a non-zero value indicates an error and the value indicates the specific error.
Exit the program with code similar to:

```python
   # Exit with success status
   exit(0)
```

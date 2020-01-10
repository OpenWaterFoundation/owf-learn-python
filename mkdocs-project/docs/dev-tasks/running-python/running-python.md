# Development Task / Running Python #

This documentation explains how to run the Python software from the command line.

| **Step** | **Description** |
| -- | -- |
| **Prerequisites** | |
| [Dev Env - Install Python](../../dev-env/python/python.md) | Ensure that Python has been installed. |
| [Dev Env - Command Line](../../dev-env/command-line/command-line.md) | Understand command line tools. |
| **Information** | |
| [Introduction (see below)](#introduction) | Introduction for running Python on the command line. |
| ![windows](../../images/windows-32.png) See below:  [Run Python on Windows](#run-python-on-windows) | Run Python on the command line for Windows. |
| ![cygwin](../../images/cygwin-32.png) See below:  [Run Python on Cygwin](#run-python-on-cygwin) | Run Python on the command line for Cygwin. |
| ![gitbash](../../images/gitbash-32.png) See below:  [Run Python on Git Bash](#run-python-on-git-bash) | Run Python on the command line for Git Bash. |
| ![linux](../../images/linux-32.png) See below:  [Run Python on Linux](#run-python-on-linux) | Run Python on the command line for Linux. |

----------------------------

## Introduction ##

The Python interpreter is run on the command line to run Python commands and programs.
For production software, the interpreter is typically launched using a batch file or script.

## ![windows](../../images/windows-32.png) Run Python on Windows ##

To run the Python interpreter on the command line, first open an appropriate command line window for Windows,
such as the Windows ***Command Prompt***.

Multiple Python versions may have been installed on the Windows computer and the `PATH` environment
variable may or may not be configured.  Even if configured, the `PATH` will only allow the first
matching Python to be found.  More recent versions of Python will install into user files
and will also install the `py` (`py.exe`) program in Windows system files.
The `py` program is able to find multiple Python installations from default installation locations,
and will by default run the latest Python.
To check the latest Python version that is found:

```sh
> py --version
Python 3.7.2
```

To start and then exit the Python interpreter, use the `quit` command:

```sh
> py
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

## ![cygwin](../../images/cygwin-32.png) Run Python on Cygwin ##

Cygwin has access to Windows programs and also Python installed in the Cygwin environment used by Cygwin.
Therefore, by default, the `PATH` environment variable will be used to locate the
Python program to run, either `py`, `python`, or `python3`, depending on the Python versions that have been installed.

To avoid confusion, create a Windows batch file or Linux script to run the desired Python.

## ![gitbash](../../images/gitbash-32.png) Run Python on Git Bash ##

Git Bash has access to Windows programs and also Python installed in the MinGW environment used by Git Bash.
Therefore, by default, the `PATH` environment variable will be used to locate the
Python program to run, either `py`, `python`, or `python3`, depending on the Python versions that have been installed.

To avoid confusion, create a Windows batch file or Linux script to run the desired Python.

## ![linux](../../images/linux-32.png) Run Python on Linux ##

To run the Python interpreter on the command line, first open an appropriate command line window for Linux,
such as terminal window that runs Bash shell.

Python on Linux is typically available as the `python` program and is installed in system folders (not user folders).
Depending on the system, `python` might run Python 2 or Python 3.  The `python3` program may be available for Python 3.
To check the Python version, run:

```sh
$ python --version
Python 2.7.13

$ python3 --version
Python 3.5.3
```

To start and then exit the Python interpreter, use the `quit` command:

```sh
> python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

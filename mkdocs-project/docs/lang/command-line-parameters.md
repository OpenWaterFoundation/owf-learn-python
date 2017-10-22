# Python Language / Command Line Parameters #

The Python interpreter can be run by specifying command line parameters (also called arguments).
In basic use, the first parameter is the name of the Python program file to run and subsequent parameters are data to pass to the program.
Parameters may also be specified prior to the program file name to control Python.  To see a full list of Python interpreter command parameters,
run `python -h` or `python --help`.  For example `python -v` will run in verbose mode and `python --version` will print the version.
Running `python -v helloworld.py` will run the specified program in versbose mode.

It is customary to write programs to accept command line parameters to allow flexibility in running the program so that input is not
hard-coded.  This takes more time but allows the program to be reused and combined with other programs to provide greater functionality.

This documentation contains the following sections:

* [Operating System Command Shell](#operating-system-command-shell)
* [Python Command Line Parameter Standards](#python-command-line-parameter-standards)
* [Getting the Value of Python Command Line Parameters (Basic)](#getting-the-value-of-python-command-line-parameters-basic)
* [Getting the Value of Python Command Line Parameters (Advanced)](#getting-the-value-of-python-command-line-parameters-advanced)

## Operating System Command Shell ##

Every operating system offers a command line shell (or "console" or "terminal").  The operating system kernal runs continuously and manages processes,
some of which are transitory and some of which are "services" that start when the computer starts and run continuously.
The kernal starts a command shell program when requested.

On Windows, typical command shells are cmd.exe (shown in Start menu as "Command Prompt") and Windows PowerShell.  For this documentation, it is assumed
that cmd.exe is most often used and that batch files with \*.bat filename extension are used to run Python programs.
After starting, the Windows command shell will display a prompt such as the folder name (e.g., `C:\Users\John`).
The prompt can be modified by setting the `PROMPT` environment variable.
For example, see:  [http://www.hanselman.com/blog/ABetterPROMPTForCMDEXEOrCoolPromptEnvironmentVariablesAndANiceTransparentMultiprompt.aspx](http://www.hanselman.com/blog/ABetterPROMPTForCMDEXEOrCoolPromptEnvironmentVariablesAndANiceTransparentMultiprompt.aspx).

On Cygwin and Linux, the "bash" command shell is often used, although other shells are available.
After starting, the bash window will display the prompt (e.g., `$`, folder name, or other string), depending on the value of `PS1`, `PS2`, and `PS3`
environment variables.  These environment variables can be set to create a customized shell, for example for a bundled software framework.
See the following for more information:  [https://wiki.archlinux.org/index.php/Bash/Prompt_customization](https://wiki.archlinux.org/index.php/Bash/Prompt_customization).

On Windows, the Windows Task Manager can be used to list running applications and will show `Command Prompt`.
On Cygwin/Linux, the `ps` command will list processes and the `bash` shell will be listed as `/usr/bin/bash`.

The command shell displays a prompt and then waits for user input, which is entered using the `Enter` key on the keyboard.
Typically running the `exit` command causes the shell to exit (window will go away).
The text that is typed before `Enter` is parsed by the command shell, using spaces and tabs as whitespace between tokens.
If the first token is recognized as an internal command of the shell, it is executed without trying to run any other program.
In this case additional tokens may also be used to modify the behavior of the internal command.

If the first token is not recognized as an internal command of the shell, then the folders in the `PATH` environment variable are searched to find the program to run.
On Cygwin/Linux use `which programName` to determine whether a program is in the `PATH`.  On Windows, use `where programName`.
You need to know the name of the program that will be run.
The remaining tokens on the command line are passed to the called program, using whitespace characters to split the tokens.
For example, if the program specified after the command prompt is `python --version`, then the `python` program is called with `--version` as the first command line parameter.
The following considerations should be kept in mind:

* *Chained program calls* - One program or script can call another.  In each case, the environment of the parent program provides environment variables to the called program.
This can impact the initial state of called programs.

* *Command line parameter expansion* - The command shell provides standard variable expansion functionality using wildcard characters.
For example, for Cygwin/Linux the `ls a*` command will list all files with `a` as the first character.
This expansion by default occurs in the command shell before calling the program.
In other words, the called program does not see a command parameter of `a*` but instead sees the expanded list of matching files.
Another expansion that occurs is to replace environment veriable references with the value of the environment variable.
For example, on Cygwin/Linux `ls $HOME` will list the contents of the user's home directory.
To avoid expansion from happening, the wildcard character must be protected/escaped.  See the next two bullets.

* Filenames with spaces and backslashes.
Filenames passed to a program that include spaces can be problematic because the command shell splits the name into multiple tokens.
Baskslashes used in Windows can be problematic because the backslash is a special character that "escapes" the following character.
For example `\*` can mean "I want the literal asterisk character, not wildcard behavior", but handling is different between operating systems.
One solution is to avoid using folders and filenames with spaces and as much as possible handle input filenames gracefully whether a
Python program is run on Windows or Cygwin/Linux.
See the next bullet.

* Protecting from command parameter expansion and handling white space.
On Cygwin/Linux, single quotes around a command line parameter can be used to prevent the parameter from any expansion,
and double quotes around a parameter will allow for expansion but treat the parameter as a single value when passed to the called program
(space will be included in the parameter).  On Windows, double quotes around the parameter allow expansion and will keep spaces.

## Python Command Line Parameter Standards ##

When creating a Python program, it is best to use standard command line parameters.
Command line parameter standards are available but are typically very technical (see: [http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html)).
A basic summary is as follows:

* Use Linux-style format for command parameters, which prefix parameters with dashes rather than Windows /.
Dashes are more universal and avoid confusion with path separators.

* If the command parameter is a single character, use a single dash, for example to print the version:  `-v`.

* If the command parameter is longer than a single character, use two dashes, for example to print the version:  `--version`.

* Specify the value associated with a command line parameter using an equals sign, for example `-inputFile=nameOfFile` or as the following parameter `-inputFile nameOfInputFile`

## Getting the Value of Python Command Line Parameters (Basic) ##

Command line parameters are stored in an array `sys.argv` and can be printed using the following:

```python
import sys

for arg in sys.argv:
  print arg
```

The first argument (`arg[0]`) contains the name of the Python file that is being run.  All other array values contain the command line
parameters that were specified on the command line.  The `sys.arg` array can be manually processed to retrieve parameter values
and set in variables; however, utility functions are available to do this work.  See the next section.

## Getting the Value of Python Command Line Parameters (Advanced) ##

It is generally best to create a standard command line parsing function that uses built-in Python capabilities.
The older getopt and newer argparse modules are distributed with Python and other modules are also available, for example:
[https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/](https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/).

The following are references for several options:

* [getopt Reference](https://docs.python.org/2/library/getopt.html)
* [argparse Reference](https://docs.python.org/2/library/argparse.html#module-argparse)
* [argparse 2 Tutorial](https://docs.python.org/2/howto/argparse.html#id1)
* [argparse 3 Tutorial](https://docs.python.org/3/howto/argparse.html#id1)

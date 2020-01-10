# Training Session / Static Data #

This training session explains how to use static data to provide approved data values
and constrain software behavior.

**<p style="text-align: center;">
Training Session Summary
</p>**

| **Lesson/Task** | **Description** |
| -- | -- |
| **Prerequisites** | As needed... | 
| [Dev Env - Install Python](../../dev-env/python/python.md) | Ensure that Python has been installed. |
| [Dev Env - Workspace](../../dev-env/workspace/workspace.md) | Determine a workspace for development files. |
| [Dev Env - Command Line](../../dev-env/command-line/command-line.md) | Use a command line to run programs. |
| [Dev Task - Editing Code](../../dev-tasks/editing-code/editing-code.md) | Editing Python code. |
| [Dev Task - Running Python Program](../../dev-tasks/running-program/running-program.md) | Run a Python program. |
| **Lesson Sequence** | |
| See below: [Introduction](#introduction) | Introduction to static data. |
| See below: [Module Data](#module-data) | Static data in module. |
| Language: [Enumerations](../../lang/enumerations/enumerations.md) | Enumerations. |

## Introduction ##

Programs must often use known values to control logic.
An extreme case is the `bool` variable type, which stores either `True`, or `False` (and `None`).
The use of static (unchangeable) values ensures that software can only use accepted values.

Why use static data?  Consider the following code:

```python

   def some_function(dayofweek):
       if dayofweek == "Monday":
           # do something
           pass
       elif dayofweek == "Tuesday":
           # do something
           pass

   # Call the above function
   some_function("WEDNESDAY")
```

In the above logic, the code in the function will not properly handle the day `WEDNESDAY`
because it is not a recognized string,
and even if a supported day is specified, the spelling of the string must match exactly.
The function could of course be modified to do a case-independent comparison.

Python provides a number of options for defining static data values.
However, because Python is inherently a language that uses public scoping,
there are cases where data that appear to be static can actually be changed.
In most cases, this is not an issue, but it can cause unexpected behavior.

## Module Data ##

Static data values can be defined within a module.
Note that it is customary in many programming languages to use all uppercase variables for static data.
This approach is valid if modules with functions (not classes) are used.
For example, create a file `day_of_week.py` with the following content.

```python
# Day of week

MONDAY = "Monday"
TUESDAY = "Tuesday"
WEDNESDAY = "Wednesday"
THURSDAY = "Thursday"
FRIDAY = "Friday"
SATURDAY = "Saturday"
SUNDAY = "Sunday"
```

Then create a Python file as a main program.
Note that using the static values for days restricts the logic of the program
to use recognized values, but only as long as the programmer tries to follow the rule of using the module values.
This approach could use values of any data type.

```python
# Simple program to illustrate using module data as static data

import day_of_week

# Main program entry point
if __name__ == '__main__':
    # Want to control some logic by day
    today = day_of_week.MONDAY

    print("Doing tasks for " + today)
    if today == day_of_week.MONDAY:
        # Do some tasks for Monday
        pass

    # Actually, module data are not really static because variables can be modified
    day_of_week.MONDAY = "Friday"
    print("Monday after changing = " + day_of_week.MONDAY)
```

Run the program from the command line as follows:

```sh
$> python day_of_week_main.py
Doing tasks for Monday
Monday after changing = Friday
```

Because the defined values are module variables, they can be changed from
their original values, as illustrated by the last lines of the example main program.
Any changes would only apply to the local variable that is being assigned and
would not globally impact other code that uses the module.
Consequently, this approach is not totally safe.

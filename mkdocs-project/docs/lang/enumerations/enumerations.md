# Python Language / Enumerations #

The `Enum` (enumeration) in the `enum` module is a construct that is designed to define
specific values that control logic.
Enumerations can use any data type and `int` and `str` type are common.
Note that enumerations were added in Python 3.4.

See reference documentation:

* [Python `enum` module documentation](https://docs.python.org/3/library/enum.html)

The following example illustrates how to define an enumeration,
in this case a file named `DayOfWeekType.py`.
"CapWord" naming convention is recommended for the filename and enumeration, consistent with how classes are often named.
The convention of using "Type" at the end of the enumeration identifies the class as an enumeration.

```python
# Day of week enumeration

from enum import Enum


class DayOfWeekType(Enum):
    """
    Enumeration for day of week.
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

    def __str__(self):
        """
        Format the enumeration as a string - just return the value.
        This is needed because the default is to return the name as in MONDAY (uppercase).
        """
        return self.value
```

Create a main program to use the enumeration, named `DayOfWeekType_main.py`:

```python
# Simple program to illustrate using module data as static data

from DayOfWeekType import DayOfWeekType

# Main program entry point
if __name__ == '__main__':
    # Want to control some logic by day
    today = DayOfWeekType.MONDAY

    print("\nDoing tasks for " + str(today) + "\n")
    # Note that "is" is used for comparison rather than "==" although "==" will work
    if today is DayOfWeekType.MONDAY:
        # Do some tasks for Monday
        pass

    # Actually, module data are not really static because variables can be modified
    DayOfWeekType.MONDAY = "Friday"
    print("Monday after changing = " + str(DayOfWeekType.MONDAY))
```

Running the program prints the following:

```sh
$> python3 DayOfWeekType_main.py

Doing tasks for Monday

Traceback (most recent call last):
  File "DayOfWeekType_main.py", line 17, in <module>
    DayOfWeekType.MONDAY = "Friday"
  File "/usr/lib/python3.6/enum.py", line 361, in __setattr__
    raise AttributeError('Cannot reassign members.')
AttributeError: Cannot reassign members.
```

In this case, the enumeration behaves as desired and the `AttributeError` illustrates that
the enumeration value **cannot** be reassigned.
Therefore the enumeration is static and safe.

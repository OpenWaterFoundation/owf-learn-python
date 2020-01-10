# Python Language / Classes #

* [Introduction](#introduction)
* [Defining a Class](#defining-a-class)
* [`__init__()` Constructor Function](#__init__-constructor-function)
* [Other Built-in Functions](#other-built-in-functions)
* [Instance Methods](#instance-methods)
* [Class Data](#class-data)
* [Class Methods](#class-methods)
* [Public and Private Class Features](#public-and-private-class-features)

-------------------------

## Introduction ##

A Python `class` encapsulates data and functions (typically called "methods" when in a class).
The class definition (code) is used to instantiate (initialize) instances of the class,
which are called "objects".
In other words, instance x of class y results in an object.

See the following reference information:

* [Python documentation for classes](https://docs.python.org/3/tutorial/classes.html)

## Defining a Class ##

Python modules (files with names ending in `.py`) can contain data, functions, and classes.
Classes can be defined and imported from modules as needed.
For example, the following code imports a class `ClassA` defined in module file `modulex.py`:

```python
from modulex import ClassA
```

It is possible to define multiple classes in a module file and import the classes as needed.

However, it is common with other languages such as Java and C# to define one class per file.
Consequently, the approach taken for this documentation is to use one Python class per Python file.

Whereas "pythonic" conventions are to use lowercase and underscores for variables and functions
(e.g., `some_variable` and `some_function`),
`MixedCase` is recommended for class names.

To define a class, use syntax like the following.  For example, create a file `Station.py`
to define data collection stations.
Each class is defined using the `class` keyword followed by the class name.
It is recommended that the file name match the class name.

```python
import logging


class Station(object):
    """
    Station at which data are collected.
    """

    def __init__(self, station_id="", latitude=None, longitude=None):
        """
        Create a new Station instance.
        """

        # Station identifier
        self.station_id = station_id

        # Station coordinates
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        """
        Return a string representation of the station.
        """
        return str(self.station_id) + "," + str(self.longitude) + "," + str(self.latitude)

    def check_data(self):
        """
        Check the station data validity.
        """ 

        # Can use a logger or just print a message
        logger = logging.getLogger(__name__)

        error_count = 0
        if (self.station_id == None) or (self.station_id == ""):
            error_count += 1
            message = "station_id is not defined"
            print(message)
            logger.warning(message)
        return error_count
```

Do demonstrate use of the `Station` class, create a simple Python program such as the following `Station_main.py` program:

```python
# Simple program to illustrate using class

from Station import Station

# Main program entry point
if __name__ == '__main__':
    # Print a blank line
    print("")

    # Create a station with default data values
    station_a = Station()
    print("station_a=" + str(station_a))

    # Create a station with supplied data values
    id = "station_a"
    longitude = "45.00"
    latitude = "-106.00"
    station_b = Station("station_a",longitude,latitude)
    print("station_b=" + str(station_b))
```

Running the program displays the following:

```sh
$> python3 Station_main.py

station_a=,None,None
station_b=station_a,-106.00,45.00
```

## `__init__()` Constructor Function ##

The special `__init__()` function is used to construct an instance of the class, for example a `Station`.
This function should set all data variables associated with the class using notation:

```python
     self.variable = value
```

The `__init__()` function (method) and all other methods associated with the class should use a
first parameter named `self`, which is used by Python to associate the object instance with its methods.

If syntax such as `self.variable = value` is used elsewhere in the class and the variable was not
defined in `__init__()`, a warning will be generated.

Python does not allow overloading functions.
For example, other languages would allow overloaded constructors like:

```
    def __init__(self):
        self.station_id = ""
        self.latitude = None
        self.longitude = None

    def __init__(self, station_id=None, longitude=None, latitude=None):
        self.station_id = station_id
        self.longitude = longitude
        self.latitude = latitude
```

Instead, Python achieves overloading by allowing default parameter values to be provided,
as shown in the second `__init__()` function in the above example.
Therefore, class constructor methods should be designed appropriately.

## Other Built-in Functions ##

In addition to `__init__()` constructor function, Python defines a number of built-in functions on all objects.
The example `Station` class has a parent object `object`, which is the default if no parent is specified.
One or more classes can be specified as the parent for the class, to allow defining more complex classes.
Built-in functions can be overridden in the class.  For example, the `Station` example class overrides
the `__str__()` function in order to convert the `Station` to a string.
This is required, for example, when outputting the `Station` in a `print()`.

* See:  [List of built-in functions](https://docs.python.org/3/library/functions.html).

## Instance Methods ##

Functions defined in a class using the first parameter `self`, as follows,
can be called using an instance of the class (an object reference):

```python
    def some_function(self,parameter1,parameter2):
        """
        A function defined for the class.
        """
```

Within the class, the function should be called as follows, in order to operate on itself:

```python
   self.some_function(parameter1,parameter2)
```

Outside of the class, the function should be called using an instance of the class, as follows:

```python
   station_a = Station()

   station_a.check_data()
```

In all cases, Python will automatically pass the `self` parameter to class methods
(`self` does not need to be specified as a parameter to the method).

## Class Data ##

It is often useful to include data in a class to be maintained global to the class.
This is similar to data global to a module.
To use class data, define the data outside the `__init__()` method,
for example see the variation of `Station` defined in `Station_class_data.py`:

```python
import logging


class Station(object):
    """
    Station at which data are collected.
    """

    # Example of class data
    default_elevation = 0.0

    def __init__(self, station_id="", latitude=None, longitude=None):
        """
        Create a new Station instance.
        """

        # Station identifier
        self.station_id = station_id

        # Station coordinates
        self.latitude = latitude
        self.longitude = longitude
```

The following main program illustrates using the above class:

```python
# Simple program to illustrate using class with class data

from Station_class_data import Station

# Main program entry point
if __name__ == '__main__':
    # Print a blank line
    print("")

    # Print default elevation
    print("default_elevation=" + str(Station.default_elevation))
```

Running the program results in the following:

```sh
$> python3 Station_class_data_main.py

default_elevation=0.0
```

## Class Methods ##

Similar to class data, it is often helpful to create methods for a class that
can be run without creating an instance of the class.
The alternative would be to create a separate module or class that operates on an instance of the class.

The following variation of the `Station` class illustrates the use of a class method that can be
called to read stations from a file.

```python
import logging


class Station(object):
    """
    Station at which data are collected.
    """

    # Example of class method

    def __init__(self, station_id="", latitude=None, longitude=None):
        """
        Create a new Station instance.
        """

        # Station identifier
        self.station_id = station_id

        # Station coordinates
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def read_stations(cls, filename)
        """
        Read a list of stations from the file.
        """
        stations = []
        # Here would write code to read a file,
        # declare instances of Station, add to a list, and return the list
        return stations

```

In the above example, the `@classmethod` annotation before the `read_stations` function causes the
following method to be treated as a class method.
The method can then be run similar to:

```
    filename = 'path to file'
    stations_from_file = Station.read_stations(filename)
```

## Public and Private Class Features ##

The Python language is inherently public by design.
Some Python conventions do exist for hiding data.

See:  [Python documentation for private variables](https://docs.python.org/3/tutorial/classes.html#private-variables)

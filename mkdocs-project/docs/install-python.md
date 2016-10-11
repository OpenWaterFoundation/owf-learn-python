# Install Python

Python can be downloaded and installed from the Python website ([python.org/downloads](https://www.python.org/downloads/)).
In general, you should choose the latest 2.x or 3.x version, and the choice may depend on integration with an existing environment.
For example, an important application may have been developed in one version or the other.
To determine what version of Python is already installed, open a command shell in the preferred computer operating system
(Cygwin, Linux, or Windows), and check for an installed and default version:

```bash
$ python --version
Python 2.7.2
```

Even if nothing is listed, Python may still be installed on the system, but most likely not, because generally at least one installed
version will be the default and will be included in the `PATH` environment variable.  Refer to the following sections for
differences between operating systems.

Any changes to the Python installation environment, such as installing third-party packages, will install into the Python software file
location based on the version of Python that was configured and run in the first place.  Be careful when working on a system that includes
multiple Python versions because care needs to be taken to install components for the correct version.

## Bundled Installations

Python may be distributed with software frameworks that depend on Python and need to control its installation so as to
not break the framework.
Bundled versions of Python are generally not configured as the default installation on a system and often require that a startup script
is run to configure the Python environment.  Examples of bundled Python distributions include:

* Esri ArcGIS Geographic Information System ().  On Windows and ArcGIS 10.4, Python is installed in the C:\\Python27 folder and includes C:\\Python27\ArcGIS10.4.
The ArcGIS software provides configuration tools to select the Python that is used.
* QGIS ([https://www.qgis.org/en/site/forusers/download.html](https://www.qgis.org/en/site/forusers/download.html)) - open source Geographic Information System
(for example Python may be installed in the C:\\OSGeo4W64\apps\Python27 folder and the Python environment is initialized by running C:\\OSGeo4W64\bin\python.exe)


## Cygwin Installation

Python for Cygwin ([https://cygwin.com/install.html](https://cygwin.com/install.html)) is installed by selecting the Python interpreter in the install package listing.
The Python program is installed as /usr/bin/python or /usr/bin/python3 and supporting files are installed in /usr/lib/Python2.7/ and /usr/lib/Python3.4/.
The latest supported Python for each major version is installed when the Cygwin installer is run.

## Linux Installation

Python for Linux is installed by following the instructions on the Python download page.
The Python program is installed as /usr/bin/python or /usr/bin/python3 and supporting files are installed in /usr/lib/Python2.7/ and /usr/lib/Python3.4/.

## Windows Installation

Python for Linux is installed by following the instructions on the Python download page.
Python will install in the top-level folder C:\\Python27 or C:\\Python34, for example.
This allows the desired version of Python to be used based on component dependencies.
In general you will want to install a recent version (in the 2 or 3 major version) and stick with that until there is a reason to change,
or you have time to upgrade and ensure that third-part components are also updated.

## Install pip (or Other Package Installer)

The pip software is used to install Python packages and is the preferred installation tool since older tools such as easy_install
do not support current conventions.  Therefore, in order to install third-party packages, install pip first.  To check for whether pip is already installed:

```bash
$ pip --version
```

If not installed, install with:

```bash
$ python -m ensurepip
```

## Install Third-party Packages

Third party packages typically have their own websites with installation instructions.  Follow those instructions within the cofigured
Python environment that is to receive the installation.  If necessary, check the Python version first to ensure compatibility with the
module.

## Create a Script to Configure the Python Environment

In many cases, Python scripts can be run using the default Python that is recognized for an operating system (often the last one that was installed
because the installation procedure will update the `PATH` environment variable).  However, it may be
appropriate to specify a different version for a task.  In any case, it may make sense to create a script to run the Python program so that the user does not
need to remember command-line syntax.  The example below runs a Python program on Cygwin/Linux.
A similar .bat file could be created for Windows, in which case the `PATH` could be changed to specify the preferred Python at the start of the `PATH`.
The following environment variables control the Python execution environment:

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

A simple configuration/run script may be similar to the following.


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
#!/usre/bin/python3

print("Hello world")
```
## Install Interactive Development Environment

An Interactive Development Environment (IDE) is helpful for development because it provides an integrated edit/run/test/build/deploy environment.
There are many Python developer environments.  The following are several that may be appropriate.  It is important to recognize the impacts that an IDE
will have on file structure, project files committed to repository, etc.  Other developers may use a different tool that will introduce other artifacts
into the development environment.

* Simple text editor and command line.  This is the default case and may be appropriate especially when troubleshooting a program on a remote environment
where full developer environment cannot be installed.

* IDLE - distributed with Python.  Start by running `idle` on the command line.

* [PyCharm](https://www.jetbrains.com/pycharm/download) - Integrated Python development environment with commerical and community editions.

* [WingIDE](https://wingware.com/) - commercial product.

* [Sublime](https://www.sublimetext.com/) - text editor with features to supporty Python projects.

* [Eclipse PyDev](http://www.pydev.org/) - Python plugin for Eclipse.

# Development Environment / Python Software

Python can be downloaded and installed from the Python website ([python.org/downloads](https://www.python.org/downloads/)).
If possible, install and use the latest 3.x version.  However, the choice of Python version may depend on integration with an existing environment,
and in some cases Python may be bundled with a software product.
The last Python to be installed will generally be reflected in `PATH` environment variable,
if the option to update the `PATH` was specified at install time, meaning that running `python`
on the command line will run the last Python that was installed (not necessarily the newest version).

To determine what version of Python is already installed and will run by default,
open a command shell in the target computer operating system
(Cygwin, Linux, or Windows), and check for the installed and default version:

```bash
$ python --version
Python 2.7.2
```

Even if nothing is listed, Python may still be installed on the system and may not have been configured in the `PATH`.
Refer to the following sections for instructions to install Python on different operating systems:

* [Bundled Python Installations](#bundled-python-installations) - when Python is packaged with a software product and is run independent of Python installed on the operating system
* [Virtual Python Environment](#virtual-python-environment) - used to isolate Python package installs from operating system Python install
* [Cygwin Python Installation](#cygwin-python-installation) - instructions to install Python on Cygwin
* [Linux Python Installation](#linux-python-installation) - instructions to install Python on Linux
* [Windows Python Installation](#windows-python-installation) - instructions to install Python on Windows

## Bundled Python Installations

Python may be distributed with software products that depend on Python and need to control its installation so as to
not break the products.
This approach may be taken where significant Python libraries have been developed to integrate with the product.
Bundled versions of Python are generally not configured as the default installation on a system and often require that a startup script
is run to configure the Python environment.  Examples of bundled Python distributions include:

* [Esri ArcGIS Geographic Information System](http://www.esri.com/software/arcgis/arcgis-for-desktop), which includes
[ArcPy Python integration](http://pro.arcgis.com/en/pro-app/arcpy/main/arcgis-pro-arcpy-reference.htm).
On Windows and ArcGIS 10.4, Python is installed in the C:\\Python27 folder and includes C:\\Python27\ArcGIS10.4.
The ArcGIS software provides configuration tools to select the Python that is used.
* [Quantum GIS (QGIS)](https://www.qgis.org/en/site/forusers/download.html)) - open source Geographic Information System, which
includes [PyQGIS Python integration](http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)
(for example Python may be installed in the C:\\OSGeo4W64\apps\Python27 folder and the Python environment is initialized by running C:\\OSGeo4W64\bin\python.exe)

## Virtual Python Environment

Virtual environments are a newer approach that install Python packages
into an isolated folder so that the installation of add-on Python packages does not
impact Python installations on the computer.
Site packages in this case will not be installed with the Python software.
This option may also be appropriate in cases when administrative privileges are not available on the computer.
This option is not explored here but may be appropriate.  See:

* [Creating Virtual Environments](https://packaging.python.org/installing/#creating-virtual-environments)


## Cygwin Python Installation

Python for [Cygwin](https://cygwin.com/install.html) is installed by selecting the Python interpreter in the install package listing.
The Python program is installed as /usr/bin/python or /usr/bin/python3 and supporting files are installed in /usr/lib/Python2.7/ and /usr/lib/Python3.4/
(the version numbers will increase as newer Python versions are released on Cygwin).
The latest supported Python for each major version is installed when the Cygwin installer is run.

Use `python` to run Python 2 and `python3` to run Python 3.  Both are installed in `/usr/bin`.

## Linux Python Installation

Python for Linux is typically installed by following the instructions for the Linux distribution.
For example, see instructions:

* [Python on Debian Linux](https://wiki.debian.org/Python)

The Python program is typically installed as /usr/bin/python or /usr/bin/python3 and supporting files are installed in /usr/lib/Python2.7/ and /usr/lib/Python3.4/,
for example.  Consequently, the programs will typically be found in the `PATH`.

## Windows Python Installation

Python for Windows is installed by following the instructions:

* [Python Windows download page](https://www.python.org/downloads/) - general download page
* [Python Releases for Windows](https://www.python.org/downloads/windows/) - downloads for Windows
	+ Make sure to pick the desired Python version, for example pick latest Python 2.7 or 3.5
	+ Make sure to pick the desired operating system version, for example ***Windows x86-64 executable installer*** for Widows 64-bit
* [Using Python on Windows (Python 3)](https://docs.python.org/3/using/windows.html)
* [Using Python on Windows (Python 2)](https://docs.python.org/2/using/windows.html)

The Python documentation recommends installing Python in a shared location (not under User folder).
Python 2 will install in the top-level folder C:\\Python27 and Python 3 will install in C:\\Program Files.
When installing multiple versions of Python, the last installer to run when indicating that the `PATH` should be updated
will result in that version being found in the `PATH`.  Other versions would have to be run by specifying the install location,
or see the approach below.

Modern Python installations, when installed to the shared system location (not user files), will install the `py` program
in the Windows software location, `C:\Windows`, which is always in the `PATH`.
Verify that `py` is available as follows:

```
> where py

```


The `py` program will by default run the latest Python but can specify which Python to run:

* `py` - run latest Python version
* `py -2` - run the latest Python 2 version
* `py -3` - run the latest Python 3 version
* `py somefile.py` - run the specified Python module

The `py` program essentially wraps all Python versions and also provides a way to always run Python without conflicts in the `PATH` environment variable.
Note that it may not be necessary to use `py` if a [custom script]() is used to run a Python program,
which can specify the exact version of Python to use.

## Install pip to Install Add-on Packages

It may be necessary to install add-on packages that extend the basic Python functionality.

The [`pip` software](https://pip.pypa.io/en/stable/) is used to install Python packages and is the preferred installation tool since older tools such as `easy_install`
do not support current conventions.  Therefore, in order to install third-party packages, install pip first.
See the following resources:

* [Installing Packages](https://packaging.python.org/installing/) - should use `pip` if possible
* [Stack Overflow article on using `pip` when multiple Python versions are installed](http://stackoverflow.com/questions/10919569/how-to-install-a-module-use-pip-for-specific-version-of) -
it is possible

In summary:

* Add-on packages should install into a location consistent with the Python software install location.
* The `pip` utility should be used to install add-on packages.
* It is possible to use `pip` to install modules when multiple versions of Python are installed.
See the examples below for specific operating systems.

### Cygwin

The following uses a Cygwin `bash` shell.
To check for whether pip is already installed,:

```bash
py  --version
```

If not installed, install with the following, repeating for each Python installation:

```bash
py -m ensurepip
```

### Linux

The following uses a Linux `bash` shell.
To check for whether pip is already installed,:

```bash
py  --version
```

If not installed, install with the following, repeating for each Python installation:

```bash
py -m ensurepip
```

### Windows

The following uses a Windows Command Shell.  To check for whether pip is already installed,:

```com
py -2 -m pip --version
pip 7.0.1 from C:\Python27\lib\site-packages (python 2.7)

py -3 -m pip --version
pip 8.1.2 from C:\Users\sam\AppData\Local\Programs\Python\Python35-32\lib\site-packages (python 3.5)

```

If not installed, install with the following, repeating for each Python installation:

```com
py -2 -m ensurepip

py -3 -m ensurepip
```

## Install Third-party Packages

Third party packages typically have their own websites with installation instructions.  Follow those instructions within the configured
Python environment that is to receive the installation.  If necessary, check the Python version first to ensure compatibility with the
module and run `py` accordingly, for example to install [MkDocs software](http://www.mkdocs.org/) on Windows using the `py` program
(not used on Cygwin or Linux):

```com
py -2 -m pip install mkdocs

py -3 -m pip install mkdocs
```

## Create a Script to Run Python or a Python Program

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

Several of the above IDEs are discussed in more detail in later sections of this documentation.

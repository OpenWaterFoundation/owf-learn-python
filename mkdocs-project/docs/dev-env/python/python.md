# Development Environment / Python #

Python software is run using a Python interpreter.

* [Introduction](#introduction)
* [Install Python](#install-python)
	+ ![Cygwin](../../images/cygwin-32.png) [Install Python on Cygwin](#install-python-on-cygwin)
	+ ![Linux](../../images/linux-32.png) [Install Python on Linux](#install-python-on-linux)
	+ ![Windows](../../images/windows-32.png) [Install Python on Windows](#install-python-on-windows)
* [Install pip to Install Add-on Packages](#install-pip-to-install-add-on-packages)
	+ ![Cygwin](../../images/cygwin-32.png) [Install pip on Cygwin](#install-pip-on-cygwin)
	+ ![Linux](../../images/linux-32.png) [Install pip on Linux](#install-pip-on-linux)
	+ ![Windows](../../images/windows-32.png) [Install pip on Windows](#install-pip-on-windows)
* [Install Third-party Packages](#install-third-party-packages)
* [Install Integrated Development Environment](#install-integrated-development-environment)

----------

## Introduction ##

Python can be downloaded and installed from the Python website ([python.org/downloads](https://www.python.org/downloads/)).
If possible, install and use the latest 3.x version.
However, the choice of Python version may depend on integration with an existing environment,
and in some cases Python may be bundled with a software product.

To determine what version of Python is already installed and will run by default,
open a command shell in the target computer operating system
(Cygwin, Linux, or Windows), and check for the installed and default version:

```bash
$ python --version
Python 2.7.2
```

Even if nothing is listed, Python may still be installed on the system and may not have been configured in the `PATH`.
Refer to the following sections for instructions to install Python on different operating systems:

* Normal Installation - normal installations allow using Python for any purpose on a computer,
see installation instructions for various operating systems below
* [Bundled Python Installations](#bundled-python-installations) - when Python is packaged with a software product and is run independent of Python installed on the operating system
* [Virtual Python Environment](#virtual-python-environment) - used to isolate Python package installs from operating system Python install

### Bundled Python Installations ###

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

### Virtual Python Environment ###

Virtual environments are a newer approach that install Python packages
into virtual environment folder so that the installation of add-on Python packages does not
impact Python installations on the computer.
This option may also be appropriate in cases when administrative privileges are not available on the computer.
See additional information in the
[Development Tasks / Creating a Virtual Environment](../../dev-tasks/creating-venv) section.

## Install Python ##

The Python installation depends on the operating system.

### ![Cygwin](../../images/cygwin-32.png) Install Python on Cygwin ###

Python for [Cygwin](https://cygwin.com/install.html) is installed by selecting the Python interpreter in the install package listing.
The Python program is installed as /usr/bin/python or /usr/bin/python3 and supporting files are installed in /usr/lib/Python2.7/ and /usr/lib/Python3.4/
(the version numbers will increase as newer Python versions are released on Cygwin).
The latest supported Python for each major version is installed when the Cygwin installer is run.

Use `python` to run Python 2 and `python3` to run Python 3.  Both are installed in `/usr/bin`.

## ![Linux](../../images/linux-32.png) Install Python on Linux ##

Python for Linux is typically installed by following the instructions for the Linux distribution.
For example, see instructions:

* [Python on Debian Linux](https://wiki.debian.org/Python)

The Python program is typically installed as /usr/bin/python or /usr/bin/python3 and supporting files are installed in /usr/lib/Python2.7/ and /usr/lib/Python3.4/,
for example.  Consequently, the programs will typically be found in the `PATH`.

## ![Windows](../../images/windows-32.png) Install Python on Windows ##

Python for Windows is installed by following the instructions:

* [Python Windows download page](https://www.python.org/downloads/) - general download page
* [Python Releases for Windows](https://www.python.org/downloads/windows/) - downloads for Windows
	+ Make sure to pick the desired Python version, for example pick latest Python 2.7 or 3.7
	+ Make sure to pick the desired operating system version, for example ***Windows x86-64 executable installer*** for Widows 64-bit
* [Using Python on Windows (Python 3)](https://docs.python.org/3/using/windows.html) - explains the difference between user-specific and Windows system (`C:\Program Files) install.
* [Using Python on Windows (Python 2)](https://docs.python.org/2/using/windows.html)

Python can be installed in system location
`e.g., `C:\Program Files\Python37) or under user files (`C:\Users\user\AppData\Local\Python\Python37`).
The former requires administrator privileges whereas the latter does not (although this may not be consistent?).
Python versions prior to version 3.5 have default system installation folder `C:\Python27`, for example.
The followin table summarizes changes in defaults for different versions of Python
(need to update the table with more information).

| **Python Version** | **System Installation Folder** | **User Installation Folder**                           |
| ------------------ | ------------------------------ | ------------------------------------------------------ |
| Python 2.7         | `C:\Python27`                  | ?                                                      |
| Python 3.5+        | `C:\Program Files\...`         | `C:\Users\user\AppData\Local\Programs\Python\Python35` |

The installer will ask whether to modify the `PATH`.
Newer Python installations also install a program `py.exe` in the Windows `C:\Windows\py.exe` folder, which is always in the `PATH`.
In this case, specific Python programs such as `python3` will not be in the path
but bo exist in the installation folder.
Verify that `py` is available as follows:

```
> where py

```


The `py` program will by default run the latest Python but can specify which Python to run:

* `py` - run latest Python version
* `py -2` - run the latest Python 2 version
* `py -3` - run the latest Python 3 version
* `py somefile.py` - run the specified Python module

The `py` program essentially wraps all Python versions and also provides
a way to always run Python without conflicts in the `PATH` environment variable.
Note that it may not be necessary to use `py` if a
[custom script](../../running/run-python-program.md) is used to run a Python program,
which can specify the exact version of Python to use.

## Install pip to Install Add-on Packages ##

It is often necessary to install add-on packages that extend the basic Python functionality.

The [`pip` software](https://pip.pypa.io/en/stable/) is used to install Python packages and is the preferred installation tool since older tools such as `easy_install`
do not support current conventions.  Therefore, in order to install third-party packages, install `pip` first.
The `pip` software is often installed by default but may not be and will require installation.
In addition to installing a specific package, `pip` will install necessary dependencies.
See the following resources:

* [Installing Packages](https://packaging.python.org/installing/) - should use `pip` if possible
* [Stack Overflow article on using `pip` when multiple Python versions are installed](http://stackoverflow.com/questions/10919569/how-to-install-a-module-use-pip-for-specific-version-of) -
it is possible

In summary:

* Add-on packages should install into a location consistent with the Python software install location.
* The `pip` utility should be used to install add-on packages.
* It is possible to use `pip` to install modules when multiple versions of Python are installed.
In general, make sure that the correct `pip` version is used by confirming the `pip` install location
that is found in the `PATH` (using `where` on Windows, and `which` on Cygwin/Linux).
If necessary, type the full path to the `pip` version to use.
Also use `pip3` if necessary to avoid confusion with Python2 `pip`.
The `pip` and `pip3` programs may be equivalent on a system where only Python3 is installed.
However, `pip` and `pip3` may be different programs depending on which Python versions are installed.
* If `pip` prints messages about how to update itself, follow those instructions.
* See the examples below for specific operating systems.

### ![Cygwin](../../images/cygwin-32.png) Install pip on Cygwin ###

The following uses a Cygwin `bash` shell.
To check whether pip is already installed,:

```bash
pip --version
pip3 --version
```

If not installed, install with the following, repeating for each Python installation:

```bash
$ python -m ensurepip
$ python3 -m ensurepip
```

### ![linux](../../images/linux-32.png) Install pip on Linux ###

The following uses a Linux `bash` shell.
To check whether pip is already installed,:

```bash
pip --version
pip3 --version
```

If not installed, install with the following, repeating for each Python installation:

```bash
$ python -m ensurepip
$ python3 -m ensurepip
```

### ![Windows](../../images/windows-32.png) Install pip on Windows ###

The following uses a Windows Command Shell.  To check whether pip is already installed:

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

## Install Third-party Packages ##

Third party packages typically have their own websites with installation instructions.
Follow those instructions within the configured Python environment that is to receive the installation.
If necessary, check the Python version first to ensure compatibility with the
package and run `pip` or `pip3` accordingly.

## Install Integrated Development Environment ##

An Integrated Development Environment (IDE) is helpful for development because
it provides an integrated edit/run/test/build/deploy environment.

See the list of [IDEs in the Overview](../overview).

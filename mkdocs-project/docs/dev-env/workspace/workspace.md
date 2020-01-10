# Development Environment / Workspace #

The following information explains how to determine a location for development files.
This location is often called a software developer's "workspace".

| **Operating System** | **Information** | **Description** |
| -- | -- | -- |
|  | [Introduction](#introduction) | Introduction for workspace concept. |
| ![windows](../../images/windows-32.png) | See below:  [Workspace for Windows](#workspace-for-windows) | Determine workspace for Windows. |
| ![cygwin](../../images/cygwin-32.png) | See below:  [Workspace for Cygwin](#workspace-for-cygwin) | Determine workspace for Cygwin. |
| ![gitbash](../../images/gitbash-32.png) | See below:  [Workspace for Git Bash](#workspace-for-git-bash) | Determine workspace for Git Bash. |
| ![linux](../../images/linux-32.png) | See below:  [Workspace for Linux](#workspace-for-linux) | Determine workspace for Linux. |

------------------

## Introduction ##

A "workspace" is a location where development files will exist.
These files are typically located in the software developer's files so as to not get confused with other users or
operating system files, and are typically organized by software project or product.
Some considerations for the location of workspace files are:

1. Are the files mainly associated with a developer's personal work,
in which case the files can exist in any folder chosen by the developer.
2. Does a software program/project suggest a location in order to maintain consistency between users?
3. Does a development environment tool recommend standard locations?

The remainder of this page makes general recommendations based on the operating system;
however, the above and other considerations should be evaluated.

## ![windows](../../images/windows-32.png) Workspace for Windows ##

Development files on Windows are typically located under a user's `C:\Users\user` folder.
Although Windows provides some standard folders such as `Documents`,
it is recommended that one or more folders be created that are clearly for development.

One convention is to organize development folders based on the following hierarchy:

* Organization 1 (for which development occurs)
	+ Product1
	+ Product2
* Organization 2 (for which development occurs)
	+ ProductA
	+ ProductB

This allows development work to be easily found and managed.
An example at the Open Water Foundation is as follows.
Links to products provide access to `README` files that further illustrate file organization.

* `C:/Users/user/`
	+ `cdss-dev/` (work done as part of [Colorado's Decision Support Systems](https://www.colorado.gov/cdss))
		- `TSTool/` ([TSTool](https://github.com/OpenCDSS/cdss-app-tstool-main) software)
		- `StateDMI/` ([StateDMI](https://github.com/OpenCDSS/cdss-app-statedmi-main) software)
	+ `my-dev/` (personal work, such as training and rough prototypes)
		- `Project1/`
		- `Project2/`
	+ `owf-dev/` (work done for Open Water Foundation)
		- `GeoProcessor/` ([GeoProcessor](https://github.com/OpenWaterFoundation/owf-app-geoprocessor-python) software)
		- `Learn-Python/` ([this documentation](https://github.com/OpenWaterFoundation/owf-learn-python))

The following are also considerations:

* Text files created in Windows typically use Windows end of line (`CR``LF`).
* Windows files will be directly visible to Cygwin and Git Bash.
* Windows files can also be shared with Linux.

## ![cygwin](../../images/cygwin-32.png) Workspace for Cygwin ##

Although Cygwin home folder (`/home/user`) could be used,
development files for Cygwin are typically shared with the Windows location
to avoid having a redundant development folder, with the following considerations:

* The user's home folder that maps to Windows is similar to `/cygdrive/C/Users/user`.
* Text files created in Cygwin typically UNIX end of line (`LF`).

## ![gitbash](../../images/gitbash-32.png) Workspace for Git Bash ##

Development files for Git Bash are typically shared with the Windows location,
with the following considerations:

* The user's home folder in Git Bash is similar to `/c/Users/user`.
* Text files created in Git Bash typically use the UNIX end of line (`LF`).

## ![windows](../../images/linux-32.png) Workspace for Linux ##

Development files for Linux are similar to Windows (see above), with the following considerations:

* The user's home folder is similar to `/home/user`.
* Text files created in Linux will typically have Linux end of line (`LF`).

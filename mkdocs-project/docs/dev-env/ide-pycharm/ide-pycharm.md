# Development Environment / IDE (PyCharm) #

The PyCharm integrated development environment (IDE) is one option for a Python development environment.
PyCharm is part of the JetBrains family of development tools, which also includes IDEs for other languages.

* [Installing](#installing)
* [Troubleshooting](#troubleshooting)

-----------------------------

## Installing ##

The free PyCharm Community edition is often adequate for most projects.

* [Download PyCharm](https://www.jetbrains.com/pycharm/download)

## Troubleshooting ##

The following are issues that may require troubleshooting:

* [PyCharm changes file permissions to executable](#pycharm-changes-file-permissions-to-executable)
* [PyCharm is slow](#pycharm-is-slow)

### PyCharm changes file permissions to executable ###

In some environments, editing and saving files in PyCharm results in the file permissions having execute permission.
For example, this behavior has been seen when using PyCharm on a Windows environment and also working with files in Cygwin.
It appears that the limitations and incompatibility of Windows and Cygwin file system cause this issue.

New files created by PyCharm may always exhibit this behavior and may need permissions changed on the Cygwin command line.
However, for modified files, the default setting is that PyCharm creates temporary files rather than directly updating files.
See the following which indicates a problem for Java files but the same occurs for other source files:

* [Stack Overflow article:  Why does IntelliJ mark .java files as executable?](https://stackoverflow.com/questions/16988657/why-does-intellij-mark-java-files-as-executable)
* [Linked from above:  IDE changes the file permissions on Windows and Samba](https://youtrack.jetbrains.com/issue/IDEA-74433).

The follow improves the issue by preventing permission changes on existing files (using PyCharm version 2018.3 for this example):

***File / Settings / Appearance & Behavior / System Settings / Synchronization***

Change the ***Use "safe write" (save changes to a temporary file first)*** setting to unchecked.

### PyCharm is slow ###

PyCharm can be slow, especially when editing large projects.
Currently no recommendations are provided here for how to improve but it would be great to add some.

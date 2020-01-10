# Lesson / Users and Permissions

**Level:  Basic**

**Estimated Time:  5 Minutes**

* [Lesson Introduction](#lesson-introduction)
* [Windows Users](#windows-users)
* [Linux Users](#linux-users)

------------

## Lesson Introduction ##

Operating systems allow access to the system via a user login.
An administrator account is used to add new users and perform system administration tasks.
Permissions are used to restrict read and write access to to folders and files.
For example, it is typical that software can only be installed in system folders by an administrator account.

## ![windows](../images/windows-32.png) Windows Users ##

On Windows, most users have a normal ("Local") account, with user files in the `C:\Users\user` folder,
where `user` is the specific user.

Software is typically installed in the `C:\Program Files\` folder;
however, this requires Administrator privileges.
As an alternative, some software allows installing a local user copy of software in
`C:\Users\user\AppData`, which allows software to be installed without Administrator privileges.
Software needed for development may be installed in user files.

If it is necessary to install software as an Administrator,
the operating system will prompt for the administrator password.

## ![linux](../images/linux-32.png) Linux Users ##

On Linux, most users have a normal account, with user files in the `/home/user` folder,
where `user` is the specific user.
Most Linux software installs in standard system folders rather than user folders,
although software needed for development may be installed in user files.

If it is necessary to install software as an administrator,
it is typical to grant `sudo` permissions to a user and then use the `sudo` command.

It is also possible to login to a "root" user account, with files in `/root`.
However, using `sudo` is recommended rather than logging in as `root`.

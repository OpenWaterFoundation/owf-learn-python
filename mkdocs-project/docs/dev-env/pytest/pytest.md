# Developer Environment / pytest #

Python has built-in unit test features:

* [Python2](https://docs.python.org/2/library/unittest.html)
* [Python3](https://docs.python.org/3/library/unittest.html)

However, the `pytest` software is a useful tool that provides enhanced unit test features,
which can can also be used for functional testing of Python and other software.

See the [pytest documentation](http://doc.pytest.org/en/latest/).

See also a [comparison of Python testing frameworks](http://pythontesting.net/podcast/pytest-vs-unittest-vs-nose-pt002/).

## Install pytest ##

To install `pytest` for the installed Python 2 environment and assuming `pip` is installed, run the following on Windows, Cygwin, or Linux:

```
$ pip install -U pytest
Collecting pytest
  Downloading pytest-3.0.3-py2.py3-none-any.whl (169kB)
    100% | 172kB 1.7MB/s
Collecting py>=1.4.29 (from pytest)
  Downloading py-1.4.31-py2.py3-none-any.whl (81kB)
    100% | 86kB 2.3MB/s
Installing collected packages: py, pytest
Successfully installed py-1.4.31 pytest-3.0.3

```

## Additional pytest Configuration

The following may be useful:  [improve slow startup](http://stackoverflow.com/questions/30768254/pytest-py-test-very-slow-startup-in-cygwin).

## Writing pytest Tests

See the [testing task documentation](../../dev-tasks/testing-pytest/) for examples of tests.

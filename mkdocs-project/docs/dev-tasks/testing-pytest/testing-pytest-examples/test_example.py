# Simple pytest examples
import os;

#-----------------------------------
def func(x):
    """
    Add 1 to a number and returns the new value.
    """
    return x + 1

def test_answer():
    """
    Example test that should always generate a failure.
    """
    assert func(3) == 5, "Result does not equal 4"
#-----------------------------------

def test_hello_world(tmpdir):
    """
    Test running an external program, reading its output, and comparing with expected result.
    In this case the expected result is hard-coded in the test.
    """
    file = tmpdir.join('helloworld.txt')
    # The following would be replaced with a system call
    command = 'echo "Hello World" > ' + str(file)
    print(command)
    os.system(command)
    assert file.read().strip() == "Hello World"

#-----------------------------------
def writetoafile(fname):
    """
    Function to write line to an output file.
    """
    with open(fname, 'w') as fp:
        fp.write('Hello World')

def test_writetofile(tmpdir):
    """
    Test whether function that writes a line to file works.
    """
    file = tmpdir.join('output.txt')
    writetoafile(file.strpath)  # or use str(file)
    assert file.read().strip() == 'Hello World'
#-----------------------------------

# Running a Python Program

## Specify Python Interpreter

Python programs with source code in files with .py extension
can be compiled, but for general purpose use and transparency are distributed as text in the original files
A Python program is run by specifying the main Python program filename as the first commmand line parameter to the interpreter:

```bash
python hello-world.py
```

where the hello-world.py file contains:

```python
print("Hello world")
```

## Main Entry Point in Python Program

The interpreter will execute the Python program from top to bottom.  If the code does not contain any functions and simply 
contains Python commands, then those commands are executed in sequence.
This is appropriate for very simple programs or modules;
however, in most cases the program will be complex enough to require functions.

When the Python interpreter reads a source file, it defines a few special variables.  If the interpreter is running the program
as the main file (as specified on the command line when starting Python), the interpreter sets a special `__name__` variable
to have a value of "\_\_main\_\_".  If the module is imported and executed, then `__name__` is set to the module name.
This allows the following syntax to be used in the program file:


```code
def main():
	'''
	Main program...
	'''
	# The following are not required...just an example
	# Parse command line parameters
	parseArgs() 
	# Initialize for run
	initialize()
	# Insert some logic here if not handled in called function
	# Close down
	shutdown()
	return
	

if ( __name__ == "__main__" ):
	# Run the main function
	main()
```

## Graceful Exit

Need to discuss here graceful exit so that calling program can check the exit status for success or failure.

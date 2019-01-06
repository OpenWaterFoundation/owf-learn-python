# example-logging2.py
#
# Example of Python 2 logging:
# - Initialize logging in a function called from main at startup.
# - Configure basic file logging.
# - Coding style should be modifed as appropriate to match development team standards.
#
# TODO:
# - Provide command line parsing to set logging level for different components, console vs. file, etc.
# - Provide command line parsing to specify location of log file.

# Python standard modules
import logging
import os

# Python modules for application
import mylib 

def main():
    """
    Main program, called when program starts.
    """
    parse_command_line()
    # Setup logging using defaults reflecting command line overrides
    logfileName = "example-logging2.log"
    logfileLevel = logging.INFO
    logfileFormat = '%(asctime)s %(levelname)s: %(message)s'
    # Note that before this point, must use print() to print to console if need to troubleshoot
    setup_logging(logfileName,logfileLevel,logfileFormat)
    logging.info('Started')
    # Here insert code to do the work of this program via other function calls
    # The example calls a simple function, which uses logging
    mylib.do_something()
    logging.info('Finished')
    return

def parse_command_line():
    """
    Parse command line parameters.
    """
    # TODO - need to implement command line parsing
    return

def setup_logging(logfileName,logfileLevel,logfileFormat):
    """
    Setup logging for this program.
    See:  https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
    logfileName -- name (or path) of log file for logging
    logfileLevel -- logging level for log file (for example:  logging.INFO)
    logfileFormat -- format to use for logging messages (using logging.basicConfig(format) specification
    """
    # Remove the old log file first (use advanced logging to control other ways)
    if ( os.path.isfile(logfileName) ):
        os.remove(logfileName)
    logging.basicConfig(filename=logfileName,level=logfileLevel,format=logfileFormat)
    return

if ( __name__ == '__main__' ):
    # Name of this module is __main__ so it is being run as a main program.
    main()

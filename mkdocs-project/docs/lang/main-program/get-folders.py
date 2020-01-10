# Simple program to illustrate getting important folders

import os

# Main program entry point
if __name__ == '__main__':
    print("")
    print("Current working directory = " + os.getcwd())

    current_file = __file__
    print("Software installation directory = " + os.path.realpath(current_file))

    exit(0)

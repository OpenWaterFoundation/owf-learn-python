# Simple program to illustrate using module data as static data

from DayOfWeekType import DayOfWeekType

# Main program entry point
if __name__ == '__main__':
    # Want to control some logic by day
    today = DayOfWeekType.MONDAY

    print("\nDoing tasks for " + str(today) + "\n")
    # Note that "is" is used for comparison rather than "==" although "==" will work
    if today is DayOfWeekType.MONDAY:
        # Do some tasks for Monday
        pass

    # Actually, module data are not really static because variables can be modified
    DayOfWeekType.MONDAY = "Friday"
    print("Monday after changing = " + str(DayOfWeekType.MONDAY))

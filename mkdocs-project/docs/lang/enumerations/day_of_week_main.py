# Simple program to illustrate using module data as static data

import day_of_week

# Main program entry point
if __name__ == '__main__':
    # Want to control some logic by day
    today = day_of_week.MONDAY

    print("Doing tasks for " + today)
    if today == day_of_week.MONDAY:
        # Do some tasks for Monday
        pass

    # Actually, module data are not really static because variables can be modified
    day_of_week.MONDAY = "Friday"
    print("Monday after changing = " + day_of_week.MONDAY)

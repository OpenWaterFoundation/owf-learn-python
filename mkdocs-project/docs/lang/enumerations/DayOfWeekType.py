# Day of week enumeration

from enum import Enum


class DayOfWeekType(Enum):
    """
    Enumeration for day of week.
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

    def __str__(self):
        """
        Format the enumeration as a string - just return the value.
        This is needed because the default is to return the name as in MONDAY (uppercase).
        """
        return self.value
